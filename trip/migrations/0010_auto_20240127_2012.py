# Generated by Django 3.0.5 on 2024-01-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0009_auto_20240127_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_created',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
