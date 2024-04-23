import django
from myapi.study import Country, Category
from myapi.experiment import StudyDesign, RiskOfBias, ParticipantDesign, Implementation
from myapi.effect_data import TestTime, EffectSizeType
from django.core.exceptions import *
 

def populate_country():
    european_countries = [
    "Albania", 
    "Andorra",
    "Austria",
    "Belarus",
    "Belgium",
    "Bosnia and Herzegovina",
    "Bulgaria",
    "Croatia",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "Iceland",
    "Ireland",
    "Italy",
    "Kosovo",
    "Latvia",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Moldova",
    "Monaco",
    "Montenegro",
    "Netherlands",
    "North Macedonia",
    "Norway",
    "Poland",
    "Portugal",
    "Romania",
    "Russia",
    "San Marino",
    "Serbia",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "Switzerland",
    "Ukraine",
    "United Kingdom",
    "Vatican City"]
    for country in european_countries:
        try:
            Country.objects.get(name=country)
        except ObjectDoesNotExist:
            Country(name=country).save()
            
    
def populate_category():
    options = ['Language', 'STEM', 'Math', 'Other']
    for option in options:
        try:
            Category.objects.get(name=option)
        except ObjectDoesNotExist:
            Category(name=option).save()

def populate_study_design():
    options = ['RCT', 'QES']
    for option in options:
        try:
            StudyDesign.objects.get(design=option)
        except ObjectDoesNotExist:
            StudyDesign(design=option).save()

def populate_risk_of_bias():
    options = ['low', 'moderate', 'high', 'N/A']
    for option in options:
        try:
            RiskOfBias.objects.get(rob=option)
        except ObjectDoesNotExist:
            RiskOfBias(rob=option).save()

def populate_participant_design():
    options = ['within', 'between', 'mixed']
    for option in options:
        try:
            ParticipantDesign.objects.get(design=option)
        except ObjectDoesNotExist:
            ParticipantDesign(design=option).save()

def populate_implementation():
    options = ['researcher', 'teacher', 'paraprofessional']
    for option in options:
        try:
            Implementation.objects.get(implementor=option)
        except ObjectDoesNotExist:
            Implementation(implementor=option).save()

def populate_test_time():
    options = ['baseline(pre-test)', 'post-test', 'follow-up']
    for option in options:
        try:
            TestTime.objects.get(time=option)
        except ObjectDoesNotExist:
            TestTime(time=option).save()

def populate_effect_size_type():
    options = ['SMD', 'RR/OR']
    for option in options:
        try:
            EffectSizeType.objects.get(type=option)
        except ObjectDoesNotExist:
            EffectSizeType(type=option).save()
            
def populate_option_tables():
    populate_category()
    populate_category()
    populate_risk_of_bias()
    populate_study_design()
    populate_participant_design()
    populate_implementation()
    populate_test_time()
    populate_effect_size_type()
    
    
def delete_table_options(table):
    for object in table.objects.all():
        object.delete()
        
def delete_all_options():
    delete_table_options(Country)
    delete_table_options(Category)
    delete_table_options(RiskOfBias)
    delete_table_options(StudyDesign)
    delete_table_options(ParticipantDesign)
    delete_table_options(Implementation)
    delete_table_options(TestTime)
    delete_table_options(EffectSizeType)
    
populate_option_tables()