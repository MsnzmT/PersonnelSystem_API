# Generated by Django 5.0 on 2024-01-28 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_is_employee'),
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='conversation',
            unique_together={('user1', 'user2')},
        ),
    ]
