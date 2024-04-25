from django.test import TestCase
from rest_framework import status


def helper_population_test(self, url):
    response = self.client.get(f'/api/{url}')
    assert len(response.content) > 1; 
    self.assertEqual(response.status_code, status.HTTP_200_OK)

class CountryAlternitivesAPITest(TestCase):
    def test_get_country_alternetivs(self):
        helper_population_test(self, 'populate-country/')
        
        
class CategoryAlternitivesAPITest(TestCase):
    def test_get_category_alternetivs(self):
        helper_population_test(self, 'populate-category/')
         
         
class StudyDesignAlternitivesAPITest(TestCase):
    def test_get_study_design_alternetivs(self):
        helper_population_test(self, 'populate-study-design/')
        

class RiskOfBiasAlternitivesAPITest(TestCase):
    def test_get_study_design_alternetivs(self):
        helper_population_test(self, 'populate-risk-of-bias/')
        

class ParticipantDesignAlternitivesAPITest(TestCase):
    def test_get_participant_design_alternetivs(self):
        helper_population_test(self, 'populate-participant-design/')
        

class ImplementationAlternitivesAPITest(TestCase):
    def test_get_implementation_alternetivs(self):
        helper_population_test(self, 'populate-implementation/')
        
        
class TestTimeAlternitivesAPITest(TestCase):
    def test_get_test_time_alternetivs(self):
        helper_population_test(self, 'populate-test-time/')
        
        
class EffectSizeTypeAlternitivesAPITest(TestCase):
    def test_get_effect_size_type_alternetivs(self):
        helper_population_test(self, 'populate-effect-size-type/')
        

        
