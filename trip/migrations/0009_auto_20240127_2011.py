# Generated by Django 3.0.5 on 2024-01-27 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0008_trip_trip_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_created',
            field=models.TimeField(auto_now=True),
        ),
    ]
