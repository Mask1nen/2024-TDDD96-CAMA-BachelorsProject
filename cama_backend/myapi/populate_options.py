import django
from myapi.study import Country, Category
from myapi.experiment import StudyDesign, RiskOfBias, ParticipantDesign, Implementation
from myapi.effect_data import TestTime, EffectSizeType
from django.core.exceptions import *
 
""" To populate options tabels add the following lines to the end of the operations list in 
class Migration(migrations.Migration): 
in the migration file 

migrations.RunPython(
            code=populate_option_tables,
            reverse_code=migrations.RunPython.noop
            ),
            
and add the 
from myapi.populate_options import populate_option_tables
import at the top
"""

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
        count = Country(name=country)
        count.save()
            
    
def populate_category():
    options = ['Language', 'STEM', 'Math', 'Other']
    for option in options:
        category = Category(name=option)
        category.save()

def populate_study_design():
    options = ['RCT', 'QES']
    for option in options:
        study_design = StudyDesign(design=option)
        study_design.save()

def populate_risk_of_bias():
    options = ['low', 'moderate', 'high', 'N/A']
    for option in options:
        risk_of_bias = RiskOfBias(rob=option)
        risk_of_bias.save()

def populate_participant_design():
    options = ['within', 'between', 'mixed']
    for option in options:
        participant_design = ParticipantDesign(design=option)
        participant_design.save()

def populate_implementation():
    options = ['researcher', 'teacher', 'paraprofessional']
    for option in options:
        implementation = Implementation(implementor=option)
        implementation.save()

def populate_test_time():
    options = ['baseline(pre-test)', 'post-test', 'follow-up']
    for option in options:
        test_time = TestTime(time=option)
        test_time.save()

def populate_effect_size_type():
    options = ['SMD', 'RR/OR']
    for option in options:
        effect_size_type = EffectSizeType(name=option)
        effect_size_type.save()
            
def populate_option_tables(apps, schema_editor):
    populate_category()
    populate_country()
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
    
