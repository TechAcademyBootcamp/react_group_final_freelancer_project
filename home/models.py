from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


User = get_user_model()
# Create your models here.
LEVEL_TYPES=((1, 'Entry Level'), (2, 'Intermediate'), (3, 'Expert'))
STATUS_TYPES=((1, 'Project is aviable.'), (2, 'Work on it.'), (3, 'Project has been canceled. '), (4, 'Paid. '))
PRICE_TYPES=((1, 'Hourly work'), (2, 'Periodic works'))


class Currency(models.Model):
    currency_type=models.CharField('Currency',default=1,max_length=50)


class Upload(models.Model):
    docfile = models.FileField(upload_to='media/')


class Project(models.Model):
    title= models.CharField(max_length=50, verbose_name='title')
    short_description= models.TextField(help_text='this text show to other users', max_length=1000)
    long_description=models.TextField(blank=True, null=True)  
    price_type=models.CharField('price_type',choices=PRICE_TYPES, default='1', max_length=50)  
    price_min= models.PositiveIntegerField(verbose_name='Minimum Price')  
    price_max = models.PositiveIntegerField(verbose_name='Maximum Price')  
    level = models.CharField('level',choices=LEVEL_TYPES, default='1', max_length=150)  
    admit_time = models.DateTimeField(blank=True, default=datetime.now)  
    status = models.CharField('status',choices=STATUS_TYPES, max_length=250) 
    skills=models.CharField('skills',max_length=50)
    upload_files = models.FileField(upload_to='media/')


    is_published = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
