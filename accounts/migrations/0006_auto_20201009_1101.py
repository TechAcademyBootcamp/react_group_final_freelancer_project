# Generated by Django 3.1 on 2020-10-09 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_email_auth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='title',
            new_name='skill_type',
        ),
    ]
