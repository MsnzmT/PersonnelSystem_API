# Generated by Django 5.0 on 2024-01-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0005_trip_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='status',
            field=models.CharField(default='Pending', max_length=50, null=True),
        ),
    ]
