# Generated by Django 4.2.14 on 2024-08-19 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "taxonomies",
            "0006_taxonomynode_is_gender_taxonomynode_is_part_nature_and_more",
        ),
        ("studies", "0009_alter_adme_guideline_alter_adme_test_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="endpointstudy",
            name="test_type",
            field=models.ForeignKey(
                blank=True,
                db_column="id_test_type",
                help_text="for ex.: acute oral toxicity (OECD phrase ID 1703), or subchronic "
                "(OECD phrase ID 2399) (TEST_TYPE vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "TEST_TYPE"),
                    models.Q(("short_name", "root"), _negated=True),
                ),
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="test_type_endpointstudies",
                to="taxonomies.taxonomynode",
            ),
        ),
    ]
