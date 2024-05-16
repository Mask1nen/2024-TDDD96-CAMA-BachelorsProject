from rest_framework.test import APITestCase
from django.urls import reverse
from .data_471 import TestData

from rest_framework import status
from myapi.models import *
from rest_framework.test import APIClient

import logging
logger = logging.getLogger(__name__)

# class CamaUserAPITest(APITestCase):
#     def setUp(self):
#         self.url = reverse('cama_users')
#         self.testData = TestData

#     def test_get_post_cama_user(self):
#         response = self.client.post(self.url, self.testData.cama_user_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data[0].get('orc_id'), '0000-0002-1825-0097')

#     def test_invalid_cama_user(self):
#         invalid_payload = {}  # Payload with missing required fields
#         response = self.client.post(self.url, invalid_payload, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(CamaUser.objects.count(), 0)  # No object should be created


# class StudyTestCase(APITestCase):
#     def setUp(self):
#         self.url = reverse('studies')
#         self.detailed_url = reverse('detailed-study', kwargs={'study_id': 432})

#         self.testData = TestData
#         CamaUser.objects.create(orc_id='0000-0002-1825-0097',
#                                 name="John Doe")

#     def test_post_get_barestudy(self):
#         response = self.client.post(self.url, self.testData.bare_study_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         response = self.client.get(self.url)
#         #logger.info(response.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         study_uploader = response.data[0].get('uploader')
#         self.assertEqual(study_uploader, '0000-0002-1825-0097')
#         experiments_list = response.data[0].get('experiments')
#         self.assertEqual(experiments_list, [])

#     def test_post_get_fullstudy(self):
#         response = self.client.post(self.url, self.testData.full_study_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         response = self.client.get(self.url)
#         logger.info(response.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         study_uploader = response.data[0].get('uploader')
#         self.assertEqual(study_uploader, '0000-0002-1825-0097')
#         study_id = response.data[0].get('experiments')[0].get('study_id')
#         self.assertEqual(study_id, 432)
#         study_experimentnr = response.data[0].get('experiments')[0].get('effects')[0].get('experiment_nr')
#         self.assertEqual(study_experimentnr, 131)

#         print(study_id, 'banan')
#         update_data = {}
#         response = self.client.patch(self.detailed_url, update_data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['approved'], True)
#         print(response.data)
#         self.assertEqual(response.data['experiments'][0]['effects'][0]['approved'], True)
    

#     def test_post_get_halfstudy(self):
#         response = self.client.get(self.url)
#         study_id = response.data
#         print(study_id)

#         response = self.client.post(self.url, self.testData.half_study_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         response = self.client.get(self.url)
#         logger.info(response.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         study_uploader = response.data[0].get('uploader')
#         self.assertEqual(study_uploader, '0000-0002-1825-0097')
#         study_id = response.data[0].get('experiments')[0].get('study_id')
#         self.assertEqual(study_id, 433)
#         study_effectslist = response.data[0].get('experiments')[0].get('effects')
#         self.assertEqual(study_effectslist, [])


#     def test_invalid_study(self):
#         invalid_payload = {}  # Payload with missing required fields
#         response = self.client.post(self.url, invalid_payload, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(Study.objects.count(), 0)  # No object should be created

class ExperimentTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('experiments') 
        self.testData = TestData
        user = CamaUser.objects.create(orc_id='0000-0002-1825-0097', name="John Doe")
        study = Study.objects.create(uploader=user, study_year=2024, peer_reviewed=True, 
                             authors="", doi="", abstract="", keywords="",
                             approved=False)

    def test_post_get_bareexperiment(self):
        response = self.client.post(self.url, self.testData.bare_experiment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(self.url)
        #logger.info(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        experiment_study = response.data[0].get('study_id')
        self.assertEqual(experiment_study, 432)
        effectslist = response.data[0].get('effects')
        self.assertEqual(effectslist, [])

    def test_post_get_fullexperiment(self):
        response = self.client.post(self.url, self.testData.full_experiment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(self.url)
        #logger.info(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        experiment_study = response.data[0].get('study_id')
        self.assertEqual(experiment_study, 433)
        effect_experimentnr = response.data[0].get('effects')[0].get('experiment_nr')
        self.assertEqual(effect_experimentnr, 132)

    def test_invalid_experiment(self):
        invalid_payload = {}  # Payload with missing required fields
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Experiment.objects.count(), 0)  # No object should be created

class EffectDataTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('effect_data') 
        self.testData = TestData
        user = CamaUser.objects.create(orc_id='0000-0002-1825-0097', name="John Doe")
        study = Study.objects.create(uploader=user, study_year=2024, peer_reviewed=True, 
                             authors="", doi="", abstract="", keywords="",
                             approved=False)
        experiment = Experiment.objects.create(study_id=study, ni=1, intervention="", intervention_op="",
                                               target_population="")

    def test_get_post_effect_data(self):
        response = self.client.post(self.url, self.testData.effect_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(self.url)
        #logger.info(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        experimentnr = response.data[0].get('experiment_nr')
        self.assertEqual(experimentnr, 133)

    def test_invalid_effect_data(self):
        invalid_payload = {}  # Payload with missing required fields
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(EffectData.objects.count(), 0)  # No object should be created
      



