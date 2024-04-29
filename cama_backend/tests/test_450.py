from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from myapi.models import *
from tests.factories import *
import json
import logging
logger = logging.getLogger(__name__)



def helper_get_population_test(self, url):
    response = self.client.get(f'/api/{url}')
    assert len(response.content) > 1; 
    self.assertEqual(response.status_code, status.HTTP_200_OK)

def helper_post_population_test(self, url, variable):
    data = {
        "id": 1,
        f"{variable}": "test"
    }
    response = self.client.post(f'/api/{url}', data, format='json') 
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    
class CountryAlternitivesAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_country_alternetivs(self):
        helper_get_population_test(self, 'populate-country/')
        
    def test_post_country_alternetivs(self):
        helper_post_population_test(self, 'populate-country/', 'name')
        
        
class CategoryAlternitivesAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_category_alternetivs(self):
        helper_get_population_test(self, 'populate-category/')
        
    def test_post_category_alternetivs(self):
        helper_post_population_test(self, 'populate-category/', 'name')
         
class StudyDesignAlternitivesAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_study_design_alternetivs(self):
        helper_get_population_test(self, 'populate-study-design/')
        
    def test_post_study_design_alternetivs(self):
        helper_post_population_test(self, 'populate-study-design/', 'design')

class RiskOfBiasAlternitivesAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_study_design_alternetivs(self):
        helper_get_population_test(self, 'populate-risk-of-bias/')
        
    def test_post_risk_of_bias_alternetivs(self):
        helper_post_population_test(self, 'populate-risk-of-bias/', 'rob')    
        

class ParticipantDesignAlternitivesAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_participant_design_alternetivs(self):
        helper_get_population_test(self, 'populate-participant-design/')
        
    def test_post_participant_design_alternetivs(self):
        helper_post_population_test(self, 'populate-participant-design/', 'design')
        

class ImplementationAlternitivesAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_implementation_alternetivs(self):
        helper_get_population_test(self, 'populate-implementation/')
        
    def test_post_implementation_alternetivs(self):
        helper_post_population_test(self, 'populate-implementation/', 'implementor')
        
        
class TestTimeAlternitivesAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_test_time_alternetivs(self):
        helper_get_population_test(self, 'populate-test-time/')
        
    def test_post_test_time_alternetivs(self):
        helper_post_population_test(self, 'populate-test-time/', 'time')
        
        
class EffectSizeTypeAlternitivesAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_effect_size_type_alternetivs(self):
        helper_get_population_test(self, 'populate-effect-size-type/')
        
    def test_post_effect_size_type_alternetivs(self):
        helper_post_population_test(self, 'populate-effect-size-type/', 'name')
        

@pytest.mark.django_db   
class ExperimentFilterAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_filter_data(self):
        experiemnt = ExperimentFactory.create_batch(10)
        response = self.client.get(f'/api/experiment-filterd/?intensity_n=7&grade__seventh=True')
        assert len(response.data) == 2;
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
@pytest.mark.django_db   
class EffectDataFilterAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_filter_data(self):
        effect_datas = EffectDataFactory.create_batch(10)
        smd_count = 0
        for effect_data in effect_datas:
            name = effect_data.effect_size_type.name
            if name == "SMD":
                smd_count += 1
                
        response = self.client.get(f'/api/effect-data-filterd/?effect_size_type__name=SMD')
        assert len(response.data) == smd_count;
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
@pytest.mark.django_db   
class StudyFilterAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_filter_data(self):
        studies = StudyFactory.create_batch(10)
        sweden_count = 0
        for study in studies:
            name = study.country.name
            if name == "Sweden":
                sweden_count += 1
                
        response = self.client.get(f'/api/studies-filterd/?country__name=Sweden')
        assert len(response.data) == sweden_count;
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
# Integration test
# Get the different options of the options tables through get calls to them.
# Add an additional option.
# Filter for studies with help of the accuired alternetives.
# Check so the filterd gets worked. 

        

        
    



        
