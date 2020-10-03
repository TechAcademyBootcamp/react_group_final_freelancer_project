# Generated by Django 3.1 on 2020-10-01 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201001_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=20, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Title'),
        ),
    ]
