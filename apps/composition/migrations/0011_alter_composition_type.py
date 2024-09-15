# Generated by Django 4.2.14 on 2024-09-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("composition", "0010_alter_proposeduse_use_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="composition",
            name="type",
            field=models.CharField(
                choices=[
                    ("specification", "Specification"),
                    ("characterisation", "Characterisation"),
                    ("other", "Other"),
                ],
                help_text="Specification/Characterization/Other",
                max_length=255,
            ),
        ),
    ]
