# Generated by Django 4.2.14 on 2024-09-02 13:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("novel_food", "0015_alter_substanceofconcernnovelfood_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="specifictoxicity",
            options={
                "verbose_name": "Hazard - Specific Toxicity",
                "verbose_name_plural": "Hazard - Specific Toxicities",
            },
        ),
        migrations.AlterModelOptions(
            name="substanceofconcernnovelfood",
            options={
                "verbose_name": "Hazard - Substance of concern",
                "verbose_name_plural": "Hazard - Substances of concern",
            },
        ),
    ]
