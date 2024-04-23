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
        logger.info('bananananan')

        if serializer.is_valid():
            logger.info('banaerärrrrrrrrrrrrrrrrrrr')

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExperimentView(APIView):
    def get(self, request):
        experiments = Experiment.objects.all()
        serializer = ExperimentSerializer(experiments, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ExperimentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
