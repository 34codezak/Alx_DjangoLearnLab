from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from api.models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Test Book', publication_year=2023, author=self.author)
        self.list_url = reverse('book-list') # Use reverse() for better URL handling

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})  # Use reverse() for better URL handling
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())  # Ensure the book is deleted

    def test_unauthenticated_access(self):
        self.client.logout()
        response = self.client.post(self.list_url, {'title': 'New Book', 'publication_year': 2024, 'author': self.author.id})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
