from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(max_length=20)
    profile_photo = models.ImageField()

