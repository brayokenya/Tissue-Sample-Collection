# Generated by Django 4.2 on 2023-12-27 16:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("SampleApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sample",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
