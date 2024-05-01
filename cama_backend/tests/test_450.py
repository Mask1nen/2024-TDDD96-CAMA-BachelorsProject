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
        experiemnt = ExperimentFactory.create_batch(100)
        response = self.client.get(f'/api/experiment-filterd/?intensity_n=7&grade__seventh=True')
        exp_count = 0
        for x in experiemnt:
            if (x.intensity_n == 7 and x.grade.seventh == True):
                exp_count += 1 
        assert len(response.data) == exp_count;
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
        studies = StudyFactory.create_batch(100)
        sweden_count = 0
        for study in studies:
            name = study.country.name
            if name == "Sweden":
                sweden_count += 1
                
        response = self.client.get(f'/api/studies-filterd/?country__name=Sweden')
        assert len(response.data) == sweden_count;
        self.assertEqual(response.status_code, status.HTTP_200_OK)


@pytest.mark.django_db   
class StudySearchAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_search_data(self):
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
    def setUp(self):
        self.client = APIClient()
    
    def test(self):
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

