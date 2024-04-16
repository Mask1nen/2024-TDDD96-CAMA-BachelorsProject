from django.urls import path
from .views import CamaUserListView, StudyListCreateAPIView

urlpatterns = [
    path('cama-users/', CamaUserListView.as_view(), name='cama_user_list'),
    path('studies/', StudyListCreateAPIView.as_view(), name='study-list-create'),
]
