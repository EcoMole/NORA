# Generated by Django 4.2.14 on 2024-09-04 14:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_alter_contribution_opinion"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contribution",
            options={
                "verbose_name": "Contribution",
                "verbose_name_plural": "📂 Contributions",
            },
        ),
    ]