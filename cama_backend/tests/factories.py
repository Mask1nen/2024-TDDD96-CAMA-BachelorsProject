import factory
import factory.random
from myapi.models import *
import random as rd


# All assignments are incorect, it is temporary data which is under progress
# Aka it is all just copied from the model definitions

# Seed variables
cama_user_seed = None

study_seed = None

experiment_seed = None

effect_data_seed = None

COUNTRY_NAMES = ["Sweden", "England", "Norway", "USA", "Germany"]

CATEGORY_NAMES = ["Math", "Language", "Science"]




factory.random.randgen 
class CamaUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CamaUser
    # ressed_random takes a parameter and creates a "random" sequense from the int value of the parameter
    factory.random.reseed_random('orc_id')
    orc_id = factory.sequence(lambda n: n)
    name = factory.Faker('first_name')
    email = factory.Sequence(lambda n: f'test.mail{n}@gmail.com')
    organization = factory.Sequence(lambda n: f'organization{n}')
    nr_uploads = int() # Either make random or just have a static number for all


class StudyYearFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Year   
    study_year =  2024
    
class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country
    rd.seed('country')
    name = rd.choice(["Sweden", "England", "Norway", "USA", "Germany"])
    
    
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    rd.seed('category')
    name = "Math"


class StudyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Study
    factory.random.reseed_random('study')
    rd.seed(factory.random.randgen.getstate())
    
    uploader = factory.SubFactory(CamaUserFactory)
    study_year = Year(study_year=2024) 
    country = factory.Faker('country')
    study_year = rd.randint(2000, 2024)
    category = factory.Iterator(["Math", "STEM", "Language"])

    @classmethod
    def create(cls, **kwargs):
        country = kwargs.pop('country', None)
        study_year = kwargs.pop('study_year', None)
        category = kwargs.pop('category', None)
        if country:
            # Check if a Country with the provided name exists
            country, created = Country.objects.get_or_create(name=country)
            kwargs['country'] = country
        
    
        if study_year:
            # Check if a Year with the provided value exists
            year, created = Year.objects.get_or_create(study_year=study_year)
            kwargs['study_year'] = year
            
        if category:
            # Check if a Category with the provided name exists
            category, created = Category.objects.get_or_create(name=category)
            kwargs['category'] = category

        return super().create(**kwargs)
    
    
    peer_reviewed = True
    authors = factory.SelfAttribute('uploader.name') 
    doi = factory.Sequence(lambda n: f"https://doi.org/10.2{n}07/j.ctt1k85dmc")
    abstract = "This is a amazing abstract which pulls the reader in to the \
                study and makes them want to learn more about it"
    keywords =  f"Interesting, I dont know what to write"
    nr_downloads = factory.LazyAttribute(lambda x: rd.randint(0, 10000)) 

class StudyDesignFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StudyDesign
    rd.seed('study_design')
    
    design = rd.choice(["RCT", "QES"])


class RiskOfBiasFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RiskOfBias
    rd.seed('risk')
    rob = rd.choice(["low", "moderate", "high"])
    robins = rd.choice(["low", "moderate", "high"])


class GradeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Grade
    rd.seed('grade')
    
    grade = rd.choice(["K", "1", "2", "3", "4", "5", "6", \
                        "7", "8", "9", "10", "11", "12"])


class ParticipantDesignFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ParticipantDesign
    rd.seed('participant_design')
    design = rd.choice(["within", "between", "mixed"])


class ImplementationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Implementation
    rd.seed('implementation')
    implementor = rd.choice(["researcher", "teacher", "paraprofessional"])
    


class ExperimentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Experiment
    study_id = factory.SubFactory(StudyFactory)
    study_design = StudyDesign(design="RCT") #factory.SubFactory(StudyDesignFactory)
    risks = RiskOfBias(rob="moderate", robins="low")#factory.SubFactory(RiskOfBiasFactory) 
    grade = Grade("5") #factory.SubFactory(GradeFactory)
    participant_design = ParticipantDesign("between") #factory.SubFactory(ParticipantDesignFactory)
    implemented = Implementation("reasercher") #factory.SubFactory(ImplementationFactory)
    
    rd.seed('gender')
    gender_1 = rd.random()
    gender_2 = 1 - gender_1
    
    intensity_n = rd.randint(4, 14)
    duration_week = rd.randint(2, 8)
    frequency_n = rd.randint(2, 6)
    outcome = "The outcome of the experiment"
    outcome_full = "The complete outcome of the experiemnt which \
                    means that it will be longer then the rest"



class EffectDataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EffectData
    
    study_id = factory.SubFactory(StudyYearFactory)
    experiment_nr = factory.SubFactory(ExperimentFactory)
    

    sd1i = rd.random() * 10 
    sd2i = rd.random() * 10  
    n1i = rd.random() * 100  
    n2i = rd.random() * 100
    m1i = rd.random() * 10 
    m2i = rd.random() * 10 
    d_var = rd.random() * 100 
    d = rd.random() * 100 
    f_stat = rd.random() * 50 
    t = rd.random() * 100 
    ri = rd.random() * 50 
    mean_age = rd.random() * 50 
    ni = rd.random() * 50 
    icc = rd.random() * 30 
    ai = rd.random() * 50
    bi = rd.random() * 50 
    ci = rd.random() * 50 
    di = rd.random() * 50 
    
