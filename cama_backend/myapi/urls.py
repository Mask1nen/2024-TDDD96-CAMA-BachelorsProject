from django.urls import path
from .views import CamaUserView, StudyView, ExperimentView, EffectDataView, StudyDetailView

urlpatterns = [
    path('cama-users/', CamaUserView.as_view(), name='cama_users'),
    path('studies/', StudyView.as_view(), name='studies'),
    path('studies/<int:id>/', StudyDetailView.as_view(), name='study_detail'),
    path('experiments/', ExperimentView.as_view(), name='experiments'),
    path('effect-data/', EffectDataView.as_view(), name='effect_data'),
    
]
