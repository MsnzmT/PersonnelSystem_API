# Generated by Django 3.0.5 on 2024-01-27 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0007_auto_20240127_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='trip_created',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
