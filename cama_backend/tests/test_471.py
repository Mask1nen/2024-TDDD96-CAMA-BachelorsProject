from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from myapi.models import CamaUser

class CamaUserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.cama_user_data = {
            'orc_id': '123456',
            'name': 'John Doe',
            'email': 'john@example.com',
            'organization': 'Example Org',
            'nr_uploads': 5
        }

    def test_get_cama_users(self):
        response = self.client.get('/api/cama-users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_cama_user(self):
        response = self.client.post('/api/cama-users/', self.cama_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CamaUser.objects.count(), 1)
        self.assertEqual(CamaUser.objects.get().name, 'John Doe')
