from django.urls import path
from cama_backend import urls
from .views import CamaUserView, StudyView, ExperimentView #EffectDataView

urlpatterns = [

    path('cama-users/', CamaUserView.as_view(), name='cama_user-list-create'),
    path('studies/', StudyView.as_view(), name='study-list-create'),
    path('experiments/', ExperimentView.as_view(), name='experiment-list-create'),
    #path('effect-data/', EffectDataView.as_view(), name='effect_data-list-create'),
]
