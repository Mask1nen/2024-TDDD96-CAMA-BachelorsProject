import pytest
import django
django.setup()
from django.contrib.auth.models import User
from myapi.models import CamaUser
from myapi.models import Country
from myapi.models import Category
from myapi.models import Study
from myapi.models import EffectData
from .factories import CamaUserFactory, StudyFactory, ExperimentFactory, EffectDataFactory
'''
pytestmark = pytest.mark.django_db # Mark all functions to require database access.
@pytest.mark.django_db(Transaction = True) # Mark a function to require transaction access to database
'''

@pytest.mark.django_db
def test_studyuser():
    user = CamaUser(orc_id="1", name="name", email="email", organization="org", nr_uploads=1)
    study_year = Year(study_year=1998)
    study_country = Country(name="sweden")
    study_category = Category(name="idk")
    study = Study(study_id=1, uploader=user,study_year=study_year, country=study_country, category=study_category,
                  peer_reviewed = True, authors = "123", doi="123", abstract="123", keywords="123", nr_downloads="123")
    assert study.get_uploader() == "1"
    

@pytest.mark.django_db(transaction=True)
def test_user_user_factory(cama_user_factory):
   user = CamaUserFactory.create_batch(10)
   print(len(user))
   assert len(user) == 10
   for x in user:
       print(f'{x.orc_id} : {x.name} : {x.email} : {x.organization} : {x.nr_uploads}')
       assert x.name != None
       

@pytest.mark.django_db(transaction=True)
def test_study_factory(study_factory):
    study = StudyFactory.create_batch(10)
    print(len(study))
    assert len(study) == 10
    for x in study:
        print(f'{x.study_id} : {x.uploader} : {x.study_year} : {x.country} : {x.category} : {x.peer_reviewed} : {x.authors} : {x.doi} : {x.abstract} : {x.keywords} : {x.nr_downloads}')
        
       
@pytest.mark.django_db(transaction=True)
def test_experiment_factory(experiment_factory):
   experiemnt = ExperimentFactory.build_batch(10)
   print(len(experiemnt))
   assert len(experiemnt) == 10
   for x in experiemnt:
       print(f'{x.study_id} : {x.study_design} : {x.risks} : {x.grade} : {x.participant_design} : {x.implemented} : {x.intensity_n} : {x.duration_week} : {x.frequency_n} : {x.ni} : {x.intervention} : {x.intervention_op} : {x.target_population} : {x.mean_age} : {x.source}')
       
       
@pytest.mark.django_db(transaction=True)
def test_effect_data_factory(effect_data_factory):
   effect_data = EffectDataFactory.create_batch(10)
   print(len(effect_data))
   assert len(effect_data) == 10
   for x in effect_data:
       print(f'{x.effect_size_number} : {x.experiment_nr} : {x.outcome} : {x.outcome_full} : {x.outcome_op} : {x.gender_1} : {x.gender_2} : {x.gender_3} : {x.d_var} : {x.d} : {x.f_stat} : {x.t} : {x.ri} : {x.icc} : {x.mean_age_1i} : {x.mean_age_2i} : {x.ai} : {x.bi} : {x.ci} : {x.di} : {x.sd1i} : {x.sd2i} : {x.n1i} : {x.n2i} : {x.m1i} : {x.m2i}')
       