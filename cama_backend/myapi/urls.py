from django.urls import path
from .views import CamaUserView, StudyView, ExperimentView, EffectDataView, get_orcid_infoAPIView, \
                CountryOptionsView, CategoryOptionsView, StudyDesignOptionsView, RiskOfBiasOptionsView, ParticipantDesignOptionsView, \
                ImplementationOptionsView, TestTimeOptionsView, EffectSizeTypeOptionsView        

urlpatterns = [
    path('cama-users/', CamaUserView.as_view(), name='cama_users'),
    path('studies/', StudyView.as_view(), name='studies'),
    path('experiments/', ExperimentView.as_view(), name='experiments'),
    path('effect-data/', EffectDataView.as_view(), name='effect_data'),
    path('populate-country/', CountryOptionsView.as_view(), name='populate-country'),
    path('populate-category/', CategoryOptionsView.as_view(), name='populate-category'),
    path('populate-study_design/', StudyDesignOptionsView.as_view(), name='populate_stud'),
    path('populate-risk-of-bias/', RiskOfBiasOptionsView.as_view(), name='populate-risk-of-bias'),
    path('populate-participant-design/', ParticipantDesignOptionsView.as_view(), name='populate-participant-design'),
    path('populate-implementation/', ImplementationOptionsView.as_view(), name='populate-implementation'),
    path('populate-test-time/', TestTimeOptionsView.as_view(), name='populate-test-time'),
    path('populate-effect-size-type/', EffectSizeTypeOptionsView.as_view(), name='populate-effect-size-type'),
    path('get-orcid-info/', get_orcid_infoAPIView.as_view(), name='get_orcid_info')
    ]
