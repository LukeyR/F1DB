# Generated by Django 4.1.7 on 2023-03-19 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("personnel", "0007_teammember_unique employee"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="teammember",
            name="Unique employee",
        ),
        migrations.AlterField(
            model_name="teammember",
            name="person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="personnel.person",
                unique=True,
            ),
        ),
    ]
