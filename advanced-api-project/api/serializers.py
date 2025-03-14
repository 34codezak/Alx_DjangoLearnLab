from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) # This is a nested serializer
    class Meta:
        model = Author
        fields = ['name', 'books']