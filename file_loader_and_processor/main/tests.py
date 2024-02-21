from django.urls import include, path, reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from .models import File


class FileTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_file = File.objects.create(
            file='test_me.txt'
        )

    def test_file_processed_field_after_creation(self):
        file = File.objects.get(id=1)
        processed = f'{file.processed}'

        self.assertEqual(processed, 'False')

class FileURLTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/v1/', include('main.urls')),
    ]

    @classmethod
    def setUpTestData(cls):
        test_file = File.objects.create(
            file='test_me.txt'
        )

    def test_list_one_file(self):
        url = reverse('files')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_two_files(self):
        url = reverse('files')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(len(response.data), 2)
