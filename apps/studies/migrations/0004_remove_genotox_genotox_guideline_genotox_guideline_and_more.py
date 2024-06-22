# Generated by Django 4.2.13 on 2024-06-21 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxonomies", "0001_initial"),
        ("studies", "0003_alter_admeinvestigationtype_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="genotox",
            name="genotox_guideline",
        ),
        migrations.AddField(
            model_name="genotox",
            name="guideline",
            field=models.ForeignKey(
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
        migrations.AlterField(
            model_name="adme",
            name="guideline",
            field=models.ForeignKey(
                blank=True,
                help_text="(STUDYGUIDELINE vocab)",
                limit_choices_to={"taxonomy__code": "STUDYGUIDELINE"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="guideline_admes",
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
                limit_choices_to={"taxonomy__code": "STUDYGUIDELINE"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="guideline_endpointstudies",
                to="taxonomies.taxonomynode",
            ),
        ),
    ]
