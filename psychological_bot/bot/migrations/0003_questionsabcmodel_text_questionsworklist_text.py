# Generated by Django 4.2.3 on 2023-07-22 16:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bot", "0002_alter_answersabcmodel_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="questionsabcmodel",
            name="text",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="questionsworklist",
            name="text",
            field=models.TextField(null=True),
        ),
    ]
