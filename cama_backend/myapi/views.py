import requests
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import CamaUser, Experiment, Study
from .serializers import CamaUserSerializer, StudySerializer, ExperimentSerializer

import logging
logger = logging.getLogger(__name__)


class CamaUserListView(APIView):
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



'''class StudyListCreateAPIView(generics.ListCreateAPIView):
    logger.info("bye")
    queryset = Study.objects.all()
    serializer_class = StudySerializer'''

class StudyListCreateAPIView(APIView):
 
    def get(self, request):
        studies = Study.objects.all()
        serializer = StudySerializer(studies, many=True)
        return Response(serializer.data)

    def post(self, request):
        study_data = request.data.pop('study_data')
        serializer = StudySerializer(data=study_data)
        logger.info(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExperimentListCreateAPIView(APIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    

class ExperimentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    
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