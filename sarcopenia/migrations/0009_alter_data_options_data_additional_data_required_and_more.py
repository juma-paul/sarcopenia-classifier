# Generated by Django 5.0.4 on 2024-04-23 14:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sarcopenia", "0008_alter_data_gender"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="data",
            options={},
        ),
        migrations.AddField(
            model_name="data",
            name="additional_data_required",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="data",
            name="additional_model_used",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="message",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name="ModelTwo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "low_contraction_stress",
                    models.CharField(
                        choices=[("0.0", "No"), ("1.0", "Yes")],
                        max_length=15,
                        null=True,
                    ),
                ),
                ("contraction_stress", models.FloatField()),
                ("gait_speed", models.FloatField()),
                (
                    "data",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="model_two_data",
                        to="sarcopenia.data",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ModelThree",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "low_grip_strength",
                    models.CharField(
                        choices=[("0.0", "No"), ("1.0", "Yes")],
                        max_length=15,
                        null=True,
                    ),
                ),
                ("grip_strength", models.FloatField()),
                (
                    "model_two",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="model_three_data",
                        to="sarcopenia.modeltwo",
                    ),
                ),
            ],
        ),
    ]