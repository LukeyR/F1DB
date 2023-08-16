# Generated by Django 4.1.7 on 2023-03-19 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "personnel",
            "0005_alter_country_options_alter_person_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="teammember",
            name="team",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="personnel.team",
            ),
        ),
    ]