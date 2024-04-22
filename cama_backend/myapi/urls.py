from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('get-orcid-info/', views.get_orcid_info, name='get_orcid_info'),
]