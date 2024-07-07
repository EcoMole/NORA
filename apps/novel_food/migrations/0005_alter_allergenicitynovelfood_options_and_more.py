# Generated by Django 4.2.13 on 2024-07-05 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxonomies", "0005_alter_population_subgroup_and_more"),
        ("novel_food", "0004_alter_novelfood_shelflife_value"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="allergenicitynovelfood",
            options={
                "verbose_name": "Allergenicity",
                "verbose_name_plural": "Allergenicity",
            },
        ),
        migrations.AlterModelOptions(
            name="backgroundexposureassessment",
            options={
                "verbose_name": "Background exposure assessment",
                "verbose_name_plural": "Background exposure assessment",
            },
        ),
        migrations.RenameField(
            model_name="novelfoodorganism",
            old_name="are_the_cells_modified",
            new_name="cells_modified",
        ),
        migrations.AlterField(
            model_name="backgroundexposureassessment",
            name="comp_of_interest",
            field=models.ForeignKey(
                blank=True,
                db_column="id_comp_of_interest",
                help_text="Compound of interest (PARAM vocab)",
                limit_choices_to={"taxonomy__code": "PARAM"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="comp_of_interest_bg_expo_assessments",
                to="taxonomies.taxonomynode",
                verbose_name="Compound Assessed",
            ),
        ),
        migrations.AlterField(
            model_name="chemicalsyn",
            name="syn_type",
            field=models.ForeignKey(
                db_column="id_syn",
                on_delete=django.db.models.deletion.CASCADE,
                to="novel_food.synonymtype",
                verbose_name="Synonym Type",
            ),
        ),
        migrations.AlterField(
            model_name="hbgv",
            name="exceeded",
            field=models.ForeignKey(
                blank=True,
                db_column="id_exceeded",
                help_text="(YESNO vocab)",
                limit_choices_to={"taxonomy__code": "YESNO"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="exceeded_hbgvs",
                to="taxonomies.taxonomynode",
                verbose_name="Exceedance",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="endocrine_disrupt_prop",
            field=models.ForeignKey(
                blank=True,
                db_column="id_has_endocrine_disrupt_prop",
                help_text="(YESNO vocab)",
                limit_choices_to={"taxonomy__code": "YESNO"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="endocrine_disrupt_prop_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="Endocrine Disrupting Properties",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="genotox_final_outcome",
            field=models.ForeignKey(
                blank=True,
                db_column="id_is_genotoxic",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="genotox_final_outcome_novel_foods",
                to="novel_food.genotoxfinaloutcome",
                verbose_name="Genotoxicity Final Outcome",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="has_nutri_disadvantage",
            field=models.ForeignKey(
                blank=True,
                db_column="id_has_nutri_disadvantage",
                help_text="(YESNO vocab)",
                limit_choices_to={"taxonomy__code": "YESNO"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="has_nutri_disadvantage_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="Nutritionally Disadvantageous",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="nutri_disadvantage_explanation",
            field=models.TextField(
                blank=True,
                help_text="explanation in case the Novel Food has a nutritional disadvantage",
                null=True,
                verbose_name="Reason For Disadvantage",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="outcome",
            field=models.CharField(
                blank=True,
                choices=[
                    ("negative", "Negative"),
                    ("partially_negative", "Partially Negative"),
                    ("positive", "Positive"),
                ],
                max_length=255,
                null=True,
                verbose_name="Opinion Outcome",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="shelflife_unit",
            field=models.ForeignKey(
                blank=True,
                db_column="id_shelflife_unit",
                help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
                limit_choices_to={"taxonomy__code": "UNIT"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="shelflife_unit_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="Shelf Life Unit",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="shelflife_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=10,
                null=True,
                verbose_name="Shelf Life Value",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="tox_study_required",
            field=models.CharField(
                blank=True,
                choices=[
                    ("yes", "Yes"),
                    ("no", "No"),
                    ("no_new_data_added", "No new data added"),
                ],
                max_length=255,
                null=True,
                verbose_name="Toxicology Required",
            ),
        ),
        migrations.AlterField(
            model_name="novelfoodorganism",
            name="cell_culture",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Cell Type (Cell Culture)",
            ),
        ),
        migrations.AlterField(
            model_name="novelfoodsyn",
            name="syn_type",
            field=models.ForeignKey(
                db_column="id_syn",
                on_delete=django.db.models.deletion.CASCADE,
                to="novel_food.synonymtype",
                verbose_name="Synonym Type",
            ),
        ),
        migrations.AlterField(
            model_name="organismsyn",
            name="syn_type",
            field=models.ForeignKey(
                db_column="id_syn",
                on_delete=django.db.models.deletion.CASCADE,
                to="novel_food.synonymtype",
                verbose_name="Synonym Type",
            ),
        ),
    ]