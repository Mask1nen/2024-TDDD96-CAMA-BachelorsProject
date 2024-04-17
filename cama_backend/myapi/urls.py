from django.urls import path
from .views import CamaUserListView, StudyListCreateAPIView, ExperimentListCreateAPIView, ExperimentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('cama-users/', CamaUserListView.as_view(), name='cama_user_list'),
    path('studies/', StudyListCreateAPIView.as_view(), name='study-list-create'),
    path('experiments/', ExperimentListCreateAPIView.as_view(), name='experiment-list-create'),
    path('experiments/<int:pk>/', ExperimentRetrieveUpdateDestroyAPIView.as_view(), name='experiment-detail'),
]
