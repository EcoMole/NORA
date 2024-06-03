# Generated by Django 4.2.13 on 2024-06-03 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("taxonomies", "0001_initial"),
        ("administrative", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Allergenicity",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_allergenicity", primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Allergenicity",
                "verbose_name_plural": "Allergenicity - options",
                "db_table": "ALLERGENICITY",
            },
        ),
        migrations.CreateModel(
            name="AllergenicityNovelFood",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_allergenicity_novel_food",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "allergenicity",
                    models.ForeignKey(
                        db_column="id_allergenicity",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.allergenicity",
                        verbose_name="Allergenicity",
                    ),
                ),
            ],
            options={
                "verbose_name": "Allergenicity Assignment",
                "verbose_name_plural": "Allergenicity Assignments",
                "db_table": "ALLERGENICITY_NOVEL_FOOD",
            },
        ),
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=255)),
                ("definition", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "regulation",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_regulation",
                        limit_choices_to={"taxonomy__code": "LEGREF"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="taxonomies.taxonomynode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Novel Food Category",
                "verbose_name_plural": "NF Categories - options",
                "db_table": "SUB_TYPE",
            },
        ),
        migrations.CreateModel(
            name="Chemical",
            fields=[
                (
                    "id_chemical",
                    models.AutoField(
                        db_column="id_component", primary_key=True, serialize=False
                    ),
                ),
                (
                    "catalogue_identity",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"taxonomy__code": "PARAM"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="catalogue_identity_chemicals",
                        to="taxonomies.taxonomynode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Chemicals",
                "verbose_name_plural": "Chemicals",
                "db_table": "COMPONENT",
            },
        ),
        migrations.CreateModel(
            name="ChemicalType",
            fields=[
                (
                    "id_chemical_type",
                    models.AutoField(
                        db_column="id_component_type", primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("definition", models.CharField(max_length=2000)),
            ],
            options={
                "verbose_name": "Chemical type (future use)",
                "verbose_name_plural": "Chemical types (future use)",
                "db_table": "COM_TYPE",
            },
        ),
        migrations.CreateModel(
            name="FoodCategory",
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
                ("title", models.CharField(max_length=255)),
                ("definition", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Food category",
                "verbose_name_plural": "Food categories - options",
            },
        ),
        migrations.CreateModel(
            name="GenotoxFinalOutcome",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_genotox_final_outcome",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255)),
            ],
            options={
                "verbose_name": "Genotoxicity final outcome",
                "verbose_name_plural": "Genotoxicity final outcomes",
                "db_table": "GENOTOX_FINAL_OUTCOME",
            },
        ),
        migrations.CreateModel(
            name="NovelFood",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_study", primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="NF Name")),
                ("nf_code", models.CharField(max_length=2000, verbose_name="NF Code")),
                ("shelflife_value", models.FloatField(blank=True, null=True)),
                (
                    "outcome_remarks",
                    models.CharField(blank=True, max_length=2000, null=True),
                ),
                (
                    "allergenicity",
                    models.ManyToManyField(
                        related_name="allergenicity_novel_foods",
                        through="novel_food.AllergenicityNovelFood",
                        to="novel_food.allergenicity",
                    ),
                ),
                (
                    "antinutritional_factors",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_antinutritional_factors",
                        limit_choices_to={"taxonomy__code": "YESNO"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="antinutritional_factors_novel_foods",
                        to="taxonomies.taxonomynode",
                        verbose_name="Antinutritional factors",
                    ),
                ),
                (
                    "carcinogenicity",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_is_carcinogenic",
                        limit_choices_to={"taxonomy__code": "YESNO"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="carcinogenicity_novel_foods",
                        to="taxonomies.taxonomynode",
                        verbose_name="Carcinogenicity",
                    ),
                ),
                (
                    "catalogue_identity",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_rms_efsa",
                        limit_choices_to={"taxonomy__code": "PARAM"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="catalogue_identity_novel_foods",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "endocrine_disrupt_prop",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_has_endocrine_disrupt_prop",
                        limit_choices_to={"taxonomy__code": "YESNO"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="endocrine_disrupt_prop_novel_foods",
                        to="taxonomies.taxonomynode",
                        verbose_name="has endocrine disrupt properties",
                    ),
                ),
                (
                    "food_category",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_food_category",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="food_category_novel_foods",
                        to="novel_food.foodcategory",
                    ),
                ),
                (
                    "food_matrices",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_is_food_matrices",
                        help_text="Were food matrices provided?",
                        limit_choices_to={"taxonomy__code": "YESNO"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="food_matrices_novel_foods",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "genotox_final_outcome",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_is_genotoxic",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="genotox_final_outcome_novel_foods",
                        to="novel_food.genotoxfinaloutcome",
                    ),
                ),
                (
                    "instability_concerns",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_instability_concerns",
                        limit_choices_to={"taxonomy__code": "YESNO"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="instability_concerns_novel_foods",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "mutagenicity",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_is_mutagenic",
                        limit_choices_to={"taxonomy__code": "YESNO"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="mutagenicity_novel_foods",
                        to="taxonomies.taxonomynode",
                        verbose_name="Mutagenicity",
                    ),
                ),
            ],
            options={
                "verbose_name": "Novel Food",
                "verbose_name_plural": "Novel Foods",
                "db_table": "STUDY",
            },
        ),
        migrations.CreateModel(
            name="Organism",
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
                    "organism_node",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"taxonomy__code": "MTX"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="taxonomies.taxonomynode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Organism",
                "verbose_name_plural": "Organisms",
                "db_table": "ORGANISM",
            },
        ),
        migrations.CreateModel(
            name="StructureReported",
            fields=[
                (
                    "id_structure_reported",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=255)),
                ("definition", models.CharField(max_length=2000)),
            ],
            options={
                "verbose_name": "Structure reported (future use)",
                "verbose_name_plural": "Structures reported (future use)",
                "db_table": "COM_STRUCTURE_SHOWN",
            },
        ),
        migrations.CreateModel(
            name="SynonymType",
            fields=[
                (
                    "id_synonym_type",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "synonym_type",
                    models.CharField(
                        help_text="Type of synonym -e.g. common name, trade name, synonym",
                        max_length=255,
                    ),
                ),
                ("definition", models.CharField(blank=True, max_length=2000)),
            ],
            options={
                "verbose_name": "Synonym Type",
                "verbose_name_plural": "Synonym types - options",
                "db_table": "SYNONYM",
            },
        ),
        migrations.CreateModel(
            name="SubstanceOfConcernNovelFood",
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
                    "novel_food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.novelfood",
                    ),
                ),
                (
                    "substance_of_concern",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_sub_of_concern",
                        limit_choices_to={"taxonomy__code": "PARAM"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="substance_of_concern_substance_of_concern_novel_foods",
                        to="taxonomies.taxonomynode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Substance of concern",
                "db_table": "SUBSTANCE_OF_CONCERN_STUDY",
            },
        ),
        migrations.CreateModel(
            name="OrganismSyn",
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
                ("synonym", models.CharField(max_length=255)),
                (
                    "organism",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.organism",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.synonymtype",
                    ),
                ),
            ],
            options={
                "verbose_name": "Organism synonym",
                "db_table": "ORG_SYN",
            },
        ),
        migrations.CreateModel(
            name="NutritionalDisadvantage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_nutri_disadvantage",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("explanation", models.CharField(blank=True, max_length=2000)),
                (
                    "yes_no",
                    models.ForeignKey(
                        blank=True,
                        db_column="is_yn",
                        limit_choices_to={"taxonomy__code": "YESNO"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="yes_no_nutritional_disadvantages",
                        to="taxonomies.taxonomynode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Nutritional Disadvantage",
                "db_table": "NUTRITIONAL_DISADVANTAGE",
            },
        ),
        migrations.CreateModel(
            name="NovelFoodSyn",
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
                ("novel_food_synonym", models.CharField(max_length=255)),
                (
                    "novel_food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.novelfood",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.synonymtype",
                    ),
                ),
            ],
            options={
                "verbose_name": "Novel food synonym",
                "db_table": "STUDY_SYN",
            },
        ),
        migrations.CreateModel(
            name="NovelFoodOrganism",
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
                    "is_gmo",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"taxonomy__code": "YESNO"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="is_gmo_novel_foods",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "novel_food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.novelfood",
                    ),
                ),
                (
                    "org_part",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"taxonomy__code": "MTX"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="org_part_novel_foods",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "organism",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.organism",
                    ),
                ),
                (
                    "variant",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"taxonomy__code": "STRAIN"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="variant_novel_foods",
                        to="taxonomies.taxonomynode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Organism Identity of Novel food",
                "db_table": "STUDY_ORG",
            },
        ),
        migrations.CreateModel(
            name="NovelFoodChemical",
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
                    "chemical",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.chemical",
                    ),
                ),
                (
                    "novel_food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.novelfood",
                    ),
                ),
            ],
            options={
                "verbose_name": "Chemical identity of Novel food",
                "db_table": "STUDY_COM",
            },
        ),
        migrations.CreateModel(
            name="NovelFoodCategory",
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.category",
                    ),
                ),
                (
                    "novel_food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.novelfood",
                    ),
                ),
            ],
            options={
                "verbose_name": "Novel Food Category",
                "verbose_name_plural": "Novel Food Categories",
                "db_table": "STUDY_SUB_TYPE",
            },
        ),
        migrations.AddField(
            model_name="novelfood",
            name="nutritional_disadvantage",
            field=models.OneToOneField(
                blank=True,
                db_column="id_nutri_disadvantage",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="nutritional_disadvantage_novel_foods",
                to="novel_food.nutritionaldisadvantage",
            ),
        ),
        migrations.AddField(
            model_name="novelfood",
            name="opinion",
            field=models.ForeignKey(
                db_column="id_op",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="opinion_novel_foods",
                to="administrative.opinion",
            ),
        ),
        migrations.AddField(
            model_name="novelfood",
            name="outcome",
            field=models.ForeignKey(
                blank=True,
                db_column="id_outcome",
                limit_choices_to={"taxonomy__code": "POSNEG"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="outcome_novel_foods",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AddField(
            model_name="novelfood",
            name="protein_digestibility",
            field=models.ForeignKey(
                blank=True,
                db_column="id_protein_digestibility",
                limit_choices_to={"taxonomy__code": "YESNO"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="protein_digestibility_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="Protein digestibility",
            ),
        ),
        migrations.AddField(
            model_name="novelfood",
            name="shelflife_unit",
            field=models.ForeignKey(
                blank=True,
                db_column="id_shelflife_unit",
                help_text="UNIT Catalogue",
                limit_choices_to={"taxonomy__code": "UNIT"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="shelflife_unit_novel_foods",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AddField(
            model_name="novelfood",
            name="sufficient_data",
            field=models.ForeignKey(
                blank=True,
                db_column="id_is_sufficient_data",
                help_text="Were sufficient data provided?",
                limit_choices_to={"taxonomy__code": "YESNO"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sufficient_data_novel_foods",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AddField(
            model_name="novelfood",
            name="tox_study_required",
            field=models.ForeignKey(
                blank=True,
                db_column="id_tox_study_required",
                limit_choices_to={"taxonomy__code": "YESNO"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="tox_study_required_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="Tox study required",
            ),
        ),
        migrations.CreateModel(
            name="HBGV",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_hbgv", primary_key=True, serialize=False
                    ),
                ),
                (
                    "exceeded_for_population",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_age",
                        help_text="Population for which the HBGV is exceeded",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="population_hbgvs",
                        to="taxonomies.population",
                    ),
                ),
                (
                    "novel_food",
                    models.ForeignKey(
                        db_column="id_study",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="novel_food_hbgvs",
                        to="novel_food.novelfood",
                    ),
                ),
                (
                    "substance",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_substance",
                        limit_choices_to={"taxonomy__code": "PARAM"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="substance_hbgvs",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_type",
                        limit_choices_to={"taxonomy__code": "ENDPOINT_HGV"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="type_hbgvs",
                        to="taxonomies.taxonomynode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Health-Based Guidence Value",
                "verbose_name_plural": "Health-Based Guidence Values",
            },
        ),
        migrations.CreateModel(
            name="ChemicalSyn",
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
                ("synonym", models.CharField(max_length=255)),
                (
                    "chemical",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.chemical",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.synonymtype",
                    ),
                ),
            ],
            options={
                "verbose_name": "Chemical synonym",
                "db_table": "COM_SYN",
            },
        ),
        migrations.AddField(
            model_name="chemical",
            name="chemical_type",
            field=models.ForeignKey(
                blank=True,
                db_column="component_type",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="novel_food.chemicaltype",
            ),
        ),
        migrations.AddField(
            model_name="chemical",
            name="structure_reported",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="novel_food.structurereported",
            ),
        ),
        migrations.CreateModel(
            name="BackgroundExposureAssessment",
            fields=[
                (
                    "id_background_exposure_assessment",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("component_of_interest", models.CharField(blank=True, max_length=255)),
                (
                    "novel_food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.novelfood",
                    ),
                ),
            ],
            options={
                "verbose_name": "Background exposure assessment",
                "db_table": "BG_EXPO_ASSESSMENT",
            },
        ),
        migrations.AddField(
            model_name="allergenicitynovelfood",
            name="novel_food",
            field=models.ForeignKey(
                db_column="id_study",
                on_delete=django.db.models.deletion.CASCADE,
                to="novel_food.novelfood",
                verbose_name="Novel Food",
            ),
        ),
    ]