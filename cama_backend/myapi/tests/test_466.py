from models import *


"""This file contains the integration test of the database and 
its structure through a series of database requests"""

pear_reviewd_list = []
category_list = []
user_test_list = []
study_test_list = []
experiment_test_list = []
effect_data_test_list = []


"""User tests"""
def create_user(number_of_users):
    """ Creates a number of users

    Arguments:
        number_of_users -- the number of rows of users added to the database
    """    
    user_list = []
    for id in range(number_of_users):
        user = User(orc_id=id, name=f"{id}", email=f"{id}@gmail.com", organization=f"{id}", nr_uploads=id)
        user.save()

        user_test_list.append(user.orc_id)

"""Study tests"""

def create_studies(number_of_studies):
    """ Creates a number of studies and the required objects to create a study

    Arguments:
        number_of_users -- the number of rows of studies added to the database
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

        study_test_list.append(study.study_id)


"""Experiment test"""

def create_experiment(number_of_experiments):
    """ Creates a number of experiments and the required objects to create an experiment

    Arguments:
        number_of_experiments -- the number of rows of experiments added to the database
    """    
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
        e = Experiment(study_id=study_ids[id%len[study_ids]], study_design=s, risks=r, 
                    grade=g, participant_design=p, implemented=im, gender_1=0.5,
                    gender_2=0.5, intensity_n=1, duration_week=1, frequency_n=1, outcome="abc", outcome_full="abc")
        e.save()

        experiment_test_list.append(e.experiment_nr)

"""Effect data tests"""

    
def create_effect_data(number_of_effekts, number_of_existing_studies, number_of_exisiting_experiments):
    """ Creates a number of effect data and the required objects to create an effect data

    Arguments:
        number_of_effekts -- the number of rows of effect data added to the database
        number_of_existing_studies -- the number of rows of studies already existing in the database
        number_of_exisiting_experiments -- the number of rows of experiments already existing in the database
    """    
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
        effect_data = EffectData(study_id=[id%number_of_existing_studies],
                                 experiment_nr=[id%number_of_exisiting_experiments], sd1i=sd1i, sd2i=sd2i, n1i=n1i,
                                 n2i=n2i, m1i=m1i, m2i=m2i, d_var=d_var, d=d, f_stat=f_stat,
                                 t=t, ri=ri, mean_age=mean_age, ni=ni, icc=icc, ai=ai, bi=bi, ci=ci)
        effect_data.save()  
        the_effect_number = effect_data.effect_size_number 

        effect_data_test_list.append(the_effect_number)


"""All together"""

def create_database(number_of_rows):
    """ Creates a number of users, studies, experiments, effect data and the required 
        objects to create an effect data

    Arguments:
        number_of_rows -- the number of rows of each datatype added to the database
    """    
    create_user(number_of_rows)
    create_studies(number_of_rows)
    create_experiment(number_of_rows)
    create_effect_data(number_of_rows, number_of_rows, number_of_rows)


"""Test queries"""
# Check database contains the expected data
def test_create_objects(number_of_rows):
    """ Test the ability to create all objects in the database

    Arguments:
        number_of_rows -- the number of rows of studies and users which are expected in the database
    """    
    create_database(number_of_rows)
    # Checks so that all expected objects exists

    # Checks so that all expected objects exists in User
    for i in range(number_of_rows):
        assert User.objects.filter(orc_id=i) == User(orc_id=i, name=f"{i}", email=f"{i}@gmail.com", organization=f"{i}", nr_uploads=i)
        
        # Checks so that all expected objects exists in Study
        assert Study.objects.filter(study_id=i) == Study(study_id=i, uploader=i, country="Sweden", category=category_list[i%len(category_list)],
                    peer_reviewed=pear_reviewd_list[i%len(pear_reviewd_list)], authors="This, is, a, test, string",
                    doi="https://doi.org/10.2307/j.ctt1k85dmc", abstract="A well written abstract", keywords="Key, words",
                    nr_downloads=i)

        # Checks so that all expected objects exists in Experiment
        for ii in range(number_of_rows):
            s = StudyDesign(design=f"{id}")
            r = RiskOfBias(id=id, rob=f"{id}", robins=f"{id}")
            g = Grade(grade=f"{id}")
            p = ParticipantDesign(design=f"{id}")
            im = Implementation(implementor=f"{id}")
            assert Experiment.objects.filter(study_id=i, experiment_nr=ii) == Experiment(experiment_nr=ii, study_id=i, study_design=s, risks=r, grade=g, 
                                                                        participant_design=p, implemented=im, gender_1=0.5,gender_2=0.5, intensity_n=1, 
                                                                        duration_week=1, frequency_n=1, outcome="abc", outcome_full="abc")
            # Checks so that all expected objects exists in EffectData 
            for iii in range(number_of_rows):
                assert EffectData.objects.filter(study_id=i, experiment_nr=ii, effect_size_number=iii) == EffectData(effect_size_number=iii, study_id=[i%number_of_rows],
                                 experiment_nr=[ii%number_of_rows], sd1i=3.2132, sd2i=3.2132, n1i=22.213,
                                 n2i=21.213, m1i=4.0011, m2i=4.0201, d_var=21.321, d=32.1231, f_stat=12.123,
                                 t=42.213, ri=3.123, mean_age=22, ni=21.32, icc=12.42, ai=14, bi=54, ci=12)
#Test edgecases

"""Test updating"""
# Test updating the exisitng data 
def test_updating_objects(number_of_rows):
    """ Tests the ability to change the existing data in the database
    
    Keyword arguments:
    number_of_rows -- the number of rows of studies and users which are expected in the database
    """
    # Goes through the tables and makes changes
    for i in range(number_of_rows):
        #  Loops through all users and itterates the name of the user
        user = User.objects.filter(orc_id=i)
        user.name = f"{i + 1}"
        user.save()
        
        
        # Goes through all studies and changes the country to England from Sweden
        study = Study.objects.filter(study_id=i)
        study.country = "England"
        study.save()
        
        for ii in range(number_of_rows):
            # Goes through all experiments and changes the gender deispertion
            experiment = Experiment.objects.filter(experiment_nr = ii, study_id = i)
            experiment.gender_1 = 0.3
            experiment.gender_2 = 0.7
            experiment.save()
        
            for iii in range(number_of_rows):
                # Goes through the effect_data and adds/changes
                effect_data = EffectData.objects.filter(study_id = i, experiment_nr = ii,
                                                        effect_size_number = iii)
                effect_data.di = 5
                effect_data.save()
        
    # Goes through the table and checks so the expected changes are made
    for i in range(number_of_rows):
        # Checks so all names are iterated 
        assert User.objects.filter(orc_id=i) == User(orc_id=i, name=f"{i+1}", email=f"{i}@gmail.com", organization=f"{i}", nr_uploads=i)
        
        # Checks so all countries are changed to "England" from "Sweden"
        assert Study.objects.filter(study_id=i) == Study(study_id=i, uploader=i, country="England", category=category_list[i%len(category_list)],
                    peer_reviewed=pear_reviewd_list[i%len(pear_reviewd_list)], authors="This, is, a, test, string",
                    doi="https://doi.org/10.2307/j.ctt1k85dmc", abstract="A well written abstract", keywords="Key, words",
                    nr_downloads=i)
        
        for ii in range(number_of_rows):
            # Checks so all experiments have the new gender dispertion
            s = StudyDesign(design=f"{id}")
            r = RiskOfBias(id=id, rob=f"{id}", robins=f"{id}")
            g = Grade(grade=f"{id}")
            p = ParticipantDesign(design=f"{id}")
            im = Implementation(implementor=f"{id}")
            assert Experiment.objects.filter(study_id=i, experiment_nr=ii) == Experiment(experiment_nr=ii, study_id=i, study_design=s, risks=r, grade=g, 
                                                                        participant_design=p, implemented=im, gender_1=0.3,gender_2=0.7, intensity_n=1, 
                                                                        duration_week=1, frequency_n=1, outcome="abc", outcome_full="abc")
            for iii in range(number_of_rows):
                # Checks so all EffectData has new di element
                assert EffectData.objects.filter(study_id=i, experiment_nr=ii, effect_size_number=iii) == EffectData(effect_size_number=iii, study_id=[i%number_of_rows],
                                 experiment_nr=[ii%number_of_rows], sd1i=3.2132, sd2i=3.2132, n1i=22.213,
                                 n2i=21.213, m1i=4.0011, m2i=4.0201, d_var=21.321, d=32.1231, f_stat=12.123,
                                 t=42.213, ri=3.123, mean_age=22, ni=21.32, icc=12.42, ai=14, bi=54, ci=12, di=5)
        
        

"""Test deleting"""

def test_deleting_objects():
    """ Tests the ability to delete the existing data in the database
    """
    # Test the ability to delete the Users
    for user_id in user_test_list:
        user = User.objects.filter(orc_id=user_id)
        user.delete
        assert not User.objects.exists(user)

    # Test the ability to delete the Studies
    for study_id in study_test_list:
        study = Study.objects.filter(study_id=study_id)

        # Test the ability to delete the Experiments
        for experiment_nr in experiment_test_list:
            experiment = Experiment.objects.filter(study_id=study_id, experiment_nr=experiment_nr)

            # Test the ability to delete the EffectData
            for effect_data_nr in effect_data_test_list:
                effect_data = EffectData.objects.filter(study_id=study_id, experiment_nr=experiment_nr, 
                                                        effect_size_number=effect_data_nr)
                effect_data.delete
                assert not EffectData.objects.exists(effect_data)

            experiment.delete
            assert not Experiment.objects.exists(experiment)

        study.delete
        assert not Study.objects.exists(study)


# Handle edgecases
    # Handle no data provided
    # Handle incorrect formated data
    # Handle incorrect parameters