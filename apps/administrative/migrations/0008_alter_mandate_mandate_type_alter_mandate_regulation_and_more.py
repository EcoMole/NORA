# Generated by Django 4.2.14 on 2024-11-05 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "taxonomies",
            "0008_alter_population_qualifier_alter_population_subgroup_and_more",
        ),
        ("administrative", "0007_alter_question_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mandate",
            name="mandate_type",
            field=models.ForeignKey(
                db_column="id_mandate_type",
                on_delete=django.db.models.deletion.PROTECT,
                to="administrative.mandatetype",
            ),
        ),
        migrations.AlterField(
            model_name="mandate",
            name="regulation",
            field=models.ForeignKey(
                blank=True,
                db_column="id_regulation",
                help_text="(LEGREF vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "LEGREF"),
                    models.Q(("short_name", "root"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="regulation_mandates",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="opinion",
            name="document_type",
            field=models.ForeignKey(
                blank=True,
                db_column="id_op_type",
                help_text="(REF_TYPE vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "REF_TYPE"),
                    models.Q(("short_name", "root"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="opinions",
                to="taxonomies.taxonomynode",
                verbose_name="Document type",
            ),
        ),
        migrations.AlterField(
            model_name="opinionpanel",
            name="panel",
            field=models.ForeignKey(
                db_column="id_panel",
                on_delete=django.db.models.deletion.PROTECT,
                to="administrative.panel",
                verbose_name="EFSA Panel",
            ),
        ),
        migrations.AlterField(
            model_name="opinionquestion",
            name="question",
            field=models.ForeignKey(
                db_column="id_question",
                on_delete=django.db.models.deletion.PROTECT,
                to="administrative.question",
                verbose_name="Question Number",
            ),
        ),
        migrations.AlterField(
            model_name="opinionsciofficer",
            name="sci_officer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="administrative.scientificofficer",
                verbose_name="Scientific Officer",
            ),
        ),
        migrations.AlterField(
            model_name="questionapplicant",
            name="applicant",
            field=models.ForeignKey(
                db_column="id_applicant",
                on_delete=django.db.models.deletion.PROTECT,
                to="administrative.applicant",
            ),
        ),
    ]