from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for authentication testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.book = Book.objects.create(title='The Great Gatsby', author=self.user, publication_year=1925)
        
    def test_list_books(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_retrieve_book(self):
        response = self.client.get(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_book(self):
        data = {
            'title': 'The Catcher in the Rye',
            'author': self.user.id,
            'publication_year': 1951
        }
        response = self.client.post('/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_update_book(self):
        data = {
            'title': 'The Catcher in the Rye',
            'author': self.user.id,
            'publication_year': 1951
        }
        response = self.client.put(f'/books/{self.book.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_book(self):
        response = self.client.delete(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        return response.data