# Generated by Django 5.0 on 2024-01-19 15:03

import django.db.models.deletion
import user.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leave', '0002_delete_leaveadmin'),
        ('user', '0003_person_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveAdmin',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_leave_admin', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('user.person',),
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
    ]
