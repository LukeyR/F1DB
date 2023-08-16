# Generated by Django 4.1.7 on 2023-03-19 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("personnel", "0008_remove_teammember_unique employee_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teammember",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="personnel.team",
            ),
        ),
    ]
