# Generated by Django 5.0 on 2024-01-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0012_auto_20240127_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]