# Generated by Django 4.2.13 on 2024-07-04 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("taxonomies", "0003_alter_population_upper_range_value_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="VocabNodeField",
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
                ("title", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Vocab Node Field",
                "verbose_name_plural": "📂 Vocab Node Fields",
            },
        ),
        migrations.CreateModel(
            name="FreqUsedVocabNode",
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
                ("entity", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "field",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="extractor.vocabnodefield",
                    ),
                ),
                (
                    "node",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="code_listings",
                        to="taxonomies.taxonomynode",
                        verbose_name="taxnomy node",
                    ),
                ),
            ],
            options={
                "verbose_name": "Frequently Used Vocab Node",
                "verbose_name_plural": "📂 Frequently Used Vocab Nodes",
            },
        ),
    ]
