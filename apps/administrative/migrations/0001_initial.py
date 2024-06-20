# Generated by Django 4.2.13 on 2024-06-20 08:05

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
                (
                    "id",
                    models.AutoField(
                        db_column="id_applicant", primary_key=True, serialize=False
                    ),
                ),
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
            name="MandateType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_mandate_type", primary_key=True, serialize=False
                    ),
                ),
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
                        db_column="mandate_type",
                        help_text="Title of the mandate type",
                        max_length=255,
                    ),
                ),
            ],
            options={
                "verbose_name": "Mandate Type",
                "verbose_name_plural": "📂 Mandate Typess",
                "db_table": "MANDATE_TYPE",
            },
        ),
        migrations.CreateModel(
            name="Opinion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_op", primary_key=True, serialize=False
                    ),
                ),
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
                    "document_type",
                    models.ForeignKey(
                        blank=True,
                        db_column="id_op_type",
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
                (
                    "id",
                    models.AutoField(
                        db_column="id_panel", primary_key=True, serialize=False
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_column="panel",
                        help_text="Title of the panel",
                        max_length=255,
                        unique=True,
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
                (
                    "id",
                    models.AutoField(
                        db_column="id_question", primary_key=True, serialize=False
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        db_column="question",
                        help_text="Question number",
                        max_length=255,
                        unique=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Question",
                "verbose_name_plural": "Questions❔",
                "db_table": "QUESTION",
            },
        ),
        migrations.CreateModel(
            name="ScientificOfficer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_sci_officer", primary_key=True, serialize=False
                    ),
                ),
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
            name="QuestionApplicant",
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
                    "applicant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.applicant",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.question",
                    ),
                ),
            ],
            options={
                "verbose_name": "Question Applicant",
                "verbose_name_plural": "📂 Question Applicants",
                "db_table": "QUESTION_APPLICANT",
            },
        ),
        migrations.CreateModel(
            name="OpinionSciOfficer",
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
                    "opinion",
                    models.ForeignKey(
                        db_column="id_op",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.opinion",
                    ),
                ),
                (
                    "sci_officer",
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
            name="OpinionQuestion",
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
                    "opinion",
                    models.ForeignKey(
                        db_column="id_op",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.opinion",
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
            ],
            options={
                "db_table": "OP_QUESTION",
            },
        ),
        migrations.CreateModel(
            name="OpinionPanel",
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
                    "opinion",
                    models.ForeignKey(
                        db_column="id_op",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.opinion",
                    ),
                ),
                (
                    "panel",
                    models.ForeignKey(
                        db_column="id_panel",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.panel",
                    ),
                ),
            ],
            options={
                "db_table": "OP_AUTHOR",
            },
        ),
        migrations.CreateModel(
            name="Mandate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_mandate", primary_key=True, serialize=False
                    ),
                ),
                (
                    "mandate_type",
                    models.ForeignKey(
                        db_column="id_mandate_type",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrative.mandatetype",
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
                        related_name="regulation_mandates",
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
    ]
