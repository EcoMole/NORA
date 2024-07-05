# Generated by Django 4.2.13 on 2024-07-05 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxonomies", "0004_alter_population_upper_range_value_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="population",
            name="subgroup",
            field=models.ForeignKey(
                blank=True,
                db_column="id_subgroup",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="subgroup_populations",
                to="taxonomies.subgroup",
                verbose_name="Target Population",
            ),
        ),
        migrations.AlterField(
            model_name="population",
            name="upper_range_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="only if there is upper range value for age",
                max_digits=10,
                null=True,
                verbose_name="Age Upper Range Value",
            ),
        ),
    ]
