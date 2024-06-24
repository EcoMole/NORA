# Generated by Django 4.2.13 on 2024-06-23 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxonomies", "0001_initial"),
        ("novel_food", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="novelfoodorganism",
            name="is_cell_culture_modified",
        ),
        migrations.AddField(
            model_name="novelfoodorganism",
            name="are_the_cells_modified",
            field=models.ForeignKey(
                blank=True,
                db_column="id_are_the_cells_modified",
                help_text="Is the cell culture modified? (YESNO vocab)",
                limit_choices_to={"taxonomy__code": "YESNO"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="are_the_cells_modified_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="is the cell culture modified",
            ),
        ),
        migrations.AlterField(
            model_name="chemdescriptor",
            name="value",
            field=models.CharField(
                help_text="contains e.g. the molecular formula itself if type is "
                "'Molecular Formula', etc.",
                max_length=255,
                verbose_name="Descriptor",
            ),
        ),
        migrations.AlterField(
            model_name="novelfoodorganism",
            name="cell_culture",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="novelfoodorganism",
            name="has_qps",
            field=models.ForeignKey(
                blank=True,
                db_column="id_has_qps",
                help_text="Has qualified presumption of safety? applies only if the organism is a "
                "microorganism. (YESNO vocab)",
                limit_choices_to={"taxonomy__code": "YESNO"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="has_qps_novel_foods",
                to="taxonomies.taxonomynode",
                verbose_name="has QPS",
            ),
        ),
        migrations.AlterField(
            model_name="novelfoodorganism",
            name="variant",
            field=models.CharField(
                blank=True,
                help_text="STRAIN if microorganism / VARIETY if plant / SUBSPECIES if animal",
                max_length=255,
                null=True,
            ),
        ),
    ]
