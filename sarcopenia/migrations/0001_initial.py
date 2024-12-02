# Generated by Django 4.2.7 on 2024-04-20 20:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
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
                ("age", models.PositiveIntegerField()),
                ("weight", models.FloatField()),
                ("height", models.FloatField()),
                ("hip", models.FloatField()),
                (
                    "smoking",
                    models.CharField(choices=[(0, "No"), (1, "Yes")], max_length=10),
                ),
                ("smoking_packet_per_year", models.IntegerField()),
                (
                    "alcohol",
                    models.CharField(
                        choices=[(0, "None"), (1, "Social"), (2, "Regular")],
                        max_length=15,
                    ),
                ),
                (
                    "education",
                    models.CharField(
                        choices=[
                            (0, "None"),
                            (1, "Primary School"),
                            (2, "Secondary School"),
                            (3, "University"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "occupation",
                    models.CharField(
                        choices=[
                            (0, "None"),
                            (1, "Police Officer"),
                            (2, "Teacher"),
                            (3, "Farmer"),
                            (4, "Soldier"),
                            (5, "Painter"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "working_Status",
                    models.CharField(
                        choices=[(0, "Retired"), (1, "Working"), (2, "Not Working")],
                        max_length=25,
                    ),
                ),
                (
                    "exercise",
                    models.CharField(
                        choices=[
                            (0, "None"),
                            (1, "1 - 2 Per Week"),
                            (2, "3 - 4 Per Week"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[(0, "Female"), (1, "Male")], max_length=10
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
    ]
