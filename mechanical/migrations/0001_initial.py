# Generated by Django 4.1.7 on 2023-03-19 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TyreManufacturer",
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
                ("company_name", models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="TyreCompound",
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
                ("compound_name", models.CharField(max_length=25)),
                (
                    "compound_alias",
                    models.CharField(blank=True, max_length=25, null=True),
                ),
                (
                    "producer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mechanical.tyremanufacturer",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="tyrecompound",
            constraint=models.UniqueConstraint(
                fields=("producer", "compound_name"),
                name="Unique tyre producer-compound",
            ),
        ),
    ]
