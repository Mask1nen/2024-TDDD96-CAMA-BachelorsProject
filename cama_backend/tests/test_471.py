from rest_framework.test import APITestCase
from django.urls import reverse

from rest_framework import status
from myapi.models import *

import logging
logger = logging.getLogger(__name__)

class TestData:
    import json
    cama_user_data = {
        'orc_id': '0000-0002-1825-0097',
        "name": "John Doe",
        "email": "john.doe@example.com",
        "organization": "Example University",
        "nr_uploads": 5
    }
    cama_user_payload = json.dumps(cama_user_data)

    study_data = {
        "cama_user": {
            'orc_id': '0000-0002-1825-0097',
            "name": "John Doe",
            "email": "john.doe@example.com",
            "organization": "Example University",
            "nr_uploads": 5
        },
        "country": {"name":"United States"},
        "category": {"name": "Health"},
        "study_year": 2024,
        "peer_reviewed": True,
        "authors": "Jane Doe, John Smith",
        "doi": "10.1234/abcd.12345",
        "abstract": "This study investigates the effects of...",
        "keywords": "health, research, study",
        "nr_downloads": "200",
    }
    study_payload = json.dumps(study_data)

    experiment_data = {
        "study": {
            "cama_user": {
                'orc_id': '0000-0002-1825-0097',
                "name": "John Doe",
                "email": "john.doe@example.com",
                "organization": "Example University",
                "nr_uploads": 5
            },
            "country": {"name":"United States"},
            "category": {"name": "Health"},
            "study_year": 2024,
            "peer_reviewed": True,
            "authors": "Jane Doe, John Smith",
            "doi": "10.1234/abcd.12345",
            "abstract": "This study investigates the effects of...",
            "keywords": "health, research, study",
            "nr_downloads": "200",
        },
        "study_design": {
            "design": "Randomized Controlled Trial"
        },
        "risks": {
            "rob": "Low",
            "robins": "Moderate"
        },
        "grade": {
            "grade": "A"
        },
        "participant_design": {
            "design": "Between-Group Design"
        },
        "implemented": {
            "implementor": "Pilot Study"
        },
        "intensity_n": 3,
        "duration_week": 12,
        "frequency_n": 3,
        "ni": 1,
        "intervention": "Example Intervention",
        "intervention_op": "Example Intervention_op",
        "target_population": "Example Target Population",
        "mean_age": 25.5,
        "source": "Example Source"
    }
    experiment_payload = json.dumps(experiment_data)

    effect_data = {
        "experiment": {
            "study_id": {
                "study_id": 1,
                "uploader": {
                    "orc_id": "0000-0002-1825-0097",
                    "name": "John Doe",
                    "email": "john.doe@example.com",
                    "organization": "Example University",
                    "nr_uploads": 5
                },
                "study_year": 2024,
                "country": {
                    "name": "United States"
                },
                "category": {
                    "name": "Health"
                },
                "peer_reviewed": True,
                "authors": "Jane Doe, John Smith",
                "doi": "10.1234/abcd.12345",
                "abstract": "This study investigates the effects of...",
                "keywords": "health, research, study",
                "nr_downloads": "200"
            },
            "study_design": {
                "design": "Randomized Controlled Trial"
            },
            "risks": {
                "rob": "Low",
                "robins": "Moderate"
            },
            "grade": {
                "grade": "A"
            },
            "participant_design": {
                "design": "Between-Group Design"
            },
            "implemented": {
                "implementor": "Pilot Study"
            },
            "intensity_n": 3,
            "duration_week": 12,
            "frequency_n": 3,
            "ni": 1,
            "intervention": "Example Intervention",
            "intervention_op": "Example Intervention_op",
            "target_population": "Example Target Population",
            "mean_age": 25.5,
            "source": "Example Source"
        },
        "sd1i": 1.5,
        "sd2i": 1.8,
        "n1i": 30,
        "n2i": 35,
        "m1i": 15.2,
        "m2i": 16.7,
        "d_var": 0.5,
        "d": 0.45,
        "f_stat": 5.23,
        "t": 2.45,
        "ri": 1,
        "mean_age": 25.3,
        "ni": 65,
        "icc": 0.78,
        "ai": 2,
        "bi": 3,
        "ci": 4,
        "di": 5
    }

class CamaUserAPITest(APITestCase):
    def setUp(self):
        self.url = reverse('cama_user-list-create')
        self.testData = TestData

    def test_get_cama_users(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_cama_user(self):
        response = self.client.post(self.url, self.testData.cama_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CamaUser.objects.count(), 1)
        self.assertEqual(CamaUser.objects.get().name, 'John Doe')


class StudyListCreateAPIViewTests(APITestCase):
    def setUp(self):
        self.url = reverse('study-list-create')
        self.testData = TestData

    def test_create_study(self):
        '''CamaUser.objects.create(orc_id='0000-0002-1825-0097',
                                name="John Doe", 
                                email="john.doe@example.com", 
                                organization="Example University", 
                                nr_uploads=5)'''
        response = self.client.post(self.url, self.testData.study_data, format='json')
        logger.info(f"Response after POST: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Study.objects.count(), 1)
        study = Study.objects.first()
        self.assertEqual(study.cama_user.orc_id, "0000-0002-1825-0097")
        self.assertEqual(study.cama_user.name, "John Doe")

    def test_invalid_study(self):
        invalid_payload = {}  # Payload with missing required fields
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Study.objects.count(), 0)  # No object should be created


class ExperimentTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('experiment-list-create') 
        self.testData = TestData

    def test_create_experiment(self):
        response = self.client.post(self.url, self.testData.experiment_data, format='json')
        logger.info(f"Response after POST: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Experiment.objects.count(), 1)
        experiment = Experiment.objects.first()
        self.assertEqual(experiment.study.cama_user.orc_id, "0000-0002-1825-0097")


      





