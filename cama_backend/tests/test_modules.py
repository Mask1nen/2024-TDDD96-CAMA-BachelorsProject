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
    

