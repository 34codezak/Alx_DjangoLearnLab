from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return True

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Restrict access to authenticated users only