from django.db import models
from accounts.models import CustomUser, Skill
from datetime import datetime


User = CustomUser()
# Create your models here.
LEVEL_TYPES=((1, 'Entry Level'), (2, 'Intermediate'), (3, 'Expert'))
STATUS_TYPES=((1, 'Project is aviable.'), (2, 'Work on it.'), (3, 'Project has been canceled. '), (4, 'Paid. '))
PRICE_TYPES=((1, 'Hourly work'), (2, 'Periodic works'))


class Currency(models.Model):
    currency_type=models.CharField('Currency',max_length=50)
    def __str__(self):
        return self.currency_type

class Upload(models.Model):
    docfile = models.FileField(upload_to='media/')

class Level(models.Model):
    level_type=models.CharField('Level',max_length=50)
    def __str__(self):
        return self.level_type

class Project(models.Model):
    title= models.CharField(max_length=50, verbose_name='title')
    description=models.TextField()  
    price_type=models.IntegerField('price_type',choices=PRICE_TYPES, default=1)  
    price_min= models.PositiveIntegerField(verbose_name='Minimum Price')  
    price_max = models.PositiveIntegerField(verbose_name='Maximum Price')  
 
    admit_time = models.DateTimeField(default=datetime.now)  
    status = models.IntegerField('status',choices=STATUS_TYPES) 
    skills=models.ManyToManyField(Skill,related_name='projects')
    upload_files = models.FileField(upload_to='media/',blank=True, null=True)


    is_published = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    level= models.ForeignKey(Level,on_delete=models.CASCADE,)


class  Replies(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    reply=models.TextField('Reply',max_length=2500)
    duration=models.IntegerField('Duration' )
    price=models.DecimalField('Price',max_digits = 10, decimal_places = 2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Proposals(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.ForeignKey(Project,on_delete=models.CASCADE, related_name='proposals')
    
    created_at=models.DateTimeField(auto_now_add=True)