# Generated by Django 4.2.13 on 2024-07-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("composition", "0002_alter_composition_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="proposeduse",
            name="remarks",
            field=models.TextField(
                blank=True,
                help_text="Can be used for comments on the population.",
                null=True,
            ),
        ),
    ]