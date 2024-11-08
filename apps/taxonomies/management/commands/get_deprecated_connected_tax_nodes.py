# encoding: utf-8

from django.apps import apps
from django.core.management.base import BaseCommand
from django.db.models import ForeignKey
from taxonomies.models import TaxonomyNode


class Command(BaseCommand):
    help = (
        "Provides a list of TaxonomyNode objects with status 'deprecated' "
        "that are used as foreign keys in any objects, "
        "except for objects of models TaxonomyNode or Taxonomy."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "app_label", type=str, help="App label to check all models within"
        )
        parser.add_argument(
            "--exclude-models",
            type=str,
            default="",
            help="Optional: Comma-separated list of model names to exclude "
            '(e.g., "TaxonomyNode, Taxonomy")',
        )

    def handle(self, *args, **options):
        app_label = options["app_label"]
        exclude_models = {
            model_name.strip() for model_name in options["exclude_models"].split(",")
        }
        exclude_models.update({"TaxonomyNode", "Taxonomy"})

        try:
            app_config = apps.get_app_config(app_label)
        except LookupError:
            self.stdout.write(self.style.ERROR(f'App "{app_label}" not found'))
            return

        models = app_config.get_models()
        if not models:
            self.stdout.write(self.style.ERROR(f'No models found in app "{app_label}"'))
            return

        deprecated_taxonomy_nodes = TaxonomyNode.objects.filter(
            status=TaxonomyNode.STATUS.DEPRECATED
        )
        if not deprecated_taxonomy_nodes.exists():
            self.stdout.write("No deprecated TaxonomyNode instances found.")
            return

        for model in models:
            if model.__name__ in exclude_models:
                continue

            # Get all ForeignKey fields pointing to TaxonomyNode
            fk_fields = [
                field
                for field in model._meta.get_fields()
                if isinstance(field, ForeignKey) and field.related_model == TaxonomyNode
            ]
            if not fk_fields:
                continue

            self.stdout.write(f"Inspecting model: {model.__name__}")
            for fk_field in fk_fields:
                field_name = fk_field.name
                model_name = model.__name__
                lookup = f"{field_name}__in"
                related_objects = model.objects.filter(
                    **{lookup: deprecated_taxonomy_nodes}
                )

                if related_objects.exists():
                    count = related_objects.count()
                    self.stdout.write(
                        f"\n\nFound {count} {model_name} instances with field '{field_name}' "
                        "linked to deprecated TaxonomyNode\n\n"
                        f" - <deprecated TaxonomyNode> - <{model_name} instances "
                        "linked to the deprecated TaxonomyNode> "
                        f"(ID: <{model_name} instance ID>)\n\n"
                    )

                    for rel_obj in related_objects:
                        taxonomy_node = getattr(rel_obj, field_name)
                        self.stdout.write(
                            f" - {taxonomy_node} - {rel_obj} (ID: {rel_obj.id})"
                        )
