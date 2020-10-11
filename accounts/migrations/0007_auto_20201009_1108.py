# Generated by Django 3.1 on 2020-10-09 07:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201009_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill_type',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='email_auth',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='hourly_price',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Hourly Prize'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
    ]
