# Generated by Django 4.2.14 on 2024-09-01 14:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "taxonomies",
            "0006_taxonomynode_is_gender_taxonomynode_is_part_nature_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="taxonomynode",
            name="short_name",
            field=models.CharField(
                blank=True,
                help_text="if Organism: use SPECIES name + '(as animal)' or '(as plant)' or "
                "'(as organism)'",
                max_length=255,
                null=True,
            ),
        ),
    ]
