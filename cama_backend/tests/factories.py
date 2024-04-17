import factory
import factory.random
from myapi.models import *
import random as rd


# All assignments are incorect, it is temporary data which is under progress
# Aka it is all just copied from the model definitions

# Seed variables
year_seed = None
country_seed = None
category_seed = None
study_design_seed = None
risk_of_bias_seed = None
grade_seed = None



class CamaUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CamaUser
    # ressed_random takes a parameter and creates a "random" sequense from the int value of the parameter
    orc_id = factory.random.reseed_random('orc_id')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    name = f"{first_name} {last_name}"
    email_later = factory.Sequence(lambda n: f'test.mail{n}@gmail.com')
    organization = factory.Sequence(lambda n: f'organization{n}')
    nr_uploads = int() # Either make random or just have a static number for all


class StudyYearFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Year
    if not year_seed:
        rd.seed('year')
    else:
        rd.setstate(year_seed)
    study_year = rd.choice([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
    year_seed = rd.getstate()
    
class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country
    rd.seed('country')
    name = rd.choice(["Sweden", "England", "Norway", "USA", "Germany"])
    
    
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    rd.seed('category')
    name = rd.choice(["Math", "STEM", "Language"])


class StudyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Study
    study_id = models.AutoField(primary_key=True)
    
    uploader = factory.SubFactory(CamaUserFactory)
    study_year = factory.SubFactory(StudyYearFactory)
    country = factory.SubFactory(CountryFactory)
    category = factory.SubFactory(CategoryFactory)
    
    peer_reviewed = True
    authors = f'{uploader.name}'
    doi = factory.Sequence(lambda n: f"https://doi.org/10.2{n}07/j.ctt1k85dmc")
    abstract = "This is a amazing abstract which pulls the reader in to the \
                study and makes them want to learn more about it"
    keywords = f"Interesting, {category.name}, I dont know what to write"
    nr_downloads = 0
    

class StudyDesignFactory(models.Model):
    rd.seed('study_design')
    design = rd.choice(["RCT", "QES"])


class RiskOfBiasFactory(models.Model):
    rd.seed('risk')
    rob = rd.choice(["low", "moderate", "high"])
    robins = rd.choice(["low", "moderate", "high"])


class GradeFactory(models.Model):
    rd.seed('grade')
    
    grade = rd.choice(["K", "1", "2", "3", "4", "5", "6", \
                        "7", "8", "9", "10", "11", "12"])


class ParticipantDesignFactory(models.Model):
    rd.seed('participant_design')
    design = rd.choice(["within", "between", "mixed"])


class ImplementationFactory(models.Model):
    rd.seed('implementation')
    implementor = rd.choice(["researcher", "teacher", "paraprofessional"])
    


class ExperimentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        
    study_id = factory.SubFactory(StudyYearFactory)
    
    study_design = factory.SubFactory(StudyDesignFactory)
    risks = factory.SubFactory(RiskOfBiasFactory)
    grade = factory.SubFactory(GradeFactory)
    participant_design = factory.SubFactory(ParticipantDesignFactory)
    implemented = factory.SubFactory(ImplementationFactory)
    
    rd.seed('gender')
    gender_1 = rd.random()
    gender_2 = 1 - gender_1
    
    intensity_n = 60
    duration_week = 6
    frequency_n = 3
    outcome = "The outcome of the experiment"
    outcome_full = "The complete outcome of the experiemnt which \
                    means that it will be longer then the rest"



class EffectDataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EffectData
    
    study_id = factory.SubFactory(StudyYearFactory)
    experiment_nr = factory.SubFactory(ExperimentFactory)

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
    