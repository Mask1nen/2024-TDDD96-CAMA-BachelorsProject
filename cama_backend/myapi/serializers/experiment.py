from rest_framework import serializers
from ..models import Experiment, StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, Study, EffectData
from .effect_data import EffectDataSerializer, EffectDataFromParentSerializer

import logging
logger = logging.getLogger(__name__)


class StudyDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDesign
        fields = '__all__'
        
    def create(self, validated_data):
            study_design_name = validated_data.pop('design')
            study_design = StudyDesign.objects.create(design=study_design_name)
            return study_design


class RiskOfBiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskOfBias
        fields = '__all__'
        
    def create(self, validated_data):
            risk_of_bias_rob = validated_data.pop('rob')
            risk_of_bias = RiskOfBias.objects.create(rob=risk_of_bias_rob)
            return risk_of_bias


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        exclude = ['id']

class ParticipantDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantDesign
        fields = '__all__'
        
    def create(self, validated_data):
            participant_design_name = validated_data.pop('design')
            participant_design = ParticipantDesign.objects.create(design=participant_design_name)
            return participant_design


class ImplementationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Implementation
        fields = '__all__'
        
    def create(self, validated_data):
            implementation_name = validated_data.pop('implementor')
            implementation = Implementation.objects.create(implementor=implementation_name)
            return implementation


class ExperimentSerializer(serializers.ModelSerializer):
    study_id = serializers.PrimaryKeyRelatedField(queryset=Study.objects.all())
    study_design = StudyDesignSerializer(read_only=True)
    risks = RiskOfBiasSerializer(read_only=True)
    grade = GradeSerializer(read_only=True)
    participant_design = ParticipantDesignSerializer(read_only=True)
    implemented = ImplementationSerializer(read_only=True)
    effects = EffectDataSerializer(many=True, read_only=True)

    class Meta:
        model = Experiment
        fields = '__all__'

class ExperimentCreateSerializer(serializers.ModelSerializer):
    study_id = serializers.PrimaryKeyRelatedField(queryset=Study.objects.all())
    study_design = serializers.SlugRelatedField(queryset=StudyDesign.objects.all(), slug_field='design')
    risks = serializers.SlugRelatedField(queryset=RiskOfBias.objects.all(), slug_field='rob')
    grade = GradeSerializer()
    participant_design = serializers.SlugRelatedField(queryset=ParticipantDesign.objects.all(), slug_field='design')
    implemented = serializers.SlugRelatedField(queryset=Implementation.objects.all(), slug_field='implementor')
    effects = serializers.ListField(child=EffectDataFromParentSerializer())
    
    class Meta:
        model = Experiment
        fields = '__all__'

    def create(self, validated_data):
        effects_data = validated_data.pop('effects')
        grade_data = validated_data.pop('grade')
        grade = Grade.objects.get_or_create(**grade_data)[0]
        experiment = Experiment.objects.create(grade=grade, **validated_data)
        for effect in effects_data:
            EffectData.objects.create(experiment_nr=experiment, **effect)
        return experiment

class ExperimentFromParentSerializer(serializers.ModelSerializer):
    study_design = serializers.SlugRelatedField(queryset=StudyDesign.objects.all(), slug_field='design')
    risks = serializers.SlugRelatedField(queryset=RiskOfBias.objects.all(), slug_field='rob')
    grade = GradeSerializer()
    participant_design = serializers.SlugRelatedField(queryset=ParticipantDesign.objects.all(), slug_field='design')
    implemented = serializers.SlugRelatedField(queryset=Implementation.objects.all(), slug_field='implementor')
    effects = serializers.ListField(child = EffectDataFromParentSerializer())

    class Meta:
        model = Experiment
        exclude = ['study_id']


class ExperimentFromParentSerializerApproved(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = ['approved']