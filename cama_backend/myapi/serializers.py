from rest_framework import serializers
from .models import Study, Country, Category, CamaUser,  StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, Experiment



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class CamaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamaUser
        fields = ['orc_id', 'name', 'email', 'organization', 'nr_uploads']

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

class ExperimentSerializer(serializers.ModelSerializer):
    study_design = serializers.PrimaryKeyRelatedField(queryset=StudyDesign.objects.all())
    # risks = RiskOfBiasSerializer()
    # grade = serializers.PrimaryKeyRelatedField(queryset=Grade.objects.all())
    # participant_design = serializers.PrimaryKeyRelatedField(queryset=ParticipantDesign.objects.all())
    # implemented = serializers.PrimaryKeyRelatedField(queryset=Implementation.objects.all())

# CamaUser Serializer
class CamaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = ['gender_2','experiment_nr','gender_1', 'intensity_n', 'duration_week', 'frequency_n', 'outcome','outcome_full', 'study_design']#, 'risks', 'grade', 'participant_design', 'implemented']#'__all__'

    
# Study Serializer
class StudySerializer(serializers.ModelSerializer):
    experiment = ExperimentSerializer(many=True)
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Study
        fields = '__all__'  # Customize fields as needed'''

# Experiment Serializer
class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = '__all__'

    def create(self, validated_data):
        # Get experiment list
        experiments_data = validated_data.pop('experiment')
        
        

        # Get uploader id
        #uploader_id = validated_data.pop('uploader')
        # Get all dictionaries from json
        # study_year_data = validated_data.pop('study_year')
        # country_data = validated_data.pop('country')
        # category_data = validated_data.pop('category')
    
        # Create tables in order to create a study
        #uploader, _ = CamaUser.objects.get(validated_data['uploader'])
        # study_year = Year.objects.get(pk=study_year_data)
        # country, _ = Country.objects.get_or_create(**country_data)
        # category, _ = Category.objects.get_or_create(**category_data)


        # Create study
        study = Study.objects.create(
            #uploader=uploader,
            # study_year=study_year,
            # country=country,
            # category=category,
            **validated_data
        )

        # Create experiment tables
        for entry in experiments_data:
            # Get all dictionaries from 
            study_design_data = validated_data.pop('study_design')
            # risks_data = validated_data.pop('risks')
            # grade_data = validated_data.pop('grade')
            # participant_design_data = validated_data.pop('participant_design')
            # implemented_data = validated_data.pop('implemented')

            study_design, _ = StudyDesign.objects.get_or_create(**study_design_data)
            # risks, _ = RiskOfBias.objects.get_or_create(**risks_data)
            # grade, _ = Grade.objects.get_or_create(**grade_data)
            # participant_design, _ = ParticipantDesign.objects.get_or_create(**participant_design_data)
            # implemented, _ = Implementation.objects.get_or_create(**implemented_data)

            experiment = Experiment.objects.create(
                # study_id=study,
                # study_design=study_design,
                # risks=risks,
                # grade=grade,
                # participant_design=participant_design,
                # implemented=implemented,
                **entry
            )  



        return study
