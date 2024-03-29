# Generated by Django 4.1.7 on 2023-03-18 21:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("country_name", models.CharField(max_length=50)),
                ("country_code", models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("is_driver", models.BooleanField()),
                (
                    "driver_abbreviation",
                    models.CharField(blank=True, max_length=3, null=True),
                ),
                (
                    "driver_number",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(99),
                        ],
                    ),
                ),
                (
                    "secondary_driver_number",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(2),
                            django.core.validators.MaxValueValidator(99),
                        ],
                    ),
                ),
                (
                    "nationality",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="personnel.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Team",
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
                ("team_name", models.CharField(max_length=200)),
                (
                    "driver1",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="driver1",
                        to="personnel.person",
                    ),
                ),
                (
                    "driver2",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="driver2",
                        to="personnel.person",
                    ),
                ),
                (
                    "nationality",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="personnel.country",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="team",
            constraint=models.UniqueConstraint(
                fields=("driver1", "driver2"), name="Unique drivers"
            ),
        ),
    ]
