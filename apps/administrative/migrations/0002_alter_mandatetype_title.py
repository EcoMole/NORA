# Generated by Django 4.2.11 on 2024-05-12 18:52

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
                help_text="Title of the mandate type", max_length=255
            ),
        ),
    ]
