import pytest
import django
django.setup()
from django.contrib.auth.models import User
from django.core.exceptions import *
from myapi.models import CamaUser
from myapi.models import Country
from myapi.models import Category
from myapi.models import Study
from myapi.models import EffectData, Experiment
from .factories import CamaUserFactory, StudyFactory, ExperimentFactory, EffectDataFactory


@pytest.mark.django_db(transaction=True)
def test_user_user_factory(cama_user_factory):
    size = 10
    user = CamaUserFactory.create_batch(size)
    print(len(user))
    assert len(user) == size
    #for x in user:
    #   print(f'{x.orc_id} : {x.name} : {x.email} : {x.organization} : {x.nr_uploads}')
    #   assert x.name != None
       

@pytest.mark.django_db(transaction=True)
def test_study_factory(study_factory):
    size = 10
    study = StudyFactory.create_batch(size)
    print(len(study))
    assert len(study) == size
    #for x in study:
       # print(f'{x.study_id} : {x.uploader} : {x.study_year} : {x.country.name} : {x.category} : {x.peer_reviewed} : {x.authors} : {x.doi} : {x.abstract} : {x.keywords} : {x.nr_downloads}')
        
       
@pytest.mark.django_db(transaction=True)
def test_experiment_factory(experiment_factory):
    size = 10
    experiemnt = ExperimentFactory.build_batch(size)
    print(len(experiemnt))
    assert len(experiemnt) == size
    #for x in experiemnt:
      # print(f'{x.study_id} : {x.study_design} : {x.risks} : {x.robins} : {x.grade} : {x.participant_design} : {x.implemented} : {x.intensity_n} : {x.duration_week} : {x.frequency_n} : {x.ni} : {x.intervention} : {x.intervention_op} : {x.target_population} : {x.mean_age} : {x.source}')
       
       
@pytest.mark.django_db(transaction=True)
def test_effect_data_factory(effect_data_factory):
    size = 10
    effect_data = EffectDataFactory.create_batch(size)
    print(len(effect_data))
    assert len(effect_data) == size
    #for x in effect_data:
       # print(f'{x.effect_size_number} : {x.experiment_nr} : {x.outcome} : {x.outcome_full} : {x.outcome_op} : {x.gender_1} : {x.gender_2} : {x.gender_3} : {x.d_var} : {x.d} : {x.f_stat} : {x.t} : {x.ri} : {x.icc} : {x.mean_age_1i} : {x.mean_age_2i} : {x.ai} : {x.bi} : {x.ci} : {x.di} : {x.sd1i} : {x.sd2i} : {x.n1i} : {x.n2i} : {x.m1i} : {x.m2i}')
        
        
# @pytest.mark.django_db(transaction=True)
# def test_database_foriegn_key_whith_cascade(effect_data_factory):
#     size = 10
#     effect_data = EffectDataFactory.create_batch(size)
#     assert len(effect_data) == size 
#     for x in effect_data:
#         exp_nr = x.experiment_nr.experiment_nr
#         assert x.experiment_nr != None 
#         study_id = x.experiment_nr.study_id.study_id
#         assert x.experiment_nr.study_id != None 
#         Study.objects.filter(study_id=study_id).delete()
#         with pytest.raises(ObjectDoesNotExist):
#             print(Study.objects.get(study_id=study_id))
#         with pytest.raises(ObjectDoesNotExist):
#             print(EffectData.objects.get(effect_size_number=x.effect_size_number, experiment_nr=x.experiment_nr))
#         with pytest.raises(ObjectDoesNotExist):
#             print(Experiment.objects.get(experiment_nr=exp_nr, study_id=study_id))
         
        
        