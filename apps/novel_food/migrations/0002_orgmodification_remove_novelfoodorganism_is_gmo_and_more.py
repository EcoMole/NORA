# Generated by Django 4.2.13 on 2024-06-12 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("novel_food", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrgModification",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="id_org_modification",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_column="org_modification", max_length=255, unique=True
                    ),
                ),
                (
                    "description",
                    models.CharField(blank=True, max_length=2000, null=True),
                ),
            ],
            options={
                "verbose_name": "Organism Modification",
                "verbose_name_plural": "📂 Organism Modifications",
                "db_table": "ORG_MODIFICATION",
            },
        ),
        migrations.RemoveField(
            model_name="novelfoodorganism",
            name="is_gmo",
        ),
        migrations.AddField(
            model_name="novelfoodorganism",
            name="modification",
            field=models.ForeignKey(
                blank=True,
                help_text="if modified choose how: genitically, hormonally, etc.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="modification_novel_foods",
                to="novel_food.orgmodification",
                verbose_name="modification",
            ),
        ),
    ]