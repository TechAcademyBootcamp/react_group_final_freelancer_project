# Generated by Django 3.1 on 2020-10-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201009_1108'),
        ('home', '0003_auto_20201009_1108'),
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
