# Generated by Django 4.1.7 on 2023-03-19 14:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("personnel", "0010_alter_teammember_person"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="driver_abbreviation",
        ),
        migrations.RemoveField(
            model_name="person",
            name="driver_number",
        ),
        migrations.RemoveField(
            model_name="person",
            name="is_driver",
        ),
        migrations.RemoveField(
            model_name="person",
            name="secondary_driver_number",
        ),
        migrations.CreateModel(
            name="Driver",
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
                    "driver_abbreviation",
                    models.CharField(max_length=3, unique=True),
                ),
                (
                    "driver_number",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(99),
                        ]
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
                    "driver",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="personnel.person",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="team",
            name="driver1",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="driver1",
                to="personnel.driver",
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="driver2",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="driver2",
                to="personnel.driver",
            ),
        ),
    ]
