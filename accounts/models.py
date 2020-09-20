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

    image=models.ImageField(upload_to='user/', null=True, blank=True)
    email=models.EmailField('Email',unique=True,max_length=255)
    active=models.BooleanField('Active', default=False)    
    hourly_prize=models.IntegerField('Hourly Prize',validators=[MaxValueValidator(100)],null=True, blank=True)
    
    REQUIRED_FIELDS = ['username', 'password']
    USERNAME_FIELD='email'



