from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from myapi.models import CamaUser, Study, Country, Category
from myapi.serializers import StudySerializer, ExperimentSerializer

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



class StudyListCreateAPIViewTests(APITestCase):
    def setUp(self):
        self.url = reverse('study-list-create')
        self.valid_payload = {
            "study_year":  2022,
            "country": "Country",
            "category": "Category",
            "peer_reviewed": True,
            "authors": "Author",
            "doi": "example_doi",
            "abstract": "Abstract",
            "keywords": "Keywords",
            "nr_downloads": 100,
            'experiment': [{'gender_2': 0.5, 'experiment_nr':1, 'gender_1':0.5, 'intensity_n':1, 'duration_week':1, 'frequency_n':1, 'outcome':'test','outcome_full':'test',
                            'study_design':'design',
                            #'risks': {'rob': 'rob', 'robins':'robins'},
                            #'grade': 'grade',
                            #'participant_design': 'design',
                            #'implemented': 'implementor'
                            
                            
                            
        }
                           
                           
                           ]
        }

    def test_create_study(self):
        Category.objects.create(name="Category")
        Country.objects.create(name="Country")
        StudyDesign.objects.create(design='design')
        # Grade.objects.create(grade='grade')
        # ParticipantDesign.objects.create(design='design')
        # Implementation.objects.create(implementor='implementor')



        response = self.client.post(self.url, self.valid_payload, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(self.url)
        print(response.data)
        # self.assertEqual(Study.objects.count(), 1)
        # study = Study.objects.first()
        # self.assertEqual(study.uploader.orc_id, "12345")
        # self.assertEqual(study.study_year.study_year, 2022)
        # self.assertEqual(study.country.name, "Example Country")
        # self.assertEqual(study.category.name, "Example Category")
        # self.assertTrue(study.peer_reviewed)
        # self.assertEqual(study.authors, "Example Author")
        # self.assertEqual(study.doi, "example_doi")
        # self.assertEqual(study.abstract, "Example Abstract")
        # self.assertEqual(study.keywords, "Example Keywords")
        # self.assertEqual(study.nr_downloads, "100")

    def test_invalid_study(self):
        invalid_payload = {}  # Payload with missing required fields
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Study.objects.count(), 0)  # No object should be created

from myapi.models import Study, Country, Category, CamaUser,  StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, Experiment
from rest_framework.renderers import JSONRenderer




class ExperimentTestCase(TestCase):
    def setUp(self):

        self.experiment_attributes = {
            "gender_2":0.500,
            "study_id":5
        }
        self.client = APIClient()




    def test_create_experiment_get_request(self):


        url = reverse('experiment-list-create') 

        response = self.client.post(url, self.experiment_attributes, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Experiment.objects.count(), 1)
        #self.assertEqual(Experiment.objects.get().study_design.design, self.experiment_attributes['study_design']['design'])

    def test_create_experiment_post_request(self):
        self.study = Study.objects.create(
            uploader=CamaUser.objects.create(
                orc_id="12345",
                name="John Doe",
                email="john@example.com",
                organization="Example Org",
                nr_uploads=5
            ),
            country=Country.objects.create(name="Example Country"),
            category=Category.objects.create(name="Example Category"),
            peer_reviewed=True,
            authors="Example Author",
            doi="example_doi",
            abstract="Example Abstract",
            keywords="Example Keywords",
            nr_downloads="100"
        )

        self.studyDesign = StudyDesign.objects.create(
            design="Example"
        )
        self.risks = RiskOfBias.objects.create(

            id=1,
            rob='low',
            robins='low'
        )
        self.grade = Grade.objects.create(
            grade='A'
        )
        self.participantDesign = ParticipantDesign.objects.create(
            design = 'Test'
        )

        self.implemented = Implementation.objects.create(
            implementor = 'Test'
        )

        # experiment = Experiment.objects.create(
        #     study_id = self.study,
        #     experiment_nr = 112,
        #     study_design=self.studyDesign,
        #     risks=self.risks,
        #     grade=self.grade,
        #     participant_design=self.participantDesign,
        #     implemented=self.implemented,
        #     gender_1=0.5,
        #     gender_2=0.5,
        #     intensity_n=0.5,
        #     duration_week=1,
        #     frequency_n=0.5,
        #     outcome='a',
        #     outcome_full='b'
        # )  # or however you get your experiment


        # # Create a serializer instance
        # serializer = ExperimentSerializer(experiment)

        # # Generate JSON
        # json_data = JSONRenderer().render(serializer.data)

        # # If you want the JSON as a string
        # json_str = json_data.decode('utf-8')
        # print(json_str)

        pass



      





