from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers.cama_user import *
from .serializers.study import *
from .serializers.experiment import *
from .serializers.effect_data import *
from django.shortcuts import get_object_or_404

import logging
logger = logging.getLogger(__name__)

class CamaUserView(APIView):
    def get(self, request):
        cama_users = CamaUser.objects.all()
        serializer = CamaUserSerializer(cama_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CamaUserSerializer(data=request.data)
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
        serializer = CountrySerializer(data=name)
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryOptionsView(APIView):
    def get(self, request):
        options = Category.objects.all()
        serializer = CategorySerializer()

    def post(self, request):
        name = request.data.pop('name')
        serializer = CategorySerializer(data=name)
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
        serializer = StudyDesignSerializer(data=design)
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
        serializer = RiskOfBiasSerializer(data=rob)
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
        serializer = GradeSerializer(data=grade)
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
        serializer = ParticipantDesign(data=design)
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
        serializer = Implementation(data=implementor)
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
        serializer = TestTimeSerializer(data=time)
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
        serializer = EffectSizeTypeSerializer(data=name)
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