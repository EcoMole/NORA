# Generated by Django 4.2.13 on 2024-07-27 13:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "administrative",
            "0004_alter_mandate_question_alter_opinionpanel_opinion_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="opinion",
            name="pdf",
        ),
    ]
