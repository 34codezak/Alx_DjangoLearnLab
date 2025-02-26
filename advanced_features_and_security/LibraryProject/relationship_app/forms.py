from django import forms
from .models import Book  # Ensure you have a Book model in models.py

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'pages', 'cover']
