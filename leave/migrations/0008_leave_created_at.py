# Generated by Django 5.0 on 2024-01-27 19:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0007_alter_leave_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
