# Generated by Django 4.2.6 on 2023-10-08 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0010_remove_water_water_quality_water_warning'),
    ]

    operations = [
        migrations.RenameField(
            model_name='water',
            old_name='actvities',
            new_name='activities',
        ),
    ]