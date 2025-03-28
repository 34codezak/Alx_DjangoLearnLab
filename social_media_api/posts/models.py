from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    author = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField(max_length=500)
    author = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content