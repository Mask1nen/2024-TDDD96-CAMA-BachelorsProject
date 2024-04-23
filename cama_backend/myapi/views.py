from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import CamaUser, Experiment, Study, EffectData
from .serializers import CamaUserSerializer, StudySerializer, ExperimentSerializer

import logging
logger = logging.getLogger(__name__)

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
        
        # Return errors if the data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudyView(APIView):
    def get(self, request):
        study = Study.objects.all()
        serializer = StudySerializer(study, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExperimentView(APIView):
    def get(self, request):
        experiments = Experiment.objects.all()
        serializer = ExperimentSerializer(experiments, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        
        # Handle nested Study data
        study_data = data.get('study_id')
        if study_data:
            # Handle nested CamaUser data within Study data
            camauser_data = study_data.get('uploader')
            if camauser_data:
                # Try to find an existing CamaUser instance or create a new one
                camauser_instance, created = CamaUser.objects.get_or_create(
                    orc_id=camauser_data['orc_id'],
                    defaults=camauser_data
                )
                # Assign the CamaUser instance to the study_data
                study_data['uploader'] = camauser_instance
            
            # Try to find an existing Study instance or create a new one
            study_instance, created = Study.objects.get_or_create(
                # Define fields for matching the existing instance or creating a new one
                uploader=study_data['uploader'],
                study_year=study_data['study_year'],
                country=study_data['country'],
                category=study_data['category'],
                defaults=study_data
            )
            # Assign the Study instance ID to the data dictionary
            data['study_id'] = study_instance.id
        
        # Serialize the data and create an Experiment instance
        serializer = ExperimentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Return errors if the data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExperimentListCreateAPIView(APIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    
'''class EffectDataView(APIView):
    def get(self, request):
        effect_data = EffectData.objects.all()
        serializer = EffectDataSerializer(effect_data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EffectDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''
