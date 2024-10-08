# Generated by Django 4.2.14 on 2024-08-19 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "taxonomies",
            "0006_taxonomynode_is_gender_taxonomynode_is_part_nature_and_more",
        ),
        (
            "novel_food",
            "0010_alter_backgroundexposureassessment_comp_of_interest_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="novelfoodorganism",
            name="has_qps",
            field=models.ForeignKey(
                blank=True,
                db_column="id_has_qps",
                help_text="Has qualified presumption of safety? applies only if the organism is a "
                "microorganism. (YESNO vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "YESNO"),
                    models.Q(("short_name", "root"), _negated=True),
                    ("is_yesno", True),
                ),
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="has_qps_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="has QPS",
            ),
        ),
    ]
