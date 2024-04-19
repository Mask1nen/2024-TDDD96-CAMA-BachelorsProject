import factory
import factory.random
from myapi.models import *
import random as rd
import django
import pytest



# All assignments are incorect, it is temporary data which is under progress
# Aka it is all just copied from the model definitions

# Seed variables
cama_user_seed = None

study_seed = None

experiment_seed = None

effect_data_seed = None

COUNTRY_NAMES = ["Sweden", "England", "Norway", "USA", "Germany"]

CATEGORY_NAMES = ["Math", "Language", "Science"]

CATEGORY_FULL = False




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



@pytest.mark.django_db(transaction=True)
class StudyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Study
        
    factory.random.reseed_random('study')
    rd.seed(factory.random.randgen.getstate())

    uploader = factory.SubFactory(CamaUserFactory)
    study_year = rd.randint(2000, 2024)
    
    @factory.lazy_attribute
    def country(self):
        return Country.objects.get_or_create(name=rd.choice(["Sweden", "England", "Norway", "USA", "Germany"]))[0]
    
    @factory.lazy_attribute
    def category(self):
        return Category.objects.get_or_create(name=rd.choice(["Math", "STEM", "Language"]))[0]

    
    peer_reviewed = True
    authors = factory.SelfAttribute('uploader.name') 
    doi = factory.Sequence(lambda n: f"https://doi.org/10.2{n}07/j.ctt1k85dmc")
    abstract = "This is a amazing abstract which pulls the reader in to the \
                study and makes them want to learn more about it"
    keywords =  f"Interesting, I dont know what to write"
    nr_downloads = factory.LazyAttribute(lambda x: rd.randint(0, 10000)) 

    


class ExperimentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Experiment
        
    study_id = factory.SubFactory(StudyFactory)

    @factory.lazy_attribute
    def study_design(self):
        return StudyDesign.objects.get_or_create(design=rd.choice(["RCT", "QES"]))[0]
    
    
    @factory.lazy_attribute
    def risks(self):
        return RiskOfBias.objects.get_or_create(rob=rd.choice(["low", "moderate", "high"]), robins=rd.choice(["low", "moderate", "high"]) )[0]
    
    
    @factory.lazy_attribute
    def grade(self):
        return Grade.objects.get_or_create(grade=rd.choice(["K", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]))[0]
    
    
    @factory.lazy_attribute
    def participant_design(self):
        return ParticipantDesign.objects.get_or_create(design=rd.choice(["within", "bewteen", "mixed"]))[0]
    
    
    @factory.lazy_attribute
    def implemented(self):
        return Implementation.objects.get_or_create(implementor=rd.choice(["researcher","teacher", "paraprofessional"]))[0]
    
    
    intensity_n = rd.randint(4, 14)
    duration_week = rd.randint(2, 8)
    frequency_n = rd.randint(2, 6)
    
    ni = factory.random.randgen.randint(1, 1000)
    intervention = "The name of the intervention implemented"
    intervention_op = "A short explanation/description of how the intervention was operationalized"
   
    target_population = models.CharField(max_length=255, null=True)
    @factory.lazy_attribute
    def target_population(self):
        return TargetPopulation.objects.get_or_create(target=rd.choice(["Typically developing student", "Disabilities"]))[0]
    
    mean_age = factory.random.randgen.random() * 50 
    source = "The doi to the meta analysis from which the experiment is taken."
                    
                    

    



class EffectDataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EffectData
    
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
    
