from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

# Create your models here.
class Skill(models.Model):
    title=models.CharField('Skill',max_length=50)
    category=models.ForeignKey('self',on_delete=models.CASCADE, blank=True, null=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title



class CustomUser(AbstractUser):
    skill=models.ManyToManyField(Skill)

    first_name=models.CharField('First Name', null=False, blank=False,max_length=20)    
    last_name=models.CharField('Last name', null=False, blank=False,max_length=20)    
    email=models.EmailField('Email',unique=True,max_length=100)

    title=models.CharField('Title', null=True, blank=True,max_length=50)    
    overview=models.TextField('Overview', null=True, blank=True,max_length=1000)    
    hourly_price=models.DecimalField('Hourly Prize',null=True, blank=True,decimal_places=2,max_digits=4)
    image=models.ImageField(upload_to='user/', null=True, blank=True)    
    active=models.BooleanField('Active', default=False)    
    email_auth=models.BooleanField('Email Verification', default=False)
    
    REQUIRED_FIELDS = ['first_name','last_name','username', 'password']
    USERNAME_FIELD='email'



