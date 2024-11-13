# encoding: utf-8

from django.apps import apps
from django.core.management.base import BaseCommand
from django.db.models import ForeignKey
from taxonomies.models import TaxonomyNode


class Command(BaseCommand):
    help = "Provides a list of all the cases where connected TaxonomyNode is "
    "outside the limit_choices_to"

    def add_arguments(self, parser):
        # use: "admin, administrative, api, authentication, composition, core, extractor,
        # novel_food, studies, taxonomies"
        parser.add_argument(
            "app_labels",
            type=str,
            default="",
            help='App labels to check all models within (e.g., "novel_food, administrative")',
        )
        parser.add_argument(
            "--exclude-models",
            type=str,
            default="",
            help="Optional: Comma-separated list of model names to exclude "
            '(e.g., "TaxonomyNode, Taxonomy")',
        )

    def handle(self, *args, **options):
        app_labels = {
            model_name.strip() for model_name in options["app_labels"].split(",")
        }
        exclude_models = {
            model_name.strip() for model_name in options["exclude_models"].split(",")
        }
        exclude_models.update(
            {
                "TaxonomyNode",
                "Taxonomy",
                "ImplicitAttribute",
                "ExtendedTaxonomyNodeInformation",
            }
        )
        for app_label in app_labels:
            try:
                app_config = apps.get_app_config(app_label)
            except LookupError:
                self.stdout.write(self.style.ERROR(f"App {app_label} not found"))
                return

            self.stdout.write("")
            self.stdout.write(f"INSPECTING APP: {app_label}")
            models = app_config.get_models()
            if not models:
                self.stdout.write(
                    self.style.ERROR(f'No models found in app "{app_label}"')
                )
                return

            for model in models:
                model_name = model.__name__
                if model_name in exclude_models:
                    continue
                self.stdout.write(f"Inspecting model: {model_name}")

                fk_fields = [
                    field
                    for field in model._meta.get_fields()
                    if isinstance(field, ForeignKey)
                    and field.related_model == TaxonomyNode
                    and hasattr(field.remote_field, "limit_choices_to")
                    and field.remote_field.limit_choices_to
                ]
                if not fk_fields:
                    continue
                for obj in model.objects.all():
                    for fk_field in fk_fields:
                        limit_choices_to = fk_field.remote_field.limit_choices_to
                        field_name = fk_field.name
                        fk_value = getattr(obj, field_name)
                        if fk_value and fk_value not in TaxonomyNode.objects.filter(
                            limit_choices_to
                        ):
                            self.stdout.write(
                                f"- {fk_value} - Field: {field_name} - Model: {model_name}, "
                                f"Object ID: {obj.id} - Object: {str(obj)}"
                            )
