from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class BookTests(APITestCase):
    def test_create_Book(self):
        """
        Ensure we can create a new Book object.
        """
        url = reverse('ListBooks')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().name, 'DabApps')
