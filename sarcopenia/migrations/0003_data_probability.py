# Generated by Django 4.2.7 on 2024-04-20 20:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sarcopenia", "0002_alter_data_alcohol_alter_data_education_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="data",
            name="probability",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
