from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAuthenticated
from rest_framework.filters import DjangoFilterBackend, SearchFilter, OrderingFilter

#ListView: Retrieve a list of all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author' 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year'] # These are the fields allowed for filtering and ordering
    
#DetailView: Retrieve a single book by its ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
#CreateView: Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
#UpdateView: Update an existing book by its ID
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
#DeleteView: Delete an existing book by its ID
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer