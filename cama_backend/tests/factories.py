# import factory
# import factory.random
# import factory.fuzzy
# from myapi.models import *
# import random as rd
# import django
# import pytest



# # All assignments are incorect, it is temporary data which is under progress
# # Aka it is all just copied from the model definitions

# factory.random.randgen 
# class CamaUserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = CamaUser
#     # ressed_random takes a parameter and creates a "random" sequense from the int value of the parameter
#     factory.random.reseed_random('orc_id')
#     orc_id = factory.sequence(lambda n: n)
#     name = factory.Faker('first_name')
#     email = factory.Sequence(lambda n: f'test.mail{n}@gmail.com')
#     organization = factory.Sequence(lambda n: f'organization{n}')
#     nr_uploads = factory.fuzzy.FuzzyInteger(1, 10000) 


# @pytest.mark.django_db(transaction=True)
# class StudyFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Study
        
#     title = "This is a example title which is extremely captivating"
#     uploader = factory.SubFactory(CamaUserFactory)
#     study_year = factory.fuzzy.FuzzyInteger(2000, 2024)
    
#     @factory.lazy_attribute
#     def country(self):
#         return Country.objects.get_or_create(name=factory.fuzzy.FuzzyChoice(["Sweden", "England", "Norway", "USA", "Germany"]))[0]
    
#     @factory.lazy_attribute
#     def category(self):
#         return Category.objects.get_or_create(name=factory.fuzzy.FuzzyChoice(["Math", "STEM", "Language"]))[0]

    
#     peer_reviewed = True
#     authors = factory.SelfAttribute('uploader.name') 
#     doi = factory.Sequence(lambda n: f"https://doi.org/10.2{n}07/j.ctt1k85dmc")
#     abstract = "This is a amazing abstract which pulls the reader in to the \
#                 study and makes them want to learn more about it"
#     keywords =  f"Interesting, I dont know what to write"
#     nr_downloads = factory.fuzzy.FuzzyInteger(0, 10000)


# class ExperimentFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Experiment
        
#     study_id = factory.SubFactory(StudyFactory)

#     @factory.lazy_attribute
#     def study_design(self):
#         return StudyDesign.objects.get_or_create(design=factory.fuzzy.FuzzyChoice(["RCT", "QES"]))[0]
    
    
#     @factory.lazy_attribute
#     def risks(self):
#         return RiskOfBias.objects.get_or_create(rob=factory.fuzzy.FuzzyChoice(["low", "moderate", "high"]), robins=factory.fuzzy.FuzzyChoice(["low", "moderate", "high"]) )[0]
    
    
#     @factory.lazy_attribute
#     def grade(self):
#         return Grade.objects.get_or_create(grade=factory.fuzzy.FuzzyChoice(["K", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]))[0]
    
    
#     @factory.lazy_attribute
#     def participant_design(self):
#         return ParticipantDesign.objects.get_or_create(design=factory.fuzzy.FuzzyChoice(["within", "bewteen", "mixed"]))[0]
    
    
#     @factory.lazy_attribute
#     def implemented(self):
#         return Implementation.objects.get_or_create(implementor=factory.fuzzy.FuzzyChoice(["researcher","teacher", "paraprofessional"]))[0]
    
    
#     intensity_n = factory.fuzzy.FuzzyInteger(4, 14) 
#     duration_week = factory.fuzzy.FuzzyInteger(2, 8) 
#     frequency_n = factory.fuzzy.FuzzyInteger(2, 6) 
    
#     ni = factory.fuzzy.FuzzyInteger(1, 1000)
#     intervention = "The name of the intervention implemented"
#     intervention_op = "A short explanation/description of how the intervention was operationalized"
   
#     @factory.lazy_attribute
#     def target_population(self):
#         return TargetPopulation.objects.get_or_create(target=factory.fuzzy.FuzzyChoice(["Typically developing student", "Disabilities"]))[0]
    
#     mean_age = factory.fuzzy.FuzzyFloat(5, 50) 
#     source = "The doi to the meta analysis from which the experiment is taken."
                    

# class EffectDataFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = EffectData
    
#     factory.random.reseed_random('effect_data')
    
#     experiment_nr = factory.SubFactory(ExperimentFactory)
    
#     @factory.lazy_attribute
#     def effect_size_type(self):
#         return EffectSizeType.objects.get_or_create(name=rd.choice(["SMD","RR/OR"]))[0]
    
#     @factory.lazy_attribute
#     def test_time(self):
#         return TestTime.objects.get_or_create(time=rd.choice(["pre-test", "post-test", "follow-up"]))[0]
    
#     test_name = "This is the name of the test used to measure the outcome"
    
#     outcome = "Machine readable"
#     outcome_full = "Full name of the outcome as stated in the study"
#     outcome_op = "Short explanation/discription of how the outcome was operationalized"
    
#     gender_1 = factory.fuzzy.FuzzyInteger(1, 1000) 
#     gender_2 = factory.fuzzy.FuzzyInteger(1, 1000)
#     gender_3 = factory.fuzzy.FuzzyInteger(1, 1000)

#     sd1i = factory.fuzzy.FuzzyFloat(1, 100) 
#     sd2i = factory.fuzzy.FuzzyFloat(1, 100)  
#     n1i = factory.fuzzy.FuzzyFloat(1, 100)  
#     n2i = factory.fuzzy.FuzzyFloat(1, 100)
#     m1i = factory.fuzzy.FuzzyFloat(1, 100) 
#     m2i = factory.fuzzy.FuzzyFloat(1, 100) 
#     d_var = factory.fuzzy.FuzzyFloat(1, 100) 
#     d = factory.fuzzy.FuzzyFloat(1, 100) 
#     f_stat = factory.fuzzy.FuzzyFloat(1, 100) 
#     t = factory.fuzzy.FuzzyFloat(1, 100) 
#     ri = factory.fuzzy.FuzzyFloat(1, 100)
#     mean_age_1i = factory.fuzzy.FuzzyFloat(1, 100)
#     mean_age_2i = factory.fuzzy.FuzzyFloat(1, 100)
#     icc = factory.fuzzy.FuzzyFloat(1, 100) 
    
#     ai = factory.fuzzy.FuzzyInteger(1, 100)
#     bi = factory.fuzzy.FuzzyInteger(1, 100)
#     ci = factory.fuzzy.FuzzyInteger(1, 100)
#     di = factory.fuzzy.FuzzyInteger(1, 100)
    
