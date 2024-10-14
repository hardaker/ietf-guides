# Generated by Django 5.0.2 on 2024-10-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guides", "0018_guide_remote"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guide",
            name="remote",
            field=models.CharField(
                choices=[("YES", "Yes"), ("NO", "No")],
                default="NO",
                max_length=32,
                verbose_name="Will you be attending remotely?",
            ),
        ),
    ]
