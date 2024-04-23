from models import *
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

def populate_grade():
    options = ['K', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
               'K-1', 'K-2', 'K-3', 'K-4', 'K-5', 'K-6', 'K-7', 'K-8', 'K-9', 'K-10', 'K-11', 'K-12',
               '1-2', '1-3', '1-4', '1-5', '1-6', '1-7', '1-8', '1-9', '1-10', '1-11', '1-12',
               '2-3', '2-4', '2-5', '2-6', '2-7', '2-8', '2-9', '2-10', '2-11', '2-12',
               '3-4', '3-5', '3-6', '3-7', '3-8', '3-9', '3-10', '3-11', '3-12',
               '4-5', '4-6', '4-7', '4-8', '4-9', '4-10', '4-11', '4-12',
               '5-6', '5-7', '5-8', '5-9', '5-10', '5-11', '5-12',
               '6-7', '6-8', '6-9', '6-10', '6-11', '6-12',
               '7-8', '7-9', '7-10', '7-11', '7-12',
               '8-9', '8-10', '8-11', '8-12',
               '9-10', '9-11', '9-12',
               '10-11', '10-12',
               '11-12']
    for option in options:
        try:
            Grade.objects.get(grade=option)
        except ObjectDoesNotExist:
            Grade(grade=option).save()

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
    populate_grade()
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
    delete_table_options(Grade)
    delete_table_options(ParticipantDesign)
    delete_table_options(Implementation)
    delete_table_options(TestTime)
    delete_table_options(EffectSizeType)