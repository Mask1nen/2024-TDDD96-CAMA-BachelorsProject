from django.db import models
import pytest
from django.core.exceptions import *

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
        user = User(orc_id=f"{id}", name=f"{id}", email=f"{id}@gmail.com", organization=f"{id}", nr_uploads=id)
        user.save()
    
        
        user_test_list.append(user.orc_id)
    print(User._meta.get_fields()[0])
    


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
        study = Study(uploader=id, year=year1, country=country, category=category_list[id%len(category_list)],
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
                effect_data.delete()
                assert not EffectData.objects.exists(effect_data)

            experiment.delete()
            assert not Experiment.objects.exists(experiment)

        study.delete()
        assert not Study.objects.exists(study)


# Handle edgecases
    # Handle no data provided
def test_providing_no_data():
    """Tests if providing no data couses the expected exeptions
    """    
    # Create empty user
    user = User()
    user.save()
    empty_user_id = user.objects.orc_id
    
    # Create emppty study
    study = Study()
    study.save()
    empty_study_id = study.objects.orc_id
    
    # Test creating empty experiment and assert the expected exception is thrown
    experiment = Experiment()
    with pytest.raises((DataError, ValidationError)):
        experiment.save()
    empty_experiment_id = experiment.objects.orc_id
    
    # Test creating empty efffect data and assert the expected exception is thrown
    effect_data = EffectData()
    with pytest.raises((DataError, ValidationError)):
        effect_data.save()
    empty_effect_data_id = effect_data.objects.orc_id
    
    # Delete the experiment and effect data if they were created
    if empty_experiment_id:
        Experiment.objects.filter(experiemtn_nr=empty_experiment_id).delete
    if empty_effect_data_id:
        EffectData.objects.filter(effect_size_number=empty_effect_data_id).delete
        
    # Test creating empty experiment and effect data which only contains refrences
    empty_experiment = Experiment(study_id=empty_study_id)
    empty_experiment.save()
    empty_experiment_id = empty_experiment.experiment_nr
    empty_effect_data = EffectData(study_id=empty_study_id, experiment_nr=empty_experiment_id)
    empty_effect_data.save()
    empty_effect_data_id = empty_effect_data.effect_size_number
    
    
    # Assert that the empty representations of the user and study is correct formated
    empty_user = User.objects.filter(orc_id=empty_user_id)
    empty_study = Study.objects.filter(study_id=empty_study_id)
    empty_experiment = Experiment.objects.filter(study_id=empty_study_id, experiment_nr=empty_experiment_id)
    empty_experiment = EffectData.objects.filter(study_id=empty_study_id, experiment_nr=empty_experiment_id,
                                                 effect_size_number=empty_effect_data_id)
    assert empty_user == User(study_id=empty_study_id)
    assert empty_study == Study(study_id=empty_study_id)
    assert empty_experiment == Experiment(study_id=empty_study_id, experiment_nr=empty_experiment_id)
    assert empty_effect_data == EffectData(study_id=empty_study_id, experiment_nr=empty_experiment_id,
                                           effect_size_number=empty_effect_data_id)
        
    empty_user.delete
    empty_study.delete

    
#def validation_check_improvment(table, value_to_change, new_value):
#    with pytest.raises(ValidationError):
#        for x in User._meta.get_fields(): 
#            print(x.field)
#            match x.db_type:
#                case models.fields.CharField:
#                    x.name
#                    models.Model.
#                    user = User(x.name=new_value)
#                case models.fields.IntegerField:
#                    
#                case models.fields.BooleanField:
                    
            
    
def validation_check(table, value_to_change, new_value):
    with pytest.raises(ValidationError):
        tmp_table = table
        match value_to_change:
            # User 
            case "name":
                table.name = new_value
            case "email":
                table.email = new_value
            case "organization":
                table.organization = new_value
            case "nr_uploads":
                table.nr_uploads = new_value   
            # Study
            case "uploader":
                table.uploader = new_value
            case "country":
                table.country = new_value
            case "category":
                table.category = new_value
            case "peer_reviewed":
                table.peer_reviewed = new_value
            case "authors":
                table.authors = new_value
            case "doi":
                table.doi = new_value
            case "abstract":
                table.abstract = new_value
            case "keywords":
                table.keywords = new_value
            case "nr_downloads":
                table.nr_downloads = new_value
            # Experiment
            case "study_id":
                table.study_id = new_value
            case "experiment_nr":
                table.experiment_nr = new_value
            case "study_design":
                table.study_design = new_value
            case "risks":
                table.risks = new_value
            case "grade":
                table.grade = new_value
            case "participant_design":
                table.participant_design = new_value
            case "implemented":
                table.implemented = new_value
            case "gender_1":
                table.gender_1 = new_value
            case "gender_2":
                table.gender_2 = new_value
            case "intensity_n":
                table.intensity_n = new_value
            case "duration_week":
                table.duration_week = new_value
            case "frequency_n":
                table.frequency_n = new_value
            case "outcome":
                table.outcome = new_value
            case "outcome_full":
                table.outcome_full = new_value
            # Effect Data
            case "effect_size_number":
                table.effect_size_number = new_value
            case "study_id":
                table.study_id = new_value
            case "experiment_nr":
                table.experiment_nr = new_value
            case "sd1i":
                table.sd1i = new_value
            case "sd2i":
                table.sd2i = new_value
            case "n1i":
                table.n1i = new_value
            case "n2i":
                table.n2i = new_value
            case "m1i":
                table.m1i = new_value
            case "m2i":
                table.m2i = new_value
            case "d_var":
                table.d_var = new_value
            case "d":
                table.d = new_value
            case "f_stat":
                table.f_stat = new_value
            case "t":
                table.t = new_value
            case "ri":
                table.ri = new_value
            case "mean_age":
                table.mean_age = new_value
            case "ni":
                table.ni = new_value
            case "icc":
                table.icc = new_value
            case "ai":
                table.ai = new_value
            case "bi":
                table.bi = new_value
            case "ci":
                table.ci = new_value
            case "di":
                table.di = new_value
        tmp_table.save()
    
# Handle incorrect formated data
def test_incorrect_formated_data():


    # incorrect User data
    user = User(orc_id="10", name="10", email="10", organization="10", nr_uploads=10)
    user.save()
    validation_check(user, "orc_id", 10) 
    validation_check(user, "name", 10)
    validation_check(user, "email", 10)
    validation_check(user, "organization", 10)
    validation_check(user, "nr_uploads", "10")
    
    # incorrect year data
    with pytest.raises(ValidationError):
        year = Year(year="hi")
        year.save()

    # incorrect country data
    with pytest.raises(ValidationError):
        country = Country(name=10)
        country.save()

    # incorrect category data
    with pytest.raises(ValidationError):
        category = Category(name=10)
        category.save()

    # incorrect Study data
    year = Year(year=2024)
    year.save()
    country = Country(name=f"Sweden")
    country.save()
    category_list = ["Language", "Math", "STEM"]
    category = Category(name="HI")
    category.save()
    study = Study(uploader=user, year=year, country=country, category=category,
                    peer_reviewed=True, authors="This, is, a, test, string",
                    doi="https://doi.org/10.2307/j.ctt1k85dmc", abstract="A well written abstract", 
                    keywords="Key, words", nr_downloads=10)
    study.save()
    
    validation_check(study, "uploader", "hi")
    validation_check(study, "year", "hi")
    validation_check(study, "country", 10)
    validation_check(study, "category", 10)
    validation_check(study, "peer_reviewed", "hi")
    validation_check(study, "authors", 10)
    validation_check(study, "doi", 10)
    validation_check(study, "abstract", 10)
    validation_check(study, "keywords", 10)
    validation_check(study, "nr_downloads", "hi")   

    # incorrect StudyDesign data
    with pytest.raises(ValidationError):
        s = StudyDesign(design=10)
        s.save()
    # incorrect RiskOfBias data
    with pytest.raises(ValidationError):
        r = RiskOfBias(id="id", rob="abcd", robins="abcd")
        r.save()
    with pytest.raises(ValidationError):
        r = RiskOfBias(id=1, rob=10, robins="abcd")
        r.save()
    with pytest.raises(ValidationError):
        r = RiskOfBias(id=1, rob="abcd", robins=10)
        r.save()
    # incorrect Grade data
    with pytest.raises(ValidationError):
        g = Grade(grade=10)
        g.save()
    # incorrect ParticipantDesign data
    with pytest.raises(ValidationError):
        p = ParticipantDesign(design=10)
        p.save()
    # incorrect Implementation data
    with pytest.raises(ValidationError):
        im = Implementation(implementor=10)
        im.save()
    # incorrect Experiment data
    s = StudyDesign(design="abcd")
    r = RiskOfBias(id=1, rob="abcd", robins="abcd")
    g = Grade(grade="abcd")
    p = ParticipantDesign(design="abcd")
    im = Implementation(implementor="abcd")
    s.save()
    r.save()
    g.save()
    p.save()
    im.save()
    e = Experiment(study_id=study, study_design=s, risks=r, 
                    grade=g, participant_design=p, implemented=im, gender_1=0.5,
                    gender_2=0.5, intensity_n=1, duration_week=1, frequency_n=1, outcome="abc", outcome_full="abc")
    e.save()
    
    validation_check(e, "study_id", "hi")
    validation_check(e, "study_design", 10)
    validation_check(e, "risks", 10)
    validation_check(e, "grade", 10)
    validation_check(e, "participant_design", 10)
    validation_check(e, "implemented", 10)
    validation_check(e, "gender_1", "hi")
    validation_check(e, "gender_2", "hi")
    validation_check(e, "intensity_n", "hi")
    validation_check(e, "duration_week", "hi")
    validation_check(e, "frequency_n", "hi")
    validation_check(e, "outcome", 10)
    validation_check(e, "outcome_full", 10)
    
    # incorrect Effect data
    effect_data = EffectData(study_id=study, experiment_nr=e, sd1i=3.2132, sd2i=3.2132, n1i=22.213,
                            n2i=21.213, m1i=4.0011, m2i=4.0201, d_var=21.321, d=32.1231, f_stat=12.123,
                            t=42.213, ri=3.123, mean_age=22, ni=21.32, icc=12.42, ai=14, bi=54, ci=12, di=5)

    validation_check(effect_data, "study_id", 10)
    validation_check(effect_data, "experiment_nr", "hi")
    validation_check(effect_data, "sd1i", "hi")
    validation_check(effect_data, "sd2i", "hi")
    validation_check(effect_data, "n1i", "hi")
    validation_check(effect_data, "n2i", "hi")
    validation_check(effect_data, "m1i", "hi")
    validation_check(effect_data, "m2i", "hi")
    validation_check(effect_data, "d_var", "hi")
    validation_check(effect_data, "d", "hi")
    validation_check(effect_data, "f_stat", "hi")
    validation_check(effect_data, "t", "hi")
    validation_check(effect_data, "ri", "hi")
    validation_check(effect_data, "mean_age", "hi")
    validation_check(effect_data, "ni", "hi")
    validation_check(effect_data, "icc", "hi")
    validation_check(effect_data, "ai", "hi")
    validation_check(effect_data, "bi", "hi")
    validation_check(effect_data, "ci", "hi")
    validation_check(effect_data, "di", "hi")


    s.delete()
    r.delete()
    g.delete()
    p.delete()
    im.delete()
    e.delete()
    year.delete()
    country.delete()
    category.delete()
    study.delete()
        
    # Check cascade working correctly


        