from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CamaUser
from .serializers import CamaUserSerializer

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


from rest_framework.generics import ListCreateAPIView
from .models import Study
from .serializers import StudySerializer

class StudyListCreateAPIView(ListCreateAPIView):
    queryset = Study.objects.all()
    serializer_class = StudySerializer