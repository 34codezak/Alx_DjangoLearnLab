from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, date_of_birth, password, **extra_fields)
    
class CustomUserManager(BaseUserManager):
    create_user = models.Model.create_user()
    create_superuser = models.Model.create_superuser()  