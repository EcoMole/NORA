# Generated by Django 4.2.14 on 2024-11-13 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxonomies", "0009_alter_population_qualifier_alter_population_unit"),
        (
            "studies",
            "0012_alter_adme_guideline_alter_adme_guideline_qualifier_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="adme",
            name="guideline",
            field=models.ForeignKey(
                blank=True,
                help_text="(STUDYGUIDELINE vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "STUDYGUIDELINE"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="guideline_admes",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="adme",
            name="test_type",
            field=models.ForeignKey(
                blank=True,
                db_column="assay_system_endpoint",
                help_text="for ex.: in silico, in vitro, in vivo, "
                "human study etc. (TEST_TYPE vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "TEST_TYPE"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="test_type_admes",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="endpoint",
            name="qualifier",
            field=models.ForeignKey(
                blank=True,
                db_column="id_qualifier",
                help_text="(QUALIFIER vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "QUALIFIER"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="qualifier_endpoints",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="endpoint",
            name="reference_point",
            field=models.ForeignKey(
                blank=True,
                db_column="id_reference_point",
                help_text="(ENDPOINT_HGV vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "ENDPOINT_HGV"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="endpoint_endpoints",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="endpoint",
            name="subpopulation",
            field=models.ForeignKey(
                blank=True,
                db_column="id_subpopulation",
                help_text="value such as 'male', 'female', 'mothers', 'fetuses', "
                "'offsprings' are stored here. (MTX vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "MTX"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(
                        ("is_gender", True),
                        (
                            "extended_name",
                            "Fetus / stillbirth / neonatus (as part-nature)",
                        ),
                        _connector="OR",
                    ),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="subpopulation_endpoints",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="endpoint",
            name="unit",
            field=models.ForeignKey(
                blank=True,
                db_column="id_unit",
                help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "UNIT"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="unit_endpoints",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="endpointstudy",
            name="duration_unit",
            field=models.ForeignKey(
                blank=True,
                db_column="id_duration_unit",
                help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "UNIT"),
                    ("extended_name__in", ["Hour", "Day", "Week", "Month", "Year"]),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="duration_unit_endpointstudies",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="endpointstudy",
            name="guideline",
            field=models.ForeignKey(
                blank=True,
                db_column="id_guideline",
                help_text="(STUDYGUIDELINE vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "STUDYGUIDELINE"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="guideline_endpointstudies",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="endpointstudy",
            name="sex",
            field=models.ForeignKey(
                blank=True,
                db_column="id_sex",
                help_text="(MTX vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "MTX"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_gender", True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="sex_endpointstudies",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="endpointstudy",
            name="species",
            field=models.ForeignKey(
                blank=True,
                db_column="id_species",
                help_text="(MTX vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "MTX"),
                    models.Q(
                        ("extended_name__icontains", "(as animal)"),
                        ("extended_name__icontains", "(as organism)"),
                        ("short_name__icontains", "(as animal)"),
                        ("short_name__icontains", "(as organism)"),
                        _connector="OR",
                    ),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="species_endpointstudies",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="endpointstudy",
            name="test_type",
            field=models.ForeignKey(
                blank=True,
                db_column="id_test_type",
                help_text="for ex.: acute oral toxicity (OECD phrase ID 1703), "
                "or subchronic (OECD phrase ID 2399) (TEST_TYPE vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "TEST_TYPE"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="test_type_endpointstudies",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="finaloutcome",
            name="outcome",
            field=models.ForeignKey(
                blank=True,
                db_column="id_assessment_type",
                help_text="(ENDPOINT_HGV vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "ENDPOINT_HGV"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="outcome_final_outcomes",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="finaloutcome",
            name="qualifier",
            field=models.ForeignKey(
                blank=True,
                db_column="id_risk_qualifier",
                help_text="(QUALIFIER vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "QUALIFIER"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="qualifier_final_outcomes",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="finaloutcome",
            name="unit",
            field=models.ForeignKey(
                blank=True,
                db_column="id_risk_unit",
                help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "UNIT"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="unit_final_outcomes",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="genotox",
            name="guideline",
            field=models.ForeignKey(
                blank=True,
                db_column="id_genotox_guideline",
                help_text="(STUDYGUIDELINE vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "STUDYGUIDELINE"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="guideline_genotoxes",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="genotox",
            name="outcome",
            field=models.ForeignKey(
                blank=True,
                db_column="id_is_genotoxic",
                help_text="(POSNEG vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "POSNEG"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="outcome_genotoxes",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="genotox",
            name="test_type",
            field=models.ForeignKey(
                blank=True,
                db_column="id_test_type",
                help_text="for ex.: acute oral toxicity (OECD phrase ID 1703), "
                "or subchronic (OECD phrase ID 2399). (TEST_TYPE vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "TEST_TYPE"),
                    models.Q(("short_name", "root"), _negated=True),
                    models.Q(("status", "D"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="test_type_genotoxes",
                to="taxonomies.taxonomynode",
            ),
        ),
    ]
