# Generated by Django 4.2.13 on 2024-06-29 13:58

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("composition", "0002_alter_parameter_title"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="parameter",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("title"),
                name="unique_title_case_insensitive",
            ),
        ),
    ]
