from models import *

"""This file contains the integration test of the database and 
its structure through a series of database requests"""

"""User tests"""
def create_user(number_of_users):
    user_list = []
    for id in range(0,5):
        user = User(orc_id=id, name=f"{id}", email=f"{id}@gmail.com", organization=f"{id}", nr_uploads=id)
        user.save()

"""Study tests"""

def create_studies(number_of_studies):
    """ Creates a number of studies and the required objects to create a study
    """
    year1 = Year(year=2024)
    year1.save()
    country = Country(name=f"Sweden")
    country.save()
    category_list = ["Language", "Math", "STEM"]
    for category_id in range(len(category_list)):    
        category = Category(name=category_list[category_id])
        category.save()

    pear_reviewd_list = [True, False]
    for id in range(number_of_studies):
        study = Study(uploader=id, country=country, category=category_list[id%len(category_list)],
                    peer_reviewed=pear_reviewd_list[id%len(pear_reviewd_list)], authors="This, is, a, test, string",
                    doi="https://doi.org/10.2307/j.ctt1k85dmc", abstract="A well written abstract", keywords="Key, words",
                    nr_downloads=id)
        study.save()


"""Experiment test"""

def create_experiment(number_of_experiments):
    s = StudyDesign(design="abc")
    r = RiskOfBias(id=1, rob="abc", robins="abc")
    g = Grade(grade="abc")
    p = ParticipantDesign(design="abc")
    im = Implementation(implementor="abc")
    s.save()
    r.save()
    g.save()
    p.save()
    im.save()
    study_ids = Study.objects.values_list('id')
    for id in range(number_of_experiments):
        s = StudyDesign(design=f"{id}")
        r = RiskOfBias(id=id, rob=f"{id}", robins=f"{id}")
        g = Grade(grade=f"{id}")
        p = ParticipantDesign(design=f"{id}")
        im = Implementation(implementor=f"{id}")
        e = Experiment(study_id=study_ids[id%len[study_ids]], study_design="abc", risks=r, 
                    grade=g, participant_design=p, implemented=im, gender_1=0.5,
                    gender_2=0.5, intensity_n=1, duration_week=1, frequency_n=1, outcome="abc", outcome_full="abc")
        e.save()

"""Effect data tests"""

    
def create_effect_data(number_of_effekts, number_of_existing_studies, number_of_exisiting_experiments):
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
    
    for id in range(number_of_effekts):
        effect_data = EffectData(effect_size_number=id, study_id=id%number_of_existing_studies,
                                 experiment_nr=id%number_of_exisiting_experiments, sd1i=sd1i, sd2i=sd2i, n1i=n1i,
                                 n2i=n2i, m1i=m1i, m2i=m2i, d_var=d_var, d=d, f_stat=f_stat,
                                 t=t, ri=ri, mean_age=mean_age, ni=ni, icc=icc, ai=ai, bi=bi, ci=ci)
        effect_data.save()  

"""All together"""

def create_database(number_of_rows):
    create_user(number_of_rows)
    create_studies(number_of_rows)
    create_experiment(number_of_rows)
    create_effect_data(number_of_rows)


"""Test queries"""
# Check database contains the expected data
def create_queries(number_of_rows):
    for i in range(number_of_rows):
        assert User.objects.filter(orc_id=i) == User(orc_id=i, name=f"{i}", email=f"{i}@gmail.com", organization=f"{i}", nr_uploads=i)

#Test edgecases

"""Test updating"""
# Test updating the exisitng data 

"""Test deleting"""
