# Generated by Django 5.0 on 2024-01-19 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0002_payslip'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
