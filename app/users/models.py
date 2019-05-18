from django.db import models
from django.contrib.auth.models import User 


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
