from rest_framework import serializers
from .models import Study, Country, Category, CamaUser,  StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, Experiment

import logging
logger = logging.getLogger(__name__)

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

    def create(self, validated_data):
        
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


        # Create study
        logger.info(f"Calling Study.create with cama_user: {cama_user}")
        study = Study.objects.create(
            cama_user=cama_user,
            country=country,
            category=category,
            **validated_data
        )
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

