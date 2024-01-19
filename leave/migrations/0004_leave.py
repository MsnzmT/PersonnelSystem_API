# Generated by Django 5.0 on 2024-01-19 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_is_employee'),
        ('leave', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('reason', models.CharField(choices=[('Sick', 'Sick'), ('Marriage', 'Marriage'), ('Death', 'Death'), ('Childbirth', 'Childbirth'), ('Other', 'Other')], max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]
