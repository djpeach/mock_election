# Generated by Django 4.1.3 on 2022-11-14 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elections", "0003_candidate_bio"),
    ]

    operations = [
        migrations.AddField(
            model_name="election",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
