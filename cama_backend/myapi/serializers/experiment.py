from rest_framework import serializers
from ..models import Experiment, StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, Study
from .effect_data import EffectDataSerializer, EffectDataFromStudySerializer

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
        fields = ['grade']

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
    study_design = StudyDesignSerializer()
    risks = RiskOfBiasSerializer()
    grade = GradeSerializer()
    participant_design = ParticipantDesignSerializer()
    implemented = ImplementationSerializer()
    effects = EffectDataSerializer(many=True)

    class Meta:
        model = Experiment
        fields = '__all__'

class ExperimentCreateSerializer(serializers.ModelSerializer):
    study_id = serializers.PrimaryKeyRelatedField(queryset=Study.objects.all())
    study_design = serializers.SlugRelatedField(read_only = True, slug_field='study_design')
    risks = serializers.SlugRelatedField(read_only = True, slug_field='riskofbias')
    grade = serializers.SlugRelatedField(read_only = True, slug_field='agegrade')
    participant_design = serializers.SlugRelatedField(read_only = True, slug_field='part_design')
    implemented = serializers.SlugRelatedField(read_only = True, slug_field='implementation')

    class Meta:
        model = Experiment
        fields = '__all__'

class ExperimentFromStudySerializer(serializers.ModelSerializer):
    study_design = serializers.SlugRelatedField(read_only = True, slug_field='study_design')
    risks = serializers.SlugRelatedField(read_only = True, slug_field='riskofbias')
    grade = serializers.SlugRelatedField(read_only = True, slug_field='agegrade')
    participant_design = serializers.SlugRelatedField(read_only = True, slug_field='part_design')
    implemented = serializers.SlugRelatedField(read_only = True, slug_field='implementation')
    effects = serializers.ListField(child = EffectDataFromStudySerializer())

    class Meta:
        model = Experiment
        exclude = ['study_id']