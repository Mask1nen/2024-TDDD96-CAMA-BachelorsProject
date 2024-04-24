from rest_framework import serializers
from .models import *
import logging
logger = logging.getLogger(__name__)


class StudyDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDesign
        fields = ['design']
    
    def create(self, validated_data):
            study_design_name = validated_data.pop('design')
            study_design = StudyDesign.objects.create(**study_design_name)
            return study_design

class RiskOfBiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskOfBias
        fields = ['rob']

    def create(self, validated_data):
            risk_of_bias_rob = validated_data.pop('rob')
            risk_of_bias = RiskOfBias.objects.create(**risk_of_bias_rob)
            return risk_of_bias

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['grade']
        
    def create(self, validated_data):
            grade_name = validated_data.pop('grade')
            grade = Grade.objects.create(**grade_name)
            return grade

class ParticipantDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantDesign
        fields = ['design']
        
    def create(self, validated_data):
            participant_design_name = validated_data.pop('design')
            participant_design = ParticipantDesign.objects.create(**participant_design_name)
            return participant_design

class ImplementationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Implementation
        fields = ['implementor']
        
    def create(self, validated_data):
            implementation_name = validated_data.pop('implementor')
            implementation = Implementation.objects.create(**implementation_name)
            return implementation

class EffectDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EffectData
        fields = '__all__'  # add other fields if needed        

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']
        
        def create(self, validated_data):
            country_name = validated_data.pop('name')
            country = Country.objects.create(**country_name)
            return country

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        
    def create(self, validated_data):
            name = validated_data.pop('name')
            category = Category.objects.create(**name)
            return category


class YearSerializer(serializers.ModelSerializer):
    class Meta:
    #    model = Year
        fields = ['study_year']

class CamaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamaUser
        fields = ['orc_id', 'name', 'email', 'organization', 'nr_uploads']
        
        
class TestTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTime
        fields = '__all__'
        
    def create(self, validated_data):
            time = validated_data.pop('time')
            test_time = TestTime.objects.create(**time)
            return test_time
        
class EffectSizeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EffectSizeType
        fields = '__all__'
        
    def create(self, validated_data):
            type = validated_data.pop('name')
            effect_size_type = EffectSizeType.objects.create(**type)
            return effect_size_type
    
class StudySerializer(serializers.ModelSerializer):
    uploader = CamaUserSerializer(many=False)
   # study_year = YearSerializer(many=False)
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
       # study_year = Year.objects.create(**study_year_data)
        country_data = validated_data.pop('country')
        country = Country.objects.create(**country_data)
        category_data = validated_data.pop('category')
        category = Category.objects.create(**category_data)
        
        study = Study.objects.create(
            uploader = cama_user,
          #  study_year = study_year,
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