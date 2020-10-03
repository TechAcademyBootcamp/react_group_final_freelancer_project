# Generated by Django 3.1 on 2020-10-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_email_auth'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='skills',
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(related_name='projects', to='accounts.Skill'),
        ),
    ]
