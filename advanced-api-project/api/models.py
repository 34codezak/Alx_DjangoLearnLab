from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title