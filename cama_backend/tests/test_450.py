from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from myapi.models import *
from tests.factories import *
import json
import logging
logger = logging.getLogger(__name__)
from myapi.serializers import study, experiment, effect_data

def helper_get_population_test(self, url):
    """
    Helper function to test GET requests to the specified URL.

    This function sends a GET request to the given URL, asserts that the response 
    content length is greater than 1, and checks if the response status code is 200 OK.

    Args:
        url (str): The endpoint to send the GET request to.
    """
    response = self.client.get(f'/api/{url}')
    assert len(response.content) > 1
    self.assertEqual(response.status_code, status.HTTP_200_OK)

def helper_post_population_test(self, url, variable):
    """
    Helper function to test POST requests to the specified URL with a given variable.

    This function sends a POST request with a sample payload to the given URL, 
    and checks if the response status code is 201 CREATED.

    Args:
        url (str): The endpoint to send the POST request to.
        variable (str): The key for the variable in the data payload.
    """
    data = {
        "id": 1,
        f"{variable}": "test"
    }
    response = self.client.post(f'/api/{url}', data, format='json') 
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

class CountryAlternativesAPITest(TestCase):
    """
    Test case for testing Country alternatives API.
    """

    def setUp(self):
        self.client = APIClient()
    
    def test_get_country_alternatives(self):
        """
        Test the GET method for country alternatives.
        """
        helper_get_population_test(self, 'populate-country/')
        
    def test_post_country_alternatives(self):
        """
        Test the POST method for country alternatives.
        """
        helper_post_population_test(self, 'populate-country/', 'name')
        

class CategoryAlternativesAPITest(TestCase):
    """
    Test case for testing Category alternatives API.
    """

    def setUp(self):
        self.client = APIClient()
    
    def test_get_category_alternatives(self):
        """
        Test the GET method for category alternatives.
        """
        helper_get_population_test(self, 'populate-category/')
        
    def test_post_category_alternatives(self):
        """
        Test the POST method for category alternatives.
        """
        helper_post_population_test(self, 'populate-category/', 'name')
        

class StudyDesignAlternativesAPITest(TestCase):
    """
    Test case for testing Study Design alternatives API.
    """

    def setUp(self):
        self.client = APIClient()
    
    def test_get_study_design_alternatives(self):
        """
        Test the GET method for study design alternatives.
        """
        helper_get_population_test(self, 'populate-study-design/')
        
    def test_post_study_design_alternatives(self):
        """
        Test the POST method for study design alternatives.
        """
        helper_post_population_test(self, 'populate-study-design/', 'design')


class RiskOfBiasAlternativesAPITest(TestCase):
    """
    Test case for testing Risk of Bias alternatives API.
    """

    def setUp(self):
        self.client = APIClient()
    
    def test_get_risk_of_bias_alternatives(self):
        """
        Test the GET method for risk of bias alternatives.
        """
        helper_get_population_test(self, 'populate-risk-of-bias/')
        
    def test_post_risk_of_bias_alternatives(self):
        """
        Test the POST method for risk of bias alternatives.
        """
        helper_post_population_test(self, 'populate-risk-of-bias/', 'rob')
        

class ParticipantDesignAlternativesAPITest(TestCase):
    """
    Test case for testing Participant Design alternatives API.
    """

    def setUp(self):
        self.client = APIClient()
    
    def test_get_participant_design_alternatives(self):
        """
        Test the GET method for participant design alternatives.
        """
        helper_get_population_test(self, 'populate-participant-design/')
        
    def test_post_participant_design_alternatives(self):
        """
        Test the POST method for participant design alternatives.
        """
        helper_post_population_test(self, 'populate-participant-design/', 'design')
        

class ImplementationAlternativesAPITest(TestCase):
    """
    Test case for testing Implementation alternatives API.
    """

    def setUp(self):
        self.client = APIClient()
    
    def test_get_implementation_alternatives(self):
        """
        Test the GET method for implementation alternatives.
        """
        helper_get_population_test(self, 'populate-implementation/')
        
    def test_post_implementation_alternatives(self):
        """
        Test the POST method for implementation alternatives.
        """
        helper_post_population_test(self, 'populate-implementation/', 'implementor')
        

class TestTimeAlternativesAPITest(TestCase):
    """
    Test case for testing Test Time alternatives API.
    """

    def setUp(self):
        self.client = APIClient()
    
    def test_get_test_time_alternatives(self):
        """
        Test the GET method for test time alternatives.
        """
        helper_get_population_test(self, 'populate-test-time/')
        
    def test_post_test_time_alternatives(self):
        """
        Test the POST method for test time alternatives.
        """
        helper_post_population_test(self, 'populate-test-time/', 'time')
        

class EffectSizeTypeAlternativesAPITest(TestCase):
    """
    Test case for testing Effect Size Type alternatives API.
    """

    def setUp(self):
        self.client = APIClient()
    
    def test_get_effect_size_type_alternatives(self):
        """
        Test the GET method for effect size type alternatives.
        """
        helper_get_population_test(self, 'populate-effect-size-type/')
        
    def test_post_effect_size_type_alternatives(self):
        """
        Test the POST method for effect size type alternatives.
        """
        helper_post_population_test(self, 'populate-effect-size-type/', 'name')
        

@pytest.mark.django_db   
class ExperimentFilterAPITest(TestCase):
    """
    Test case for testing the filtering of Experiment data.
    """

    def setUp(self):
        self.client = APIClient()
    
    def test_get_filter_data(self):
        """
        Test the GET method for filtering experiment data based on specific criteria.

        This test creates a batch of Experiment instances, filters them based on 
        given parameters, and verifies the count of filtered results matches the expected count.
        """
        experiemnt = ExperimentFactory.create_batch(100)
        response = self.client.get(f'/api/experiment-filterd/?intensity_n=7&grade__seventh=True')
        exp_count = 0
        for x in experiemnt:
            if (x.intensity_n == 7 and x.grade.seventh == True):
                exp_count += 1 
        assert len(response.data) == exp_count
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

@pytest.mark.django_db   
class EffectDataFilterAPITest(TestCase):
    """
    Test case for testing the filtering of EffectData.
    """

    def setUp(self):
        self.client = APIClient()
    
    def test_get_filter_data(self):
        """
        Test the GET method for filtering effect data based on specific criteria.

        This test creates a batch of EffectData instances, filters them based on 
        given parameters, and verifies the count of filtered results matches the expected count.
        """
        effect_datas = EffectDataFactory.create_batch(10)
        smd_count = 0
        for effect_data in effect_datas:
            name = effect_data.effect_size_type.name
            if name == "SMD":
                smd_count += 1
                
        response = self.client.get(f'/api/effect-data-filterd/?effect_size_type__name=SMD')
        assert len(response.data) == smd_count
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

@pytest.mark.django_db   
class StudyFilterAPITest(TestCase):
    """
    Test case for testing the filtering of Study data.
    """

    def setUp(self):
        self.client = APIClient()
    
    def test_get_filter_data(self):
        """
        Test the GET method for filtering study data based on specific criteria.

        This test creates a batch of Study instances, filters them based on 
        given parameters, and verifies the count of filtered results matches the expected count.
        """
        studies = StudyFactory.create_batch(100)
        sweden_count = 0
        for study in studies:
            name = study.country.name
            if name == "Sweden":
                sweden_count += 1
                
        response = self.client.get(f'/api/studies-filterd/?country__name=Sweden')
        assert len(response.data) == sweden_count
        self.assertEqual(response.status_code, status.HTTP_200_OK)


@pytest.mark.django_db   
class StudySearchAPITest(TestCase):
    """
    Test case for testing the search functionality of Study data.
    """

    def setUp(self):
        self.client = APIClient()
    
    def test_get_search_data(self):
        """
        Test the GET method for searching study data based on author and title.

        This test creates a batch of Study instances, searches for them based on 
        author and title, and verifies the count of search results matches the expected count.
        """
        studies = StudyFactory.create_batch(100)
        response = self.client.get(f'/api/studies-search/?authors=Thomas')
        name_count = 0
        for x in studies:
            if x.authors == 'Thomas':
                name_count += 1
        assert len(response.data) == name_count
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        word = 'fine'
        response = self.client.get(f'/api/studies-search/?title={word}')        
        word_count = 0
        for x in studies:
            if word in x.title:
                word_count += 1
        assert len(response.data) == word_count
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_search_data_wrong(self):
        """
        Test the GET method for searching study data with incorrect criteria.

        This test creates a batch of Study instances, searches for them based on 
        incorrect criteria, and verifies the count of search results matches the expected count.
        """
        studies = StudyFactory.create_batch(100)
        response = self.client.get(f'/api/studies-search/?authors=Thomas')
        name_count = 0
        for x in studies:
            if x.authors == 'Thomas':
                name_count += 1
        assert len(response.data) == name_count
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        word = 'fine'
        response = self.client.get(f'/api/studies-search/?title={word}')        
        word_count = 0
        for x in studies:
            if word in x.title:
                word_count += 1
        assert len(response.data) == word_count
        self.assertEqual(response.status_code, status.HTTP_200_OK)
                    

@pytest.mark.django_db   
class Feat450IntegrationTest(TestCase):
    """
    Integration test case for Feature 450.

    This test case tests the integration of various endpoints and ensures data 
    consistency across different parts of the application.
    """

    def setUp(self):
        self.client = APIClient()
    
    def test(self):
        """
        Integration test for Feature 450.

        This test generates data, fetches country and study design data, filters 
        experiments based on certain criteria, and verifies the filtered results 
        match the expected count.
        """
        generated_data = ExperimentFactory.create_batch(10)
        
        country_response = self.client.get(f'/api/populate-country/')
        self.assertEqual(country_response.status_code, status.HTTP_200_OK)
        country_list = []
        for country in country_response.data:
            country_list.append([country['id'], country['name']])
        
        
        study_design_response = self.client.get(f'/api/populate-study-design/')
        self.assertEqual(country_response.status_code, status.HTTP_200_OK)
        design_list = []
        for study_design in study_design_response.data:
            design_list.append([study_design['id'], study_design['design']])
           
        experiment_count = 0
        for x in generated_data:
            if x.study_id.country.name == country_list[46][1] and x.study_design.design == design_list[0][1]: 
                experiment_count += 1
                
        filterd_experiments_response = self.client.get(f'/api/experiment-filterd/?study_id__country={country_list[46][0]}&study_design={design_list[0][0]}')
        assert len(filterd_experiments_response.data) == experiment_count
        self.assertEqual(filterd_experiments_response.status_code, status.HTTP_200_OK)
