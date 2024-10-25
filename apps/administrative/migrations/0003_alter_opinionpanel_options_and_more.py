# Generated by Django 4.2.13 on 2024-07-05 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "administrative",
            "0002_alter_opinionpanel_id_alter_opinionquestion_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="opinionpanel",
            options={
                "verbose_name": "EFSA Panel",
                "verbose_name_plural": "📂 EFSA Panels",
            },
        ),
        migrations.AlterModelOptions(
            name="opinionquestion",
            options={"verbose_name": "Question", "verbose_name_plural": "📂 Questions"},
        ),
        migrations.AlterModelOptions(
            name="opinionsciofficer",
            options={
                "verbose_name": "Scientific Officer",
                "verbose_name_plural": "📂 Scientific Officers",
            },
        ),
        migrations.AlterModelOptions(
            name="panel",
            options={
                "verbose_name": "EFSA Panel",
                "verbose_name_plural": "📂 EFSA Panels",
            },
        ),
        migrations.AlterField(
            model_name="opinionpanel",
            name="panel",
            field=models.ForeignKey(
                db_column="id_panel",
                on_delete=django.db.models.deletion.CASCADE,
                to="administrative.panel",
                verbose_name="EFSA Panel",
            ),
        ),
        migrations.AlterField(
            model_name="opinionquestion",
            name="question",
            field=models.ForeignKey(
                db_column="id_question",
                on_delete=django.db.models.deletion.CASCADE,
                to="administrative.question",
                verbose_name="Question Number",
            ),
        ),
        migrations.AlterField(
            model_name="opinionsciofficer",
            name="sci_officer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="administrative.scientificofficer",
                verbose_name="Scientific Officer",
            ),
        ),
    ]
