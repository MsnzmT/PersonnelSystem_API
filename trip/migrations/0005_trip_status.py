# Generated by Django 5.0 on 2024-01-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0004_trip_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]