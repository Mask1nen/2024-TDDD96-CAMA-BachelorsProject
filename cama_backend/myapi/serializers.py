from rest_framework import serializers
from .models import Study, Country, Category, CamaUser,  StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, Experiment

import logging
logger = logging.getLogger(__name__)

<<<<<<< HEAD
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class StudyDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDesign
        fields = '__all__'  # Customize fields as needed

# RiskOfBias Serializer
class RiskOfBiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskOfBias
        fields = '__all__'  # Customize fields as needed

# Grade Serializer
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'  # Customize fields as needed

# ParticipantDesign Serializer
class ParticipantDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantDesign
        fields = '__all__'  # Customize fields as needed

# Implementation Serializer
class ImplementationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Implementation
        fields = ['implementor']

class CamaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamaUser
        fields = ['orc_id', 'name', 'email', 'organization', 'nr_uploads']
 
class StudySerializer(serializers.ModelSerializer):
    #Declare which variables are serialized by what serializer
    country = CountrySerializer()
    category = CategorySerializer()
    cama_user = CamaUserSerializer()

    class Meta:
        model = Study
        fields = '__all__'  # Customize fields as needed'''
=======
class CamaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamaUser
        fields = ['orc_id', 'name', 'email', 'organization', 'nr_uploads']


# Grade Serialize

class EffectDataSerializer(serializers.ModelSerializer):
    test_time = serializers.SlugRelatedField(slug_field='time', queryset=TestTime.objects.all())
    effect_size_type = serializers.SlugRelatedField(slug_field='name', queryset=EffectSizeType.objects.all())
    class Meta:
        model = EffectData
        fields = [
                "effect_size_type",
                "test_time",
                "test_name",

                "outcome",
                "outcome_full",
                "outcome_op",


                "gender_1",
                "gender_2",
                "gender_3",

                "d_var",
                "d",
                "f_stat",
                "t",
                "ri",
                "icc",

                "mean_age_1i",
                "mean_age_2i",

                "ai",
                "bi",
                "ci",
                "di",

                "sd1i",
                "sd2i",
                "n1i",
                "n2i",
                "m1i",
                "m2i",
        ]




    def create(self, validated_data):
        return validated_data

# RiskOfBias Serializer
class RiskOfBiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskOfBias
        fields = '__all__'  




class ExperimentSerializer(serializers.ModelSerializer):
    effects = EffectDataSerializer(many=True)
    grade = serializers.SlugRelatedField(slug_field='grade', queryset=Grade.objects.all())
    study_design = serializers.SlugRelatedField(slug_field='design', queryset=StudyDesign.objects.all())
    participant_design = serializers.SlugRelatedField(slug_field='design', queryset=ParticipantDesign.objects.all())
    implemented = serializers.SlugRelatedField(slug_field='implementor', queryset=Implementation.objects.all())
    rob = serializers.CharField(source="risks")

    class Meta:
        model = Experiment
        fields = [
            'grade',
            'study_design', 
            'participant_design', 
            'implemented', 
            'rob', 
            'effects',
            'intensity_n',
            'ni',
            'duration_week',
            'frequency_n',
            'intervention',
            'intervention_op',
            'target_population',
            'mean_age',
            'source',
            'robins',
        ]



    def create(self, validated_data):
        # Get experiment list
        
        print(validated_data)
           
        risks_data = validated_data.pop('risks')

        
        risks, _ = RiskOfBias.objects.get_or_create(rob=risks_data)
    


        # effect_datas = validated_data.pop('effects')


        experiment = Experiment.objects.create(
            risks=risks,
            **validated_data
        )  


        # for effect in effect_datas:
        #     EffectData.objects.create(experiment_nr = experiment, **effect)



        return experiment


class StudySerializer(serializers.ModelSerializer):
    experiments = ExperimentSerializer(many=True)
    country = serializers.SlugRelatedField(slug_field='name', queryset=Country.objects.all())
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Study
        fields = '__all__'

>>>>>>> feat/471-api

    def create(self, validated_data):
        
<<<<<<< HEAD
        #Fetch data to create/fetch entries
        cama_user_data = validated_data.pop('cama_user')
        country_data = validated_data.pop('country')
        category_data = validated_data.pop('category')
    
        # Create tables in order to create a study
        logger.info(f"Calling CamaUser.create with cama_user_data: {cama_user_data}")
        cama_user, created = CamaUser.objects.get_or_create(**cama_user_data)
        if created:
            logger.info(f"Created a new user with name: {cama_user.name}")
        else:
            logger.info(f"Fetched existing user with name: {cama_user.name}")
        country, _ = Country.objects.get_or_create(**country_data)
        category, _ = Category.objects.get_or_create(**category_data)


=======
        
>>>>>>> feat/471-api
        # Create study
        logger.info(f"Calling Study.create with cama_user: {cama_user}")
        study = Study.objects.create(
<<<<<<< HEAD
            cama_user=cama_user,
            country=country,
            category=category,
            **validated_data
        )
=======
         
            **validated_data
        )

        # Create experiment tables
        for experiment_data in experiments_data:
            
            risks_data = experiment_data.pop('risks')

            
            risks, _ = RiskOfBias.objects.get_or_create(rob=risks_data)
        

            effects = experiment_data.pop('effects')


            experiment = Experiment.objects.create(
                study_id=study,
                risks=risks,
                **experiment_data
            )  


            for effect in effects:
                EffectData.objects.create(experiment_nr = experiment, **effect)




>>>>>>> feat/471-api
        return study

class ExperimentSerializer(serializers.ModelSerializer):
    study = StudySerializer()
    study_design = StudyDesignSerializer()
    risks = RiskOfBiasSerializer()
    grade = GradeSerializer()
    participant_design = ParticipantDesignSerializer()
    implemented = ImplementationSerializer()

    class Meta:
        model = Experiment
        fields = '__all__'

    def create(self, validated_data):

        #Fetch data to create/fetch entries
        study_data = validated_data.pop('study')
        study_design_data = validated_data.pop('study_design')
        risks_data = validated_data.pop('risks')
        grade_data = validated_data.pop('grade')
        participant_design_data = validated_data.pop('participant_design')
        implemented_data = validated_data.pop('implemented')

        # Create tables in order to create an experiment
        logger.info(f"Calling Study.create with study_data: {study_data}")
        study = Study.objects.get_or_create(**study_data)
        study_design = StudyDesign.objects.get_or_create(**study_design_data)
        risks = RiskOfBias.objects.get_or_create(**risks_data)
        grade = Grade.objects.get_or_create(**grade_data)
        participant_design = ParticipantDesign.objects.get_or_create(**participant_design_data)
        implemented = Implementation.objects.get_or_create(**implemented_data)

        logger.info(f"Calling Experiment.create with study: {study}")
        experiment = Experiment.objects.create(study = study,
                                               study_design = study_design,
                                               risks = risks,
                                               grade = grade,
                                               participant_design = participant_design,
                                               implemented = implemented,
                                               **validated_data)
        return experiment

