# Generated by Django 3.0.5 on 2024-01-27 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_person_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
