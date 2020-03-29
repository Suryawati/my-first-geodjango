# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db.models import Model   
from django.contrib.gis.db.models import PointField 
from django.db import models 

class User(Model):
     location = PointField(null=True, spatial_index=True)
     
     class Meta:
     	AbstractUser

class CustomUser(AbstractUser, User):
    
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    