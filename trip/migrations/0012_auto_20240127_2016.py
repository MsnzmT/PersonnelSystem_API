# Generated by Django 3.0.5 on 2024-01-27 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0011_auto_20240127_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]