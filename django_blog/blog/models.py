from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
# User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'