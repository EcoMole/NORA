# Generated by Django 4.2.13 on 2024-06-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("administrative", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mandatetype",
            name="title",
            field=models.CharField(
                db_column="mandate_type",
                help_text="Title of the mandate type",
                max_length=255,
                unique=True,
            ),
        ),
    ]
