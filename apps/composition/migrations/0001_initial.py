# Generated by Django 4.2.13 on 2024-06-24 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("novel_food", "0001_initial"),
        ("taxonomies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FoodForm",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_food_form", primary_key=True, serialize=False
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Title of the food form", max_length=255
                    ),
                ),
            ],
            options={
                "verbose_name": "Food Form",
                "verbose_name_plural": "📂 Food Forms",
                "db_table": "FOOD_FORM",
            },
        ),
        migrations.CreateModel(
            name="NovelFoodVariant",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_nf_variant", primary_key=True, serialize=False
                    ),
                ),
                (
                    "food_form",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_food_form",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="composition.foodform",
                    ),
                ),
                (
                    "novel_food",
                    models.ForeignKey(
                        db_column="study_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.novelfood",
                    ),
                ),
            ],
            options={
                "verbose_name": "Novel Food Variant 🥗",
                "verbose_name_plural": "Novel Food Variants 🥗",
                "db_table": "NOVEL_FOOD_VARIANT",
            },
        ),
        migrations.CreateModel(
            name="ParameterType",
            fields=[
                (
                    "id_parameter_type",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Parameter type", max_length=255, unique=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Parameter Type",
                "verbose_name_plural": "📂 Parameter Types",
                "db_table": "PARAMETER_TYPE",
            },
        ),
        migrations.CreateModel(
            name="ProposedUseType",
            fields=[
                ("id_use_type", models.AutoField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(
                        choices=[
                            ("whole_foods", "Whole foods"),
                            ("food_ingredients", "Food ingredients"),
                            ("food_supplements", "Food supplements"),
                            (
                                "infant_follow_on_formula",
                                "Infant formula and follow-on formula",
                            ),
                            (
                                "special_medical_purpose",
                                "Food for special medical purposes",
                            ),
                            (
                                "total_diet_replacement",
                                "Total diet replacement for weight control",
                            ),
                        ],
                        help_text="Title of the proposed use type",
                        max_length=255,
                    ),
                ),
            ],
            options={
                "verbose_name": "Proposed Use Type",
                "verbose_name_plural": "📂 Proposed Use Types",
                "db_table": "PROPOSED_USE_TYPE",
            },
        ),
        migrations.CreateModel(
            name="RiskAssessmentRedFlags",
            fields=[
                (
                    "id_risk_assessment_red_flags",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Title of the risk assessment red flags",
                        max_length=255,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RiskAssessmentRedFlagsNFVariant",
            fields=[
                (
                    "id_risk_assessment_red_flags_novel_food",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "nf_variant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="composition.novelfoodvariant",
                    ),
                ),
                (
                    "risk_assessment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="composition.riskassessmentredflags",
                    ),
                ),
            ],
            options={
                "verbose_name": "Risk assessment red flag",
                "verbose_name_plural": "Risk assessment red flags",
            },
        ),
        migrations.CreateModel(
            name="ProposedUse",
            fields=[
                (
                    "id_proposed_use",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "nf_variant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="composition.novelfoodvariant",
                    ),
                ),
                (
                    "population",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_age",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="population_proposed_uses",
                        to="taxonomies.population",
                    ),
                ),
                (
                    "use_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="composition.proposedusetype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductionNovelFoodVariant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "id_novel_food_variant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="composition.novelfoodvariant",
                    ),
                ),
                (
                    "process",
                    models.ForeignKey(
                        blank=True,
                        help_text="(MTX vocab)",
                        limit_choices_to={"taxonomy__code": "MTX"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="process_production_novel_food_variants",
                        to="taxonomies.taxonomynode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Production Process",
                "verbose_name_plural": "Production Process",
            },
        ),
        migrations.CreateModel(
            name="Parameter",
            fields=[
                ("id_parameter", models.AutoField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(
                        help_text="Parameter", max_length=255, unique=True
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="composition.parametertype",
                    ),
                ),
                (
                    "vocab_id",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_param",
                        help_text="(PARAM vocab)",
                        limit_choices_to={"taxonomy__code": "PARAM"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="vocab_id_parameters",
                        to="taxonomies.taxonomynode",
                        verbose_name="Parameter Vocabulary Identification",
                    ),
                ),
            ],
            options={
                "verbose_name": "Parameter",
                "verbose_name_plural": "📂 Parameters",
                "db_table": "PARAMETER",
            },
        ),
        migrations.AddField(
            model_name="novelfoodvariant",
            name="risk_assessment_red_flags",
            field=models.ManyToManyField(
                through="composition.RiskAssessmentRedFlagsNFVariant",
                to="composition.riskassessmentredflags",
            ),
        ),
        migrations.CreateModel(
            name="Composition",
            fields=[
                ("id_composition", models.AutoField(primary_key=True, serialize=False)),
                (
                    "value",
                    models.DecimalField(
                        blank=True,
                        decimal_places=4,
                        help_text="Value of the parameter",
                        max_digits=10,
                        null=True,
                    ),
                ),
                (
                    "upper_range_value",
                    models.DecimalField(
                        blank=True,
                        decimal_places=4,
                        help_text="Optional upper range value of the parameter",
                        max_digits=10,
                        null=True,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("specification", "Specification"),
                            ("characterisation", "Characterisation"),
                            ("other", "Other"),
                        ],
                        help_text="Specification/Composition/Other",
                        max_length=255,
                    ),
                ),
                ("footnote", models.TextField(blank=True)),
                (
                    "novel_food_variant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="composition.novelfoodvariant",
                    ),
                ),
                (
                    "parameter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="composition.parameter",
                    ),
                ),
                (
                    "qualifier",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_qualifier",
                        help_text="(QUALIFIER vocab)",
                        limit_choices_to={"taxonomy__code": "QUALIFIER"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="qualifier_compositions",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_unit",
                        help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
                        limit_choices_to={"taxonomy__code": "UNIT"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="unit_compositions",
                        to="taxonomies.taxonomynode",
                    ),
                ),
            ],
        ),
    ]
