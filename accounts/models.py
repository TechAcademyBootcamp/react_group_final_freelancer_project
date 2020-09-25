from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

# Create your models here.
class Skill(models.Model):
    title=models.CharField('Skill',max_length=50)
    category=models.ForeignKey('self',on_delete=models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class CustomUser(AbstractUser):
    skill=models.ManyToManyField(Skill)

    email=models.EmailField('Email',unique=True,max_length=255)

    title=models.CharField('Title', null=True, blank=True,max_length=255)    
    overview=models.TextField('Overview', null=True, blank=True,max_length=1000)    
    hourly_prize=models.IntegerField('Hourly Prize',validators=[MaxValueValidator(100)],null=True, blank=True)
    image=models.ImageField(upload_to='user/', null=True, blank=True)    
    active=models.BooleanField('Active', default=False)    
    
    
    REQUIRED_FIELDS = ['username', 'password','first_name','last_name']
    USERNAME_FIELD='email'



