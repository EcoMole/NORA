# Generated by Django 4.2.14 on 2024-11-05 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "taxonomies",
            "0008_alter_population_qualifier_alter_population_subgroup_and_more",
        ),
        ("composition", "0011_alter_composition_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="composition",
            name="qualifier",
            field=models.ForeignKey(
                blank=True,
                db_column="id_qualifier",
                help_text="(QUALIFIER vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "QUALIFIER"),
                    (
                        "extended_name__in",
                        [
                            "Equal to",
                            "Less than",
                            "Less than or equal",
                            "Greater than",
                            "Greater than or equal",
                            "Circa",
                            "traces",
                        ],
                    ),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="qualifier_compositions",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="composition",
            name="unit",
            field=models.ForeignKey(
                blank=True,
                db_column="id_unit",
                help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "UNIT"),
                    models.Q(("short_name", "root"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="unit_compositions",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="novelfoodvariant",
            name="food_form",
            field=models.ForeignKey(
                blank=True,
                db_column="id_food_form",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="composition.foodform",
            ),
        ),
        migrations.AlterField(
            model_name="parameter",
            name="vocab_id",
            field=models.ForeignKey(
                blank=True,
                db_column="id_param",
                help_text="(PARAM vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "PARAM"),
                    models.Q(("short_name", "root"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="vocab_id_parameters",
                to="taxonomies.taxonomynode",
                verbose_name="Parameter Vocabulary Identification",
            ),
        ),
        migrations.AlterField(
            model_name="productionnovelfoodvariant",
            name="process",
            field=models.ForeignKey(
                db_column="id_process",
                help_text="(MTX vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "MTX"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_process", True),
                ),
                on_delete=django.db.models.deletion.PROTECT,
                related_name="process_production_novel_food_variants",
                to="taxonomies.taxonomynode",
                verbose_name="Process Step",
            ),
        ),
        migrations.AlterField(
            model_name="proposeduse",
            name="population",
            field=models.ForeignKey(
                blank=True,
                db_column="id_age",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="population_proposed_uses",
                to="taxonomies.population",
                verbose_name="Target Population",
            ),
        ),
        migrations.AlterField(
            model_name="riskassessredflagnfvariant",
            name="risk_assess_red_flag",
            field=models.ForeignKey(
                db_column="id_risk_assess_red_flag",
                on_delete=django.db.models.deletion.PROTECT,
                to="composition.riskassessredflag",
                verbose_name="Risk Assessment Red Flag",
            ),
        ),
    ]
