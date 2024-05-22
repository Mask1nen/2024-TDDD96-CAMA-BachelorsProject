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
from django.shortcuts import get_object_or_404
from .models import get_id_from_name, FIELD_MODEL_MAP


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
    """StudyView is a apiview which handles gets and posts for the study table.
    """    
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
    """StudyFilterView is a APIViews which handles study get requests with filters
    
    """    
    def get(self, request):
        """Handles get requests whith provided filters in the url

        Arguments:
            request -- the request

        Returns:
            A HTTP request with the data in json format.
        """        
        # Get all the provided parameters from the query string
        parameters = request.GET.dict()
        fields = [field.name for field in Study._meta.get_fields()]
        filters = filter_helper(parameters, fields)
        studies = Study.objects.all().filter(filters)
        serializer = StudySerializer(studies, many=True)
        return Response(serializer.data)
    
    
class ExperimentFilterView(APIView):
    """ExperimentFilterView is a APIViews which handles experiments get requests with filters
    
    """
    def get(self, request):
        """Handles get requests whith provided filters in the url

        Arguments:
            request -- the request

        Returns:
            A HTTP request with the data in json format.
        """
        # Get all the provided parameters from the query string
        parameters = request.GET.dict()
        fields = [field.name for field in Experiment._meta.get_fields()]
        filters = filter_helper(parameters, fields)
        experiments = Experiment.objects.all().filter(filters)
        serializer = ExperimentSerializer(experiments, many=True)
        return Response(serializer.data)
    
class EffectDataFilterView(APIView):
    """EffectDataFilterView is a APIViews which handles effect_data get requests with filters
    
    """
    def get(self, request):
        """Handles get requests whith provided filters in the url

        Arguments:
            request -- the request

        Returns:
            A HTTP response whith the filterd data in json format
        """
        # Get all the provided parameters from the query string
        parameters = request.GET.dict()
        fields = [field.name for field in EffectData._meta.get_fields()]
        filters = filter_helper(parameters, fields)
        effect_data = EffectData.objects.all().filter(filters)
        serializer = EffectDataSerializer(effect_data, many=True)
        return Response(serializer.data)
    
class StudySearchView(APIView):
    """EffectDataFilterView is a APIViews which handles study get requests whith
    provided search filters
    
    """
    def get(self, request):
        """Filters the studys based on the search fileds of author and title
        and provides all studies where the provided text is in the fields.

        Arguments:
            request -- the request

        Returns:
            A HTTP response whith the filterd data in json format
        """        
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
    
    
class get_orcid_infoAPIView(APIView):
    def get(self, request):
        return 
    
    def post(self, request):
        code = request.data.get('code')
    
        client_id = 'APP-IZWWE416AT5JC4N6', ###FIXME replace with your client id
        client_secret = '51bd4130-6aad-4777-9102-4755f7a5c01a', ###FIXME replace with your client secret
        redirect_uri = 'http://192.168.0.34:3000/Login' ###FIXME replace with your redirect uri

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


class StudyViewDetail(APIView):

    @staticmethod
    def get(request, study_id):
        """
        View individual study
        """

        study = get_object_or_404(Study, pk=study_id)
        return Response(StudySerializer(study).data)

    @staticmethod
    def patch(request, study_id):
        """
        Approve study
        """

        study = get_object_or_404(Study, pk=study_id)

        
        # Update the 'approved' field in the instance and all nested tables
        study.approved = True
        for experiment in study.experiments.all():
            experiment.approved = True

            for effect in experiment.effects.all():
                effect.approved = True
                effect.save()
            experiment.save()
        study.save()

        # Serialize the instance to return it in the response
        return Response(StudySerializer(study).data, status=status.HTTP_200_OK)
    
def filter_helper(parameters, fields):
    """A helper functions which creates a Q filter based on the parameters 
    which are provided.

    Arguments:
        parameters -- The parameters provided in the request.
        fields -- The fields which exists in the table.

    Returns:
        A Q filter containing filters based on the provided parameters.
    """    
    filter_container = Q()
    for key, value in parameters.items():
        if key in fields:
            filter_condition = {f"{key}": value}
            filter_container &= Q(**filter_condition)
    return filter_container

class DownloadCSV(APIView):
    def get(self, request):
        parameters = request.GET.dict()

        fields_studies = [field.name for field in Study._meta.get_fields()]
        fields_experiments = [field.name for field in Experiment._meta.get_fields()]
        fields_effect_data = [field.name for field in EffectData._meta.get_fields()]

        # Filter studies
        study_filters = filter_helper(parameters, fields_studies)
        studies = Study.objects.filter(study_filters)
        study_ids = [study.study_id for study in studies]
        print("Filtered Studies:", studies)

        # Filter experiments
        experiment_filters = filter_helper(parameters, fields_experiments)
        experiment_filters &= Q(study_id__in=study_ids)
        experiments = Experiment.objects.filter(experiment_filters)
        experiment_ids = [experiment.experiment_nr for experiment in experiments]
        print("Filtered Experiments:", experiments)

        # Fetch EffectData related to filtered experiments
        effect_datas = EffectData.objects.filter(experiment_nr__in=experiment_ids)
        print("Filtered Effect Data:", effect_datas)

        for experiment in experiments:
            related_effects = EffectData.objects.filter(experiment_nr=experiment.experiment_nr)
            print(f"Experiment {experiment.experiment_nr} has related EffectData: {related_effects}")

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        writer = csv.writer(response)
        writer.writerow(['title', 'authors', 'keywords', 'abstract', 'category', 'country', 'study_year', 'doi', 
                         'peer_reviewed', 'source', 'experiment_number', 'test_time', 'effect_size_number', 
                         'intervention', 'intervention_op', 'target_population', 'mean_age', 'grade_k', 
                         'grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5', 'grade_6', 'grade_7', 
                         'grade_8', 'grade_9', 'grade_10', 'grade_11', 'grade_12', 'ni', 'gender_1', 
                         'gender_2', 'gender_3', 'study_design', 'participant_design', 'implementation', 
                         'duration_week', 'frequency_n', 'intensity_n', 'effect_size_type', 'mean_age_1i', 
                         'm1i', 'sd1i', 'n1i', 'mean_age_2i', 'm2i', 'sd2i', 'n2i', 'icc', 'ai', 'bi', 'ci', 
                         'di', 'ri', 't', 'f_stat', 'd', 'd_var', 'rob', 'robins', 'outcome', 'test_name', 
                         'outcome_full', 'outcome_op'])

        # Write CSV rows
        for effect_data in effect_datas:
            experiment = effect_data.experiment_nr
            study = experiment.study_id
            print("Writing row for Study:", study)
            writer.writerow([
                study.title, study.authors, study.keywords, study.abstract, study.category.name, study.country.name,
                study.study_year, study.doi, study.peer_reviewed, experiment.source, experiment.experiment_nr,
                effect_data.test_time.time, effect_data.effect_size_number, experiment.intervention, 
                experiment.intervention_op, experiment.target_population, experiment.mean_age, experiment.grade.k,
                experiment.grade.first, experiment.grade.second, experiment.grade.third, experiment.grade.fourth,
                experiment.grade.fifth, experiment.grade.sixth, experiment.grade.seventh,
                experiment.grade.eighth, experiment.grade.ninth, experiment.grade.tenth, 
                experiment.grade.eleventh, experiment.grade.twelfth,
                experiment.ni, effect_data.gender_1, effect_data.gender_2, effect_data.gender_3, 
                experiment.study_design.design, experiment.participant_design.design, experiment.implemented.implementor,
                experiment.duration_week, experiment.frequency_n, experiment.intensity_n, 
                effect_data.effect_size_type.name, effect_data.mean_age_1i, effect_data.m1i, effect_data.sd1i,
                effect_data.n1i, effect_data.mean_age_2i, effect_data.m2i, effect_data.sd2i,
                effect_data.n2i, effect_data.icc, effect_data.ai, effect_data.bi, effect_data.ci,
                effect_data.di, effect_data.ri, effect_data.t, effect_data.f_stat, effect_data.d,
                effect_data.d_var, experiment.risks.rob, experiment.robins, effect_data.outcome, 
                effect_data.test_name, effect_data.outcome_full, effect_data.outcome_op
            ])

        return response