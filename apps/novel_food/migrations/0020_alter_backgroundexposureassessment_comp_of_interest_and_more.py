# Generated by Django 4.2.14 on 2024-11-13 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxonomies", "0009_alter_population_qualifier_alter_population_unit"),
        ("novel_food", "0019_alter_allergenicitynovelfood_allergenicity_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="backgroundexposureassessment",
            name="comp_of_interest",
            field=models.ForeignKey(
                blank=True,
                db_column="id_comp_of_interest",
                help_text="Compound of interest (PARAM vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "PARAM"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="comp_of_interest_bg_expo_assessments",
                to="taxonomies.taxonomynode",
                verbose_name="Compound Assessed For Background Exposure",
            ),
        ),
        migrations.AlterField(
            model_name="chemical",
            name="vocab_id",
            field=models.ForeignKey(
                db_column="id_rnc_efsa",
                help_text="(PARAM vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "PARAM"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="vocab_id_chemicals",
                to="taxonomies.taxonomynode",
                verbose_name="Chemical vocabulary identification",
            ),
        ),
        migrations.AlterField(
            model_name="hbgv",
            name="exceeded",
            field=models.ForeignKey(
                blank=True,
                db_column="id_exceeded",
                help_text="(YESNO vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "YESNO"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_yesno", True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="exceeded_hbgvs",
                to="taxonomies.taxonomynode",
                verbose_name="Exceedance",
            ),
        ),
        migrations.AlterField(
            model_name="hbgv",
            name="substance",
            field=models.ForeignKey(
                blank=True,
                db_column="id_substance",
                help_text="(PARAM vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "PARAM"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="substance_hbgvs",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="hbgv",
            name="type",
            field=models.ForeignKey(
                blank=True,
                db_column="id_type",
                help_text="(ENDPOINT_HGV vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "ENDPOINT_HGV"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="type_hbgvs",
                to="taxonomies.taxonomynode",
                verbose_name="Health-Based Guidance Value",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="antinutritional_factors",
            field=models.ForeignKey(
                blank=True,
                db_column="id_antinutritional_factors",
                help_text="(YESNO vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "YESNO"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_yesno", True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="antinutritional_factors_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="Antinutritional factors",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="endocrine_disrupt_prop",
            field=models.ForeignKey(
                blank=True,
                db_column="id_has_endocrine_disrupt_prop",
                help_text="(YESNO vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "YESNO"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_yesno", True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="endocrine_disrupt_prop_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="Endocrine Disrupting Properties",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="food_matrices",
            field=models.ForeignKey(
                blank=True,
                db_column="id_is_food_matrices",
                help_text="Were food matrices provided? (YESNO vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "YESNO"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_yesno", True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="food_matrices_novel_foods",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="has_nutri_disadvantage",
            field=models.ForeignKey(
                blank=True,
                db_column="id_has_nutri_disadvantage",
                help_text="(YESNO vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "YESNO"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_yesno", True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="has_nutri_disadvantage_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="Nutritionally Disadvantageous",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="instability_concerns",
            field=models.ForeignKey(
                blank=True,
                db_column="id_instability_concerns",
                help_text="(YESNO vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "YESNO"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_yesno", True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="instability_concerns_novel_foods",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="protein_digestibility",
            field=models.ForeignKey(
                blank=True,
                db_column="id_protein_digestibility",
                help_text="(YESNO vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "YESNO"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_yesno", True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="protein_digestibility_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="Protein digestibility",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="shelflife_unit",
            field=models.ForeignKey(
                blank=True,
                db_column="id_shelflife_unit",
                help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "UNIT"),
                    ("extended_name__in", ["Hour", "Day", "Week", "Month", "Year"]),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="shelflife_unit_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="Shelf Life Unit",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="sufficient_data",
            field=models.ForeignKey(
                blank=True,
                db_column="id_is_sufficient_data",
                help_text="Were sufficient data provided? (YESNO vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "YESNO"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_yesno", True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="sufficient_data_novel_foods",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="novelfood",
            name="vocab_id",
            field=models.ForeignKey(
                blank=True,
                db_column="id_rms_efsa",
                help_text="If missing in vocabulary, move on, do not add into vocab. (PARAM vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "PARAM"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="vocab_id_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="NovelFood Vocabulary Identification",
            ),
        ),
        migrations.AlterField(
            model_name="novelfoodcategory",
            name="regulation",
            field=models.ForeignKey(
                blank=True,
                db_column="id_regulation",
                help_text="(LEGREF vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "LEGREF"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="novelfoodorganism",
            name="cells_modified",
            field=models.ForeignKey(
                blank=True,
                db_column="id_cells_modified",
                help_text="(YESNO vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "YESNO"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_yesno", True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="cells_modified_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="Cells Modified? (Cell Culture)",
            ),
        ),
        migrations.AlterField(
            model_name="novelfoodorganism",
            name="has_qps",
            field=models.ForeignKey(
                blank=True,
                db_column="id_has_qps",
                help_text="Has qualified presumption of safety? applies only if "
                "the organism is a microorganism. (YESNO vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "YESNO"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_yesno", True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="has_qps_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="has QPS",
            ),
        ),
        migrations.AlterField(
            model_name="novelfoodorganism",
            name="is_gmo",
            field=models.ForeignKey(
                blank=True,
                db_column="id_is_gmo",
                help_text="Is the organism genetically modified? (YESNO vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "YESNO"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_yesno", True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="is_gmo_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="is GMO",
            ),
        ),
        migrations.AlterField(
            model_name="novelfoodorganism",
            name="org_part",
            field=models.ForeignKey(
                blank=True,
                db_column="id_org_part",
                help_text="(MTX vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "MTX"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_part_nature", True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="org_part_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="organism part",
            ),
        ),
        migrations.AlterField(
            model_name="organism",
            name="vocab_id",
            field=models.ForeignKey(
                db_column="id_organism",
                help_text="(MTX vocab) - only records with '(as animal)' or "
                "'(as plant)' or '(as organism)' in the name are allowed",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "MTX"),
                    models.Q(
                        ("extended_name__icontains", "(as animal)"),
                        ("extended_name__icontains", "(as organism)"),
                        ("extended_name__icontains", "(as plant)"),
                        ("short_name__icontains", "(as animal)"),
                        ("short_name__icontains", "(as organism)"),
                        ("short_name__icontains", "(as plant)"),
                        _connector="OR",
                    ),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="vocab_id_organisms",
                to="taxonomies.taxonomynode",
                verbose_name="Organism vocabulary identification",
            ),
        ),
        migrations.AlterField(
            model_name="specifictoxicity",
            name="specific_toxicity",
            field=models.ForeignKey(
                db_column="id_toxicity",
                help_text="if novel food has specific toxicity, specify which one. (TOXICITY vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "TOXICITY"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                on_delete=django.db.models.deletion.PROTECT,
                related_name="novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="Specific Toxicity",
            ),
        ),
        migrations.AlterField(
            model_name="substanceofconcernnovelfood",
            name="substance_of_concern",
            field=models.ForeignKey(
                blank=True,
                db_column="id_sub_of_concern",
                help_text="Fill only if there is a substance of concern, if not leave blank. "
                "(PARAM vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "PARAM"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="substance_of_concern_substance_of_concern_novel_foods",
                to="taxonomies.taxonomynode",
            ),
        ),
    ]
