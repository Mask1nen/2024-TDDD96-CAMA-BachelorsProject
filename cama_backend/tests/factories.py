import factory
import factory.random
from myapi.models import *


class CamaUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CamaUser
    orc_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    organization = models.CharField(max_length=255, null=True)
    nr_uploads = models.IntegerField(null=True)


class StudyYearFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Year
    study_year = models.IntegerField(primary_key=True, serialize=True)
    
    
class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country
    name = models.CharField(primary_key=True, max_length=255)
    
    
class Category(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = models.CharField(primary_key=True, max_length=255)


class StudyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Study
    study_id = models.AutoField(primary_key=True)
    uploader = models.ForeignKey(CamaUser, null=True, on_delete=models.SET_NULL)
    study_year = models.ForeignKey(Year, null=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    peer_reviewed = models.BooleanField(null=True)
    authors = models.CharField(max_length=255, null=True)
    doi = models.CharField(max_length=255, null=True)
    abstract = models.CharField(max_length=255, null=True)
    keywords = models.CharField(max_length=255, null=True)
    nr_downloads = models.CharField(max_length=255, null=True)



class EffectDataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EffectData
    
    effect_size_number = models.AutoField(primary_key=True)
    study_id = models.ForeignKey(Study, on_delete=models.CASCADE)
    experiment_nr = models.ForeignKey(Experiment, on_delete=models.CASCADE)

    sd1i = 3.2132
    sd2i = 3.2132 
    n1i = 22.213
    n2i = 21.213
    m1i = 4.0011
    m2i = 4.0201
    d_var = 21.321
    d = 32.1231
    f_stat = 12.123
    t = 42.213
    ri = 23.123
    mean_age = 22
    ni = 21.32
    icc = 12.42
    ai = 14
    bi = 54
    ci = 12
    di = None
    