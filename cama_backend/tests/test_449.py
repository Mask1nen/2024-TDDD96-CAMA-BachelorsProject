from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from myapi.models import *
from tests.factories import *
import csv
from django.http import HttpResponse


from io import StringIO

import logging
logger = logging.getLogger(__name__)
from myapi.serializers import study, experiment, effect_data


@pytest.mark.django_db   
class DownloadTest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_download_csv(self):
        # Generate some test data
        generated_data = EffectDataFactory.create_batch(10)
           
        # Count the number of records with 'Sweden' as the country
        expected_count = 0
        for data in generated_data:
            if data.experiment_nr.study_id.country.name == "Sweden" and data.experiment_nr.grade.third == True:
                expected_count += 1
        
        # Make a GET request to the endpoint that downloads the CSV
        response = self.client.get('/api/download-effects/?country__name=Sweden&grade__third=True')

        # Read the content of the CSV response
        csv_data = response.content.decode('utf-8')
        print(f'{response.content}')
        # Use StringIO to read the CSV content as a file-like object
        csv_file = StringIO(csv_data)
        
        # Parse the CSV content using csv.reader
        csv_reader = csv.reader(csv_file)
        
        # Calculate the number of rows in the CSV
        actual_count = sum(1 for row in csv_reader) - 1  # Subtract 1 for the header
        print(f'the response content data csv {csv_data}')
        
        # Check if the number of rows matches the expected count
        self.assertEqual(expected_count, actual_count)
        
        response = self.client.get('/api/download-effects/?title=May watch apply college rock him stock same.')
        
        # Read the content of the CSV response
        csv_data = response.content.decode('utf-8')
        print(f'{response.content}')
        # Use StringIO to read the CSV content as a file-like object
        csv_file = StringIO(csv_data)
        
        # Parse the CSV content using csv.reader
        csv_reader = csv.reader(csv_file)
        
        # Calculate the number of rows in the CSV
        actual_count = sum(1 for row in csv_reader) - 1  # Subtract 1 for the header
        print(f'the response content data csv {response.content}')
        
        response = self.client.get('/api/download-effects/?country__name=Sweden&grade__k=False')
        print(f'the response content data csv last one {response.content}')
        
        self.assertEqual(response.status_code, 404)
