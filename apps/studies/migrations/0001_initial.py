# Generated by Django 4.2.13 on 2024-06-26 07:17

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
            name="ADME",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_pktkade", primary_key=True, serialize=False
                    ),
                ),
                (
                    "test_material",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "remarks",
                    models.TextField(blank=True, db_column="study_comment", null=True),
                ),
                (
                    "guideline",
                    models.ForeignKey(
                        blank=True,
                        help_text="(STUDYGUIDELINE vocab)",
                        limit_choices_to={"taxonomy__code": "STUDYGUIDELINE"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="guideline_admes",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "guideline_qualifier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="guideline_qualifier_admes",
                        to="taxonomies.guidelinequalifier",
                    ),
                ),
                (
                    "novel_food",
                    models.ForeignKey(
                        db_column="pktkade_study",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.novelfood",
                    ),
                ),
            ],
            options={
                "verbose_name": "ADME Study 🔬♻️",
                "verbose_name_plural": "ADME Studies 🔬♻️",
                "db_table": "PKTK",
            },
        ),
        migrations.CreateModel(
            name="Endpoint",
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
                ("lovalue", models.FloatField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Endpoint",
                "verbose_name_plural": "📂 Endpoints",
                "db_table": "ENDPOINT",
            },
        ),
        migrations.CreateModel(
            name="FinalOutcome",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_hazard", primary_key=True, serialize=False
                    ),
                ),
                (
                    "value",
                    models.FloatField(blank=True, db_column="risk_value", null=True),
                ),
                (
                    "uncertainty_factor",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="uncertainty factor"
                    ),
                ),
                ("remarks", models.TextField(blank=True, null=True)),
                (
                    "endpoint",
                    models.ForeignKey(
                        db_column="id_endpoint",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="studies.endpoint",
                    ),
                ),
                (
                    "outcome",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_assessment_type",
                        help_text="(ENDPOINT_HGV vocab)",
                        limit_choices_to={"taxonomy__code": "ENDPOINT_HGV"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="outcome_final_outcomes",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "qualifier",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_risk_qualifier",
                        help_text="(QUALIFIER vocab)",
                        limit_choices_to={"taxonomy__code": "QUALIFIER"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="qualifier_final_outcomes",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_risk_unit",
                        help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
                        limit_choices_to={"taxonomy__code": "UNIT"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="unit_final_outcomes",
                        to="taxonomies.taxonomynode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Final Outcome 🎰",
                "verbose_name_plural": "Final Outcomes 🎰",
                "db_table": "HAZARD",
            },
        ),
        migrations.CreateModel(
            name="InvestigationType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_investigation_type",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name": "ADME Investigation Type",
                "verbose_name_plural": "ADME Investigation Types",
                "db_table": "INVESTIGATION_TYPE",
            },
        ),
        migrations.CreateModel(
            name="StudySource",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_study_source", primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "Study Sources",
                "db_table": "STUDY_SOURCE",
            },
        ),
        migrations.CreateModel(
            name="Genotox",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_tox", primary_key=True, serialize=False
                    ),
                ),
                (
                    "test_material",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("remarks", models.TextField(blank=True, null=True)),
                (
                    "guideline",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_genotox_guideline",
                        help_text="(STUDYGUIDELINE vocab)",
                        limit_choices_to={"taxonomy__code": "STUDYGUIDELINE"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="guideline_genotoxes",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "guideline_qualifier",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_guideline_qualifier",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="guideline_qualifier_genotoxes",
                        to="taxonomies.guidelinequalifier",
                    ),
                ),
                (
                    "novel_food",
                    models.ForeignKey(
                        db_column="id_study",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.novelfood",
                    ),
                ),
                (
                    "outcome",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_is_genotoxic",
                        help_text="(POSNEG vocab)",
                        limit_choices_to={"taxonomy__code": "POSNEG"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="outcome_genotoxes",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "study_source",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_study_source",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="study_source_genotoxes",
                        to="studies.studysource",
                    ),
                ),
                (
                    "test_type",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_test_type",
                        help_text="for ex.: acute oral toxicity (OECD phrase ID 1703), "
                        "or subchronic (OECD phrase ID 2399). (TEST_TYPE vocab)",
                        limit_choices_to={"taxonomy__code": "TEST_TYPE"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="test_type_genotoxes",
                        to="taxonomies.taxonomynode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Genotox Study 🔬🧬",
                "verbose_name_plural": "Genotox Studies 🔬🧬",
                "db_table": "GENOTOX",
            },
        ),
        migrations.CreateModel(
            name="FinalOutcomePopulation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_hazard_age", primary_key=True, serialize=False
                    ),
                ),
                (
                    "final_outcome",
                    models.ForeignKey(
                        db_column="id_hazard",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="studies.finaloutcome",
                    ),
                ),
                (
                    "population",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_age",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="population_outcome_populations",
                        to="taxonomies.population",
                    ),
                ),
            ],
            options={
                "verbose_name": "Final Outcome Population",
                "verbose_name_plural": "Final Outcome Populations",
                "db_table": "HAZARD_AGE",
            },
        ),
        migrations.CreateModel(
            name="Endpointstudy",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_tox", primary_key=True, serialize=False
                    ),
                ),
                (
                    "study_duration",
                    models.FloatField(blank=True, db_column="exp_duration", null=True),
                ),
                ("remarks", models.TextField(blank=True, null=True)),
                (
                    "test_material",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "duration_unit",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_duration_unit",
                        help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
                        limit_choices_to={"taxonomy__code": "UNIT"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="duration_unit_endpointstudies",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "guideline",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_guideline",
                        help_text="(STUDYGUIDELINE vocab)",
                        limit_choices_to={"taxonomy__code": "STUDYGUIDELINE"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="guideline_endpointstudies",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "guideline_qualifier",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_guideline_qualifier",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="guideline_qualifier_endpointstudies",
                        to="taxonomies.guidelinequalifier",
                    ),
                ),
                (
                    "novel_food",
                    models.ForeignKey(
                        db_column="id_study",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="novel_food.novelfood",
                    ),
                ),
                (
                    "sex",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_sex",
                        help_text="(MTX vocab)",
                        limit_choices_to={"taxonomy__code": "MTX"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="sex_endpointstudies",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "species",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_species",
                        help_text="(MTX vocab)",
                        limit_choices_to={"taxonomy__code": "MTX"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="species_endpointstudies",
                        to="taxonomies.taxonomynode",
                    ),
                ),
                (
                    "study_source",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_study_source",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="study_source_endpointstudies",
                        to="studies.studysource",
                    ),
                ),
                (
                    "test_type",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_test_type",
                        help_text="for ex.: acute oral toxicity (OECD phrase ID 1703), or "
                        "subchronic (OECD phrase ID 2399) (TEST_TYPE vocab)",
                        limit_choices_to={"taxonomy__code": "TEST_TYPE"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="test_type_endpointstudies",
                        to="taxonomies.taxonomynode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Endpoint Study 🔬📐",
                "verbose_name_plural": "Endpoint Studies 🔬📐",
                "db_table": "ENDPOINTSTUDY",
            },
        ),
        migrations.AddField(
            model_name="endpoint",
            name="endpointstudy",
            field=models.ForeignKey(
                db_column="id_tox",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="endpointstudy_endpoints",
                to="studies.endpointstudy",
            ),
        ),
        migrations.AddField(
            model_name="endpoint",
            name="qualifier",
            field=models.ForeignKey(
                blank=True,
                db_column="id_qualifier",
                help_text="(QUALIFIER vocab)",
                limit_choices_to={"taxonomy__code": "QUALIFIER"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="qualifier_endpoints",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AddField(
            model_name="endpoint",
            name="reference_point",
            field=models.ForeignKey(
                blank=True,
                db_column="id_endpoint",
                help_text="(ENDPOINT_HGV vocab)",
                limit_choices_to={"taxonomy__code": "ENDPOINT_HGV"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="endpoint_endpoints",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AddField(
            model_name="endpoint",
            name="subpopulation",
            field=models.ForeignKey(
                blank=True,
                db_column="id_subpopulation",
                help_text="value such as 'male', 'female', 'mothers', 'fetuses', 'offsprings' "
                "are stored here. (MTX vocab)",
                limit_choices_to={"taxonomy__code": "MTX"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="subpopulation_endpoints",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AddField(
            model_name="endpoint",
            name="unit",
            field=models.ForeignKey(
                blank=True,
                db_column="id_unit",
                help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
                limit_choices_to={"taxonomy__code": "UNIT"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="unit_endpoints",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.CreateModel(
            name="ADMEInvestigationType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_pktkade_investigation_type",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "adme",
                    models.ForeignKey(
                        db_column="id_pktkade",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="studies.adme",
                    ),
                ),
                (
                    "investigation_type",
                    models.ForeignKey(
                        db_column="id_investigation_type",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="studies.investigationtype",
                    ),
                ),
            ],
            options={
                "verbose_name": "ADME Investigation Type",
                "verbose_name_plural": "ADME Investigation Types",
                "db_table": "PKTK_INVESTIGATION_TYPE",
            },
        ),
        migrations.AddField(
            model_name="adme",
            name="study_source",
            field=models.ForeignKey(
                blank=True,
                db_column="id_study_source",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="study_source_admes",
                to="studies.studysource",
            ),
        ),
        migrations.AddField(
            model_name="adme",
            name="test_type",
            field=models.ForeignKey(
                blank=True,
                db_column="assay_system_endpoint",
                help_text="for ex.: in silico, in vitro, in vivo, "
                "human study etc. (TEST_TYPE vocab)",
                limit_choices_to={"taxonomy__code": "TEST_TYPE"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="test_type_admes",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AddConstraint(
            model_name="finaloutcomepopulation",
            constraint=models.UniqueConstraint(
                fields=("final_outcome", "population"),
                name="unique_final_outcome_population",
            ),
        ),
    ]
