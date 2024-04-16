from django.urls import path
from .views import CamaUserListView

urlpatterns = [
    path('cama-users/', CamaUserListView.as_view(), name='cama_user_list'),
]
