# Generated by Django 4.2.13 on 2024-06-29 14:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("novel_food", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="novelfood",
            name="shelflife_value",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=10, null=True
            ),
        ),
    ]