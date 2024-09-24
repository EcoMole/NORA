# Generated by Django 4.2.14 on 2024-08-19 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "taxonomies",
            "0006_taxonomynode_is_gender_taxonomynode_is_part_nature_and_more",
        ),
        ("novel_food", "0011_alter_novelfoodorganism_has_qps"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organism",
            name="vocab_id",
            field=models.ForeignKey(
                db_column="id_organism",
                help_text="(MTX vocab)",
                limit_choices_to=models.Q(
                    ("taxonomy__code", "MTX"),
                    models.Q(
                        ("extended_name__icontains", "(as animal)"),
                        ("extended_name__icontains", "(as organism)"),
                        ("extended_name__icontains", "(as plant)"),
                        ("short_name__icontains", "(as animal)"),
                        ("short_name__icontains", "(as organism)"),
                        ("short_name__icontains", "(as plant)"),
                        _connector="OR",
                    ),
                ),
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="vocab_id_organisms",
                to="taxonomies.taxonomynode",
                verbose_name="Organism vocabulary identification",
            ),
        ),
    ]