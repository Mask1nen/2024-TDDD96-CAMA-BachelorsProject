import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CamaUser, Experiment, Study, EffectData, Country, Category, StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, TestTime, EffectSizeType
from .serializers.cama_user import CamaUserSerializer
from .serializers.study import StudySerializer, StudyCreateSerializer, CountrySerializer, CategorySerializer
from .serializers.experiment import ExperimentSerializer, ExperimentCreateSerializer, StudyDesignSerializer, RiskOfBiasSerializer, GradeSerializer, ParticipantDesignSerializer, ImplementationSerializer
from .serializers.effect_data import EffectDataSerializer, EffectDataCreateSerializer, EffectSizeTypeSerializer, TestTimeSerializer
from django.http import JsonResponse
from django.db.models import Q
import csv
from django.http import HttpResponse


import logging
logger = logging.getLogger(__name__)

class FieldsView(APIView):
    def get(self, request):
        study_fields = {field.name: {
            'type': field.get_internal_type(),
            'required': not field.blank,
            'help_text': getattr(field, 'help_text', '')
        } for field in Study._meta.fields}

        experiment_fields = {field.name: {
            'type': field.get_internal_type(),
            'required': not field.blank,
            'help_text': getattr(field, 'help_text', '')
        } for field in Experiment._meta.fields}
    
        effect_fields = {field.name: {
            'type': field.get_internal_type(),
            'required': not field.blank,
            'help_text': getattr(field, 'help_text', '')
        } for field in EffectData._meta.fields}

        return JsonResponse({
            'study_fields': study_fields,
            'experiment_fields': experiment_fields,
            'effect_fields': effect_fields
    })

class CamaUserView(APIView):
    def get(self, request):
        cama_users = CamaUser.objects.all()
        serializer = CamaUserSerializer(cama_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        # Serialize the data and create a Study instance
        serializer = CamaUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudyView(APIView):
    def get(self, request):
        study = Study.objects.all()
        serializer = StudySerializer(study, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudyCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(StudySerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StudyFilterView(APIView):
    def get(self, request):
        # Get all the provided parameters from the query string
        parameters = request.GET.dict()
        # Create an empty Q object to hold the filters
        filters = Q()
        filter_condition = {}
        fields = [field.name for field in Study._meta.get_fields()]
        for key, value in parameters.items():
            if '__' in key:
                related_field, attribute = key.split('__')
                if (related_field in fields):
                    filter_condition = {f"{related_field}__{attribute}": value}
            else:
                if (key in fields):
                    filter_condition = {f"{key}": value}
            filters &= Q(**filter_condition)
        studies = Study.objects.all().filter(filters)
        serializer = StudySerializer(studies, many=True)
        return Response(serializer.data)
    
    
class ExperimentFilterView(APIView):
    def get(self, request):
        # Get all the provided parameters from the query string
        parameters = request.GET.dict()
        # Create an empty Q object to hold the filters
        filters = Q()
        filter_condition = {}
        fields = [field.name for field in Experiment._meta.get_fields()]
        for key, value in parameters.items():
            if '__' in key:
                related_field, attribute = key.split('__')
                if (related_field in fields):
                    filter_condition = {f"{related_field}__{attribute}": value}
            else:
                if (key in fields):
                    filter_condition = {f"{key}": value}
            filters &= Q(**filter_condition)
        experiments = Experiment.objects.all().filter(filters)
        serializer = ExperimentSerializer(experiments, many=True)
        return Response(serializer.data)
    
class EffectDataFilterView(APIView):
    def get(self, request):
        # Get all the provided parameters from the query string
        parameters = request.GET.dict()
        # Create an empty Q object to hold the filters
        filters = Q()
        filter_condition = {}
        fields = [field.name for field in EffectData._meta.get_fields()]
        for key, value in parameters.items():
            if '__' in key:
                related_field, attribute = key.split('__')
                if (related_field in fields):
                    filter_condition = {f"{related_field}__{attribute}": value}
            else:
                if (key in fields):
                    filter_condition = {f"{key}": value}
            filters &= Q(**filter_condition)
        effect_data = EffectData.objects.all().filter(filters)
        serializer = EffectDataSerializer(effect_data, many=True)
        return Response(serializer.data)
    
class StudySearchView(APIView):
    def get(self, request):
        # The title should be provided as url/?title=Part
         # Get all the provided parameters from the query string
        parameters = request.GET.dict()
        # Create an empty Q object to hold the filters
        filters = Q()
        for key, value in parameters.items():
            if key == 'title' or key == 'authors':
                filter_condition = {f"{key}__contains": value}
                filters &= Q(**filter_condition)
        studies = Study.objects.all().filter(filters)
        serializer = StudySerializer(studies, many=True)
        return Response(serializer.data)

class StudyDetailView(APIView):
    def get(self, request, id):
        try: 
            study = Study.objects.get(pk=id)
            serializer = StudySerializer(study)
            return Response(serializer.data)
        except Study.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ExperimentView(APIView):
    def get(self, request):
        experiments = Experiment.objects.all()
        serializer = ExperimentSerializer(experiments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExperimentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(ExperimentSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EffectDataView(APIView):
    def get(self, request):
        effect_data = EffectData.objects.all()
        serializer = EffectDataSerializer(effect_data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EffectDataCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class CountryOptionsView(APIView):
    def get(self, request):
        options = Country.objects.all()
        serializer = CountrySerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        name = request.data.pop('name')
        serializer = CountrySerializer(data={'name': name})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryOptionsView(APIView):
    def get(self, request):
        options = Category.objects.all()
        serializer = CategorySerializer(options, many=True)
        return Response(serializer.data)

    def post(self, request):
        name = request.data.pop('name')
        serializer = CategorySerializer(data={'name': name})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StudyDesignOptionsView(APIView):
    def get(self, request):
        options = StudyDesign.objects.all()
        serializer = StudyDesignSerializer(options, many=True)
        return Response(serializer.data)

    def post(self, request):
        design = request.data.pop('design')
        serializer = StudyDesignSerializer(data={'design': design})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RiskOfBiasOptionsView(APIView):
    def get(self, request):
        options = RiskOfBias.objects.all()
        serializer = RiskOfBiasSerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        rob = request.data.pop('rob')
        serializer = RiskOfBiasSerializer(data={'rob': rob})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GradeOptionsView(APIView):
    def get(self, request):
        options = Grade.objects.all()
        serializer = GradeSerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        grade = request.data.pop('grade')
        serializer = GradeSerializer(data={'grade': grade})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParticipantDesignOptionsView(APIView):
    def get(self, request):
        options = ParticipantDesign.objects.all()
        serializer = ParticipantDesignSerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        design = request.data.pop('design')
        serializer = ParticipantDesignSerializer(data={'design': design})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImplementationOptionsView(APIView):
    def get(self, request):
        options = Implementation.objects.all()
        serializer = ImplementationSerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        implementor = request.data.pop('implementor')
        serializer = ImplementationSerializer(data={'implementor': implementor})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestTimeOptionsView(APIView):
    def get(self, request):
        options = TestTime.objects.all()
        serializer = TestTimeSerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        time = request.data.pop('time')
        serializer = TestTimeSerializer(data={'time': time})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class EffectSizeTypeOptionsView(APIView):
    def get(self, request):
        options = EffectSizeType.objects.all()
        serializer = EffectSizeTypeSerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        name = request.data.pop('name')
        serializer = EffectSizeTypeSerializer(data={'name': name})
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DownloadCSV(APIView):
    def get(self, request):
        # Query the database to fetch data
        parameters = request.GET.dict()
        # Create an empty Q object to hold the filters
        study_filters = Q()
        experiment_filters = Q()
        effect_data_filters = Q()
        filter_condition = {}
        # Create field lists which contains the fiels of the tables
        fields_studies = [field.name for field in Study._meta.get_fields()]
        fields_experiments = [field.name for field in Experiment._meta.get_fields()]
        fields_effect_data = [field.name for field in EffectData._meta.get_fields()]
        
        # Go through all studies and find the ones which mactch study fitlers
        for key, value in parameters.items():
            if '__' in key:
                related_field, attribute = key.split('__')
                if related_field in fields_studies:
                    filter_condition = {f"{related_field}__{attribute}": value}
                    study_filters &= Q(**filter_condition)
                
            else:
                if key in fields_studies:
                    filter_condition = {f"{key}": value}
                    study_filters &= Q(**filter_condition)
        
        studies = Study.objects.filter(study_filters)
        study_ids = [study.study_id for study in studies]
        
        # Create filter condition on experiments so only experiment from the filterd studies are filterd
        experiment_filters &= Q(study_id__in=study_ids)
        # Filter through the experiments
        for key, value in parameters.items():
            if '__' in key:
                related_field, attribute = key.split('__')
                if related_field in fields_experiments:
                    filter_condition = {f"{related_field}__{attribute}": value}
                    experiment_filters &= Q(**filter_condition)              
            else:
                if key in fields_experiments:
                    filter_condition = {f"{key}": value}
                    experiment_filters &= Q(**filter_condition)
        experiments = Experiment.objects.filter(experiment_filters)     
        experiment_ids = [experiment.experiment_nr for experiment in experiments]

        # Create filter condition on effekt_data so only effekt_data from the filterd experiments are filterd
        effect_data_filters &= Q(experiment_nr__in=experiment_ids)
        for key, value in parameters.items():
            if '__' in key:
                related_field, attribute = key.split('__')
                if related_field in fields_effect_data:
                    filter_condition = {f"{related_field}__{attribute}": value}
                    effect_data_filters &= Q(**filter_condition)              
            else:
                if key in fields_effect_data:
                    filter_condition = {f"{key}": value}
                    effect_data_filters &= Q(**filter_condition)        
        effect_datas = EffectData.objects.filter(effect_data_filters)

        # Create a CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        # Write data to CSV
        writer = csv.writer(response)
        # Write header row
        writer.writerow(['title','authors', 'keywords', 'abstract', 'category', 'country',  'year', 'DOI', 
                         'peer_reviewed', 'source', 'experiment_number',
                         'test_time', 'effect_size_number', 'intervention', 'intervention_op', 'target_population',
                         'mean_age', 'grade_k', 'grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5',
                         'grade_6', 'grade_7', 'grade_8', 'grade_9', 'grade_10', 'grade_11', 'grade_12',
                         'ni', 'gender_1', 'gender_2', 'gender_3', 'study_design',
                         'participant_design', 'implementation', 'duration_week', 'frequency_n',
                         'intensity_n', 'effect_size_type', 'mean_age_1i', 'm1i', 'sd1i', 'n1i',
                         'mean_age_2i', 'm2i', 'sd2i', 'n2i', 'icc', 'ai', 'bi', 'ci', 'di', 'ri',
                         't', 'f_stat', 'd', 'd_var', 'rob', 'robins', 'outcome', 'test_name',
                         'outcome_full', 'outcome_op'])  # Add column names
      
        # For each effect in effect_datas write a row in the csv file with all variables defined above.
        for effekt_data in effect_datas:
            # Define the paths to the experiment of the effekt_data and the study of that experiment
            experiment = effekt_data.experiment_nr
            study = effekt_data.experiment_nr.study_id
            # Write the rows to the CSV response
            writer.writerow([study.title, study.authors, study.keywords, study.category.name, study.country.name,
                             study.study_year, study.doi, study.peer_reviewed, experiment.source, experiment.experiment_nr,
                             effekt_data.test_time.time, effekt_data.effect_size_number, experiment.intervention, 
                             experiment.intervention_op, experiment.target_population, experiment.mean_age, experiment.grade.k,
                             experiment.grade.first, experiment.grade.second, experiment.grade.third, experiment.grade.forth,
                             experiment.grade.fifth, experiment.grade.sixth, experiment.grade.seventh,
                             experiment.grade.eighth, experiment.grade.ninth, experiment.grade.tenth, 
                             experiment.grade.eleventh, experiment.grade.twelfth,
                             experiment.ni, effekt_data.gender_1, effekt_data.gender_2, effekt_data.gender_3, 
                             experiment.study_design.design, experiment.participant_design.design, experiment.implemented.implementor,
                             experiment.duration_week, experiment.frequency_n, experiment.intensity_n, 
                             effekt_data.effect_size_type.name, effekt_data.mean_age_1i, effekt_data.m1i, effekt_data.sd1i,
                             effekt_data.n1i, effekt_data.mean_age_2i, effekt_data.m2i, effekt_data.sd2i,
                             effekt_data.n2i, effekt_data.icc, effekt_data.ai, effekt_data.bi, effekt_data.ci,
                             effekt_data.di, effekt_data.ri, effekt_data.t, effekt_data.f_stat, effekt_data.d,
                             effekt_data.d_var, experiment.risks.rob, experiment.robins, effekt_data.outcome, 
                             effekt_data.test_name, effekt_data.outcome_full, effekt_data.outcome_op])  

        return response

    
class get_orcid_infoAPIView(APIView):
    def get(self, request):
        return 
    
    def post(self, request):
        code = request.data.get('code')
    
        client_id = 'APP-IZWWE416AT5JC4N6',
        client_secret = '51bd4130-6aad-4777-9102-4755f7a5c01a',
        redirect_uri = 'http://192.168.0.34:3000/Login'

        # Make a request to the ORCID API to get the auth token
        token_url = 'https://orcid.org/oauth/token'
        headers = {'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri
        }
        response = requests.post(token_url, headers=headers, data=data)

        # Check if the request was successful
        if response.status_code == 200:
            json_response = response.json()
            access_token = json_response.get('access_token')
            refresh_token = json_response.get('refresh_token')
            name = json_response.get('name')
            orcid = json_response.get('orcid')
            return Response({'access_token': access_token, 'refresh_token': refresh_token, 'name': name, 'orcid': orcid}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to get auth token', "response": response}, status=status.HTTP_400_BAD_REQUEST)
