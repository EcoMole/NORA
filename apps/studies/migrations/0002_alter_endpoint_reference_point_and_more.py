# Generated by Django 4.2.13 on 2024-06-27 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxonomies", "0002_alter_guidelinequalifier_title"),
        ("studies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="endpoint",
            name="reference_point",
            field=models.ForeignKey(
                blank=True,
                db_column="id_reference_point",
                help_text="(ENDPOINT_HGV vocab)",
                limit_choices_to={"taxonomy__code": "ENDPOINT_HGV"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="endpoint_endpoints",
                to="taxonomies.taxonomynode",
            ),
        ),
        migrations.AlterField(
            model_name="endpointstudy",
            name="test_material",
            field=models.CharField(
                blank=True, db_column="testsubstance", max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="finaloutcome",
            name="uncertainty_factor",
            field=models.IntegerField(blank=True, db_column="safety_factor", null=True),
        ),
        migrations.AlterField(
            model_name="studysource",
            name="title",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AddConstraint(
            model_name="admeinvestigationtype",
            constraint=models.UniqueConstraint(
                fields=("adme", "investigation_type"),
                name="unique_adme_investigation_type",
            ),
        ),
    ]
