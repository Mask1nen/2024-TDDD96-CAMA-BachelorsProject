from rest_framework import serializers
from .models import *
import logging
logger = logging.getLogger(__name__)


class StudyDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDesign
        fields = ['design']

class RiskOfBiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskOfBias
        fields = ['id', 'rob', 'robins']

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['grade']

class ParticipantDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantDesign
        fields = ['design']

class ImplementationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Implementation
        fields = ['implementor']

class EffectDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EffectData
        fields = '__all__'  # add other fields if needed        

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class YearSerializer(serializers.ModelSerializer):
    class Meta:
    #    model = Year
        fields = ['study_year']

class CamaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamaUser
        fields = ['orc_id', 'name', 'email', 'organization', 'nr_uploads']
    
class StudySerializer(serializers.ModelSerializer):
    uploader = CamaUserSerializer(many=False)
    study_year = YearSerializer(many=False)
    country = CountrySerializer(many=False)
    category = CategorySerializer(many=False)

    class Meta:
        model = Study
        fields = '__all__'  # add other fields if needed

    def create(self, validated_data):
        logger.info(f"This is the validated data: {validated_data}")
        cama_user_data = validated_data.pop('uploader')
        cama_user = CamaUser.objects.create(**cama_user_data)
        study_year_data = validated_data.pop('study_year')
       # study_year = Year.objects.create(**study_year_data)
        country_data = validated_data.pop('country')
        country = Country.objects.create(**country_data)
        category_data = validated_data.pop('category')
        category = Category.objects.create(**category_data)
        
        study = Study.objects.create(
            uploader = cama_user,
            study_year = study_year,
            country = country,
            category = category,
            **validated_data
            )
        logger.info(study)
        return study

class ExperimentSerializer(serializers.ModelSerializer):
    study_id = StudySerializer(many=False)
    study_design = StudyDesignSerializer(many=False)
    risks = RiskOfBiasSerializer(many=False)
    grade = GradeSerializer(many=False)
    participant_design = ParticipantDesignSerializer(many=False)
    implemented = ImplementationSerializer(many=False)

    class Meta:
        model = Experiment
        fields = '__all__'  # add other fields if needed