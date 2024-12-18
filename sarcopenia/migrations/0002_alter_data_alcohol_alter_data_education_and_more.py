# Generated by Django 4.2.7 on 2024-04-20 20:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sarcopenia", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="alcohol",
            field=models.CharField(
                choices=[("0", "None"), ("Social", "Social"), ("Regular", "Regular")],
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="data",
            name="education",
            field=models.CharField(
                choices=[
                    ("None", "None"),
                    ("Primary School", "Primary School"),
                    ("Secondary School", "Secondary School"),
                    ("University", "University"),
                ],
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="data",
            name="exercise",
            field=models.CharField(
                choices=[
                    ("None", "None"),
                    ("1-2/week", "1 - 2 Per Week"),
                    ("3-4/week", "3 - 4 Per Week"),
                ],
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="data",
            name="gender",
            field=models.CharField(
                choices=[("F", "Female"), ("M", "Male")], max_length=1
            ),
        ),
        migrations.AlterField(
            model_name="data",
            name="occupation",
            field=models.CharField(
                choices=[
                    ("None", "None"),
                    ("Police Officer", "Police Officer"),
                    ("Teacher", "Teacher"),
                    ("Farmer", "Farmer"),
                    ("Soldier", "Soldier"),
                    ("Painter", "Painter"),
                ],
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="data",
            name="smoking",
            field=models.CharField(
                choices=[("No", "No"), ("Yes", "Yes")], max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="data",
            name="smoking_packet_per_year",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="data",
            name="working_Status",
            field=models.CharField(
                choices=[
                    ("Retired", "Retired"),
                    ("Working", "Working"),
                    ("Not Working", "Not Working"),
                ],
                max_length=25,
            ),
        ),
    ]
