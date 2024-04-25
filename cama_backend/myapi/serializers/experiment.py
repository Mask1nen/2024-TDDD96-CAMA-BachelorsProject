from rest_framework import serializers
from ..models import Experiment, StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, Study, EffectData
from .effect_data import EffectDataSerializer, EffectDataFromParentSerializer

import logging
logger = logging.getLogger(__name__)


class StudyDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDesign
        fields = ['design']

class RiskOfBiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskOfBias
        fields = ['rob']

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class ParticipantDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantDesign
        fields = ['design']

class ImplementationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Implementation
        fields = ['implementor']

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
    study_design = serializers.SlugRelatedField(read_only=True, slug_field='design')
    risks = serializers.SlugRelatedField(read_only=True, slug_field='rob')
    grade = serializers.PrimaryKeyRelatedField(read_only=True) #Skriv om denna som multiplechoicefield
    participant_design = serializers.SlugRelatedField(read_only=True, slug_field='design')
    implemented = serializers.SlugRelatedField(read_only=True, slug_field='implementor')
    effects = serializers.ListField(child=EffectDataFromParentSerializer())

    class Meta:
        model = Experiment
        fields = '__all__'

    def create(self, validated_data):
        effects_data = validated_data.pop('effects')
        experiment = Experiment.objects.create(**validated_data)
        for effect in effects_data:
            EffectData.objects.create(experiment_nr=experiment, **effect)
        return experiment

class ExperimentFromParentSerializer(serializers.ModelSerializer):
    study_design = serializers.SlugRelatedField(read_only = True, slug_field='study_design')
    risks = serializers.SlugRelatedField(read_only = True, slug_field='riskofbias')
    grade = serializers.SlugRelatedField(read_only = True, slug_field='agegrade')
    participant_design = serializers.SlugRelatedField(read_only = True, slug_field='part_design')
    implemented = serializers.SlugRelatedField(read_only = True, slug_field='implementation')
    effects = serializers.ListField(child = EffectDataFromParentSerializer())

    class Meta:
        model = Experiment
        exclude = ['study_id']