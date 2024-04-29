from rest_framework import serializers
from ..models import Experiment, StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, Study, EffectData
from .effect_data import EffectDataSerializer, EffectDataFromParentSerializer

import logging
logger = logging.getLogger(__name__)


class StudyDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDesign
        fields = ['design']
        
    def create(self, validated_data):
            study_design_name = validated_data.pop('design')
            study_design = StudyDesign.objects.create(design=study_design_name)
            return study_design


class RiskOfBiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskOfBias
        fields = ['rob']
        
    def create(self, validated_data):
            risk_of_bias_rob = validated_data.pop('rob')
            risk_of_bias = RiskOfBias.objects.create(rob=risk_of_bias_rob)
            return risk_of_bias


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
        
    def create(self, validated_data):
            grade_k = validated_data.pop('k')
            grade_first = validated_data.pop('first')
            grade_second = validated_data.pop('second')
            grade_third = validated_data.pop('third')
            grade_forth = validated_data.pop('forth')
            grade_fifth = validated_data.pop('fifth')
            grade_sixth = validated_data.pop('sixth')
            grade_seventh = validated_data.pop('seventh')
            grade_eighth = validated_data.pop('eighth')
            grade_ninth = validated_data.pop('ninth')
            grade_tenth = validated_data.pop('tenth')
            grade_eleventh = validated_data.pop('eleventh')
            grade_twelfth = validated_data.pop('twelfth')
            grade = Grade.objects.create(k=grade_k, first=grade_first, second=grade_second,
                                         third=grade_third, forth=grade_forth, fifth=grade_fifth,
                                         sixth=grade_sixth, seventh=grade_seventh, eighth=grade_eighth,
                                         ninth=grade_ninth, tenth=grade_tenth, eleventh=grade_eleventh,
                                         twelfth=grade_twelfth)
            return grade


class ParticipantDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantDesign
        fields = '__all__' #['design']
        
    def create(self, validated_data):
            participant_design_name = validated_data.pop('design')
            participant_design = ParticipantDesign.objects.create(design=participant_design_name)
            return participant_design


class ImplementationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Implementation
        fields = ['implementor']
        
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