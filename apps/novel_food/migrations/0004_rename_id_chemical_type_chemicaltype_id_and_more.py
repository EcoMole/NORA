# Generated by Django 4.2.13 on 2024-06-12 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("novel_food", "0003_alter_chemicaltype_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="chemicaltype",
            old_name="id_chemical_type",
            new_name="id",
        ),
        migrations.AlterField(
            model_name="structurereported",
            name="id_structure_reported",
            field=models.AutoField(
                db_column="id_structure_reported", primary_key=True, serialize=False
            ),
        ),
        migrations.RenameField(
            model_name="structurereported",
            old_name="id_structure_reported",
            new_name="id",
        ),
        migrations.AlterField(
            model_name="chemical",
            name="chemical_type",
            field=models.ForeignKey(
                blank=True,
                db_column="component_type",
                help_text="The majority of the chemical types are extracted from "
                "the OECD picklist (OECD 2012). More on the purpose of "
                "this field: 2013:EN-458 page:20",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="novel_food.chemicaltype",
            ),
        ),
        migrations.AlterField(
            model_name="chemical",
            name="structure_reported",
            field=models.ForeignKey(
                blank=True,
                help_text="This field is used to indicate what type of structure (either SMILES or "
                "InChI) is reported. For example: the structure of "
                "the compound itself, the structure of the monomer if the compound is "
                "a polymer, the structure of an isomer, or no structure at all.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="novel_food.structurereported",
            ),
        ),
        migrations.AlterField(
            model_name="chemicaltype",
            name="definition",
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="structurereported",
            name="definition",
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
