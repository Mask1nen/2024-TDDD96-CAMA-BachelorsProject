from rest_framework.test import APITestCase
from django.urls import reverse
from .data_471 import TestData

from rest_framework import status
from myapi.models import *
from rest_framework.test import APIClient

import logging
logger = logging.getLogger(__name__)

class CamaUserAPITest(APITestCase):
    """
    Test suite for CamaUser API endpoints.
    
    Tests both POST and GET requests to create and retrieve CamaUser instances.
    """

    def setUp(self):
        """
        Set up the test environment.

        Initialize the URL for the CamaUser endpoint and test data.
        """
        self.url = reverse('cama_users')
        self.testData = TestData

    def test_get_post_cama_user(self):
        """
        Test creating and retrieving a CamaUser.

        Sends a POST request with valid data to create a CamaUser and then
        sends a GET request to retrieve the created user.
        """
        response = self.client.post(self.url, self.testData.cama_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get('orc_id'), '0000-0002-1825-0097')

    def test_invalid_cama_user(self):
        """
        Test creating a CamaUser with invalid data.

        Sends a POST request with missing required fields to ensure the request 
        is rejected and no object is created.
        """
        invalid_payload = {}  # Payload with missing required fields
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CamaUser.objects.count(), 0)  # No object should be created


class StudyTestCase(APITestCase):
    """
    Test suite for Study API endpoints.
    
    Tests creating and retrieving Study instances with varying levels of completeness.
    """

    def setUp(self):
        """
        Set up the test environment.

        Initialize the URLs for the Study endpoints and create necessary related objects.
        """
        self.url = reverse('studies')
        self.detailed_url = reverse('detailed-study', kwargs={'study_id': 432})

        self.testData = TestData
        CamaUser.objects.create(orc_id='0000-0002-1825-0097', name="John Doe")
        Country.objects.create(name="United States")
        Category.objects.create(name="Health")
        StudyDesign.objects.create(design="Randomized Controlled Trial")
        RiskOfBias.objects.create(rob="Low")
        ParticipantDesign.objects.create(design="Between-Group Design")
        Implementation.objects.create(implementor="Pilot Study")
        TestTime.objects.create(time="1")
        EffectSizeType.objects.create(name="type")

    def test_post_get_barestudy(self):
        """
        Test creating and retrieving a minimal Study.

        Sends a POST request with minimal valid data to create a Study and then
        sends a GET request to retrieve the created study.
        """
        response = self.client.post(self.url, self.testData.bare_study_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        study_uploader = response.data[0].get('uploader')
        self.assertEqual(study_uploader, '0000-0002-1825-0097')
        experiments_list = response.data[0].get('experiments')
        self.assertEqual(experiments_list, [])

    def test_post_get_fullstudy(self):
        """
        Test creating and retrieving a full Study with nested objects.

        Sends a POST request with full valid data to create a Study and then
        sends a GET request to retrieve the created study. Also tests updating the study.
        """
        response = self.client.post(self.url, self.testData.full_study_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        study_uploader = response.data[0].get('uploader')
        self.assertEqual(study_uploader, '0000-0002-1825-0097')
        study_id = response.data[0].get('experiments')[0].get('study_id')
        self.assertEqual(study_id, 432)
        study_experimentnr = response.data[0].get('experiments')[0].get('effects')[0].get('experiment_nr')
        self.assertEqual(study_experimentnr, 131)

        update_data = {}
        response = self.client.patch(self.detailed_url, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['approved'], True)
        self.assertEqual(response.data['experiments'][0]['effects'][0]['approved'], True)

    def test_post_get_halfstudy(self):
        """
        Test creating and retrieving a partially complete Study.

        Sends a POST request with partial valid data to create a Study and then
        sends a GET request to retrieve the created study.
        """
        response = self.client.get(self.url)
        study_id = response.data

        response = self.client.post(self.url, self.testData.half_study_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        study_uploader = response.data[0].get('uploader')
        self.assertEqual(study_uploader, '0000-0002-1825-0097')
        study_id = response.data[0].get('experiments')[0].get('study_id')
        self.assertEqual(study_id, 433)
        study_effectslist = response.data[0].get('experiments')[0].get('effects')
        self.assertEqual(study_effectslist, [])

    def test_invalid_study(self):
        """
        Test creating a Study with invalid data.

        Sends a POST request with missing required fields to ensure the request 
        is rejected and no object is created.
        """
        invalid_payload = {}  # Payload with missing required fields
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Study.objects.count(), 0)  # No object should be created


class ExperimentTestCase(APITestCase):
    """
    Test suite for Experiment API endpoints.
    
    Tests creating and retrieving Experiment instances with varying levels of completeness.
    """

    def setUp(self):
        """
        Set up the test environment.

        Initialize the URL for the Experiment endpoint and create necessary related objects.
        """
        self.url = reverse('experiments')
        self.testData = TestData
        user = CamaUser.objects.create(orc_id='0000-0002-1825-0097', name="John Doe")
        study = Study.objects.create(uploader=user, study_year=2024, peer_reviewed=True, 
                                     authors="", doi="", abstract="", keywords="",
                                     approved=False)
        StudyDesign.objects.create(design="Randomized Controlled Trial")
        RiskOfBias.objects.create(rob="Low")
        ParticipantDesign.objects.create(design="Between-Group Design")
        Implementation.objects.create(implementor="Pilot Study")
        TestTime.objects.create(time="1")
        EffectSizeType.objects.create(name="type")

    def test_post_get_bareexperiment(self):
        """
        Test creating and retrieving a minimal Experiment.

        Sends a POST request with minimal valid data to create an Experiment and then
        sends a GET request to retrieve the created experiment.
        """
        response = self.client.post(self.url, self.testData.bare_experiment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        experiment_study = response.data[0].get('study_id')
        self.assertEqual(experiment_study, 435)
        effectslist = response.data[0].get('effects')
        self.assertEqual(effectslist, [])

    def test_post_get_fullexperiment(self):
        """
        Test creating and retrieving a full Experiment with nested objects.

        Sends a POST request with full valid data to create an Experiment and then
        sends a GET request to retrieve the created experiment.
        """
        response = self.client.post(self.url, self.testData.full_experiment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        experiment_study = response.data[0].get('study_id')
        self.assertEqual(experiment_study, 436)
        effect_experimentnr = response.data[0].get('effects')[0].get('experiment_nr')
        self.assertEqual(effect_experimentnr, 134)

    def test_invalid_experiment(self):
        """
        Test creating an Experiment with invalid data.

        Sends a POST request with missing required fields to ensure the request 
        is rejected and no object is created.
        """
        invalid_payload = {}  # Payload with missing required fields
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Experiment.objects.count(), 0)  # No object should be created


class EffectDataTestCase(APITestCase):
    """
    Test suite for EffectData API endpoints.
    
    Tests creating and retrieving EffectData instances.
    """

    def setUp(self):
        """
        Set up the test environment.

        Initialize the URL for the EffectData endpoint and create necessary related objects.
        """
        self.url = reverse('effect_data')
        self.testData = TestData
        user = CamaUser.objects.create(orc_id='0000-0002-1825-0097', name="John Doe")
        study = Study.objects.create(uploader=user, study_year=2024, peer_reviewed=True, 
                                     authors="", doi="", abstract="", keywords="",
                                     approved=False)
        experiment = Experiment.objects.create(study_id=study, ni=1, intervention="", intervention_op="",
                                               target_population="")
        EffectSizeType.objects.create(name="type")
        TestTime.objects.create(time="1")


    def test_get_post_effect_data(self):
        """
        Test creating and retrieving EffectData.

        Sends a POST request with valid data to create an EffectData instance and then
        sends a GET request to retrieve the created effect data.
        """
        response = self.client.post(self.url, self.testData.effect_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        experimentnr = response.data[0].get('experiment_nr')
        self.assertEqual(experimentnr, 135)

    def test_invalid_effect_data(self):
        """
        Test creating EffectData with invalid data.

        Sends a POST request with missing required fields to ensure the request 
        is rejected and no object is created.
        """
        invalid_payload = {}  # Payload with missing required fields
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(EffectData.objects.count(), 0)  # No object should be created
