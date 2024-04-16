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



from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from myapi.models import Study

class StudyListCreateAPIViewTests(APITestCase):
    def setUp(self):
        self.url = reverse('study-list-create')
        self.valid_payload = {
            "uploader": {
                "orc_id": "12345",
                "name": "John Doe",
                "email": "john@example.com",
                "organization": "Example Org",
                "nr_uploads": 5
            },
            "study_year": {"study_year": 2022},
            "country": {"name": "Example Country"},
            "category": {"name": "Example Category"},
            "peer_reviewed": True,
            "authors": "Example Author",
            "doi": "example_doi",
            "abstract": "Example Abstract",
            "keywords": "Example Keywords",
            "nr_downloads": "100"
        }

    def test_create_study(self):
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Study.objects.count(), 1)
        study = Study.objects.first()
        self.assertEqual(study.uploader.orc_id, "12345")
        self.assertEqual(study.study_year.study_year, 2022)
        self.assertEqual(study.country.name, "Example Country")
        self.assertEqual(study.category.name, "Example Category")
        self.assertTrue(study.peer_reviewed)
        self.assertEqual(study.authors, "Example Author")
        self.assertEqual(study.doi, "example_doi")
        self.assertEqual(study.abstract, "Example Abstract")
        self.assertEqual(study.keywords, "Example Keywords")
        self.assertEqual(study.nr_downloads, "100")

    def test_invalid_study(self):
        invalid_payload = {}  # Payload with missing required fields
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Study.objects.count(), 0)  # No object should be created

    # Add more tests as needed to cover other scenarios and edge cases
