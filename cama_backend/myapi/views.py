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