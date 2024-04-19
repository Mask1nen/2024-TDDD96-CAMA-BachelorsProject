from rest_framework import serializers
from .models import (
    CamaUser,
    Year,
    Country,
    Category,
    Study,
    StudyDesign,
    RiskOfBias,
    Grade,
    ParticipantDesign,
    Implementation,
    Experiment,
    EffectData,
)
import logging
logger = logging.getLogger(__name__)

# Year Serializer
class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'  # Customize fields as needed

# Country Serializer
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'  # Customize fields as needed

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Customize fields as needed

# StudyDesign Serializer
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
        fields = '__all__'  # Customize fields as needed

# CamaUser Serializer
class CamaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamaUser
        fields = '__all__'  # You can customize fields as needed
    
# Study Serializer
class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = '__all__'  # Customize fields as needed'''

# Experiment Serializer
class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = '__all__'

# EffectData Serializer
class EffectDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EffectData
        fields = '__all__'  # Customize fields as needed
