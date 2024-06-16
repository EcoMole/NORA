# Generated by Django 4.2.13 on 2024-06-16 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("taxonomies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Applicant",
            fields=[
                ("id_applicant", models.AutoField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(
                        help_text="Name of the applicant", max_length=255, unique=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Applicant",
                "verbose_name_plural": "📂 Applicants",
                "db_table": "APPLICANT",
            },
        ),
        migrations.CreateModel(
            name="Mandate",
            fields=[
                ("id_mandate", models.AutoField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(
                        choices=[
                            ("novel_food", "Novel food"),
                            ("new_dossier", "New dossier"),
                            ("extension_of_use", "Extension of use"),
                            ("nutrient_source", "Nutrient source"),
                            ("traditional_food", "Traditional food"),
                            ("nutrient_source", "Nutrient source"),
                        ],
                        help_text="Title of the mandate type",
                        max_length=255,
                    ),
                ),
                (
                    "mandate_parent",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_mandate_parent",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="mandates",
                        to="administrative.mandate",
                    ),
                ),
            ],
            options={
                "verbose_name": "Mandate",
                "verbose_name_plural": "📂 Mandates",
                "db_table": "MANDATE",
            },
        ),
        migrations.CreateModel(
            name="Opinion",
            fields=[
                ("id_op", models.AutoField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(
                        help_text="Title of the opinion", max_length=255, unique=True
                    ),
                ),
                (
                    "doi",
                    models.CharField(
                        blank=True,
                        help_text="Digital Object Identifier",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        blank=True, help_text="URL to the opinion", null=True
                    ),
                ),
                (
                    "publication_date",
                    models.DateField(
                        blank=True, help_text="Date of publication", null=True
                    ),
                ),
                (
                    "adoption_date",
                    models.DateField(
                        blank=True, help_text="Date of adoption", null=True
                    ),
                ),
                ("pdf", models.FileField(blank=True, null=True, upload_to="pdfs/")),
                (
                    "id_op_type",
                    models.ForeignKey(
                        blank=True,
                        help_text="(REF_TYPE vocab)",
                        limit_choices_to={"taxonomy__code": "REF_TYPE"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="opinions",
                        to="taxonomies.taxonomynode",
                        verbose_name="Document type",
                    ),
                ),
            ],
            options={
                "verbose_name": "Opinion 📄",
                "verbose_name_plural": "Opinions 📄",
                "db_table": "OPINION",
            },
        ),
        migrations.CreateModel(
            name="Panel",
            fields=[
                ("id_panel", models.AutoField(primary_key=True, serialize=False)),
                (
                    "panel",
                    models.CharField(
                        help_text="Title of the panel", max_length=255, unique=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Panel",
                "verbose_name_plural": "📂 Panels",
                "db_table": "PANEL",
            },
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id_question", models.AutoField(primary_key=True, serialize=False)),
                (
                    "question",
                    models.CharField(
                        help_text="Question number", max_length=255, unique=True
                    ),
                ),
                (
                    "applicant",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_applicant",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="applicant_questions",
                        to="administrative.applicant",
                    ),
                ),
                (
                    "mandate",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_mandate",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="questions",
                        to="administrative.mandate",
                    ),
                ),
            ],
            options={
                "verbose_name": "Question",
                "verbose_name_plural": "📂 Questions",
                "db_table": "QUESTION",
            },
        ),
        migrations.CreateModel(
            name="ScientificOfficer",
            fields=[
                ("id_sci_officer", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=255)),
                (
                    "middle_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("last_name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Scientific Officer",
                "verbose_name_plural": "📂 Scientific Officers",
                "db_table": "SCI_OFFICER",
            },
        ),
        migrations.CreateModel(
            name="QuestionMandate",
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
                    "mandate",
                    models.ForeignKey(
                        db_column="id_mandate",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.mandate",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        db_column="id_question",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.question",
                    ),
                ),
                (
                    "regulation",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_regulation",
                        help_text="(LEGREF vocab)",
                        limit_choices_to={"taxonomy__code": "LEGREF"},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="regulation_questionmandates",
                        to="taxonomies.taxonomynode",
                    ),
                ),
            ],
            options={
                "verbose_name": "Question Mandate Regulation",
                "verbose_name_plural": "📂 Question Mandate Regulation",
                "db_table": "QUESTION_MANDATE",
            },
        ),
        migrations.CreateModel(
            name="OPScientificOfficer",
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
                    "id_op",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.opinion",
                    ),
                ),
                (
                    "id_sci_officer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.scientificofficer",
                    ),
                ),
            ],
            options={
                "db_table": "OP_SCI_OFFICER",
            },
        ),
        migrations.CreateModel(
            name="OPQuestion",
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
                    "id_op",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.opinion",
                    ),
                ),
                (
                    "id_question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.question",
                    ),
                ),
            ],
            options={
                "db_table": "OP_QUESTION",
            },
        ),
        migrations.CreateModel(
            name="OPAuthor",
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
                    "id_op",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.opinion",
                    ),
                ),
                (
                    "id_panel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.panel",
                    ),
                ),
            ],
            options={
                "db_table": "OP_AUTHOR",
            },
        ),
    ]
