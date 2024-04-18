from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import CamaUser, Experiment, Study
from .serializers import CamaUserSerializer, StudySerializer, ExperimentSerializer

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



class StudyListCreateAPIView(APIView):
    def get(self, request):
        study = Study.objects.all()
        serializer = ExperimentSerializer(study, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExperimentListCreateAPIView(APIView):
    def get(self, request):
        experiment = Experiment.objects.all()
        serializer = ExperimentSerializer(experiment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExperimentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ExperimentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
