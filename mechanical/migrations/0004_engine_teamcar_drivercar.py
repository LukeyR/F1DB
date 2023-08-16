# Generated by Django 4.1.7 on 2023-03-19 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("personnel", "0011_remove_person_driver_abbreviation_and_more"),
        ("mechanical", "0003_tyrecompound_unique tyre producer-compound"),
    ]

    operations = [
        migrations.CreateModel(
            name="Engine",
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
                    "manufacturer",
                    models.CharField(
                        max_length=30,
                        unique=True,
                        verbose_name="TyreManufacturer",
                    ),
                ),
                ("is_current_producer", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="TeamCar",
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
                    "engine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mechanical.engine",
                    ),
                ),
                (
                    "team",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="personnel.team",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DriverCar",
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
                    "driver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="personnel.driver",
                    ),
                ),
                (
                    "team_car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mechanical.teamcar",
                    ),
                ),
            ],
        ),
    ]
