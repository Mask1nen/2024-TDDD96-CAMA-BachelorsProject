from rest_framework import serializers
from ..models import Experiment, StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, Study, EffectData
from .effect_data import EffectDataSerializer, EffectDataFromParentSerializer

import logging
logger = logging.getLogger(__name__)


class StudyDesignSerializer(serializers.ModelSerializer):
    """
    Serializer for the StudyDesign model.
    
    Converts JSON representations of a study design into a StudyDesign model 
    object during POST-requests and StudyDesign model objects into JSON objects 
    during GET-requests.
    """
    class Meta:
        model = StudyDesign
        fields = '__all__'


class RiskOfBiasSerializer(serializers.ModelSerializer):
    """
    Serializer for the RiskOfBias model.
    
    Converts JSON representations of a risk of bias into a RiskOfBias model 
    object during POST-requests and RiskOfBias model objects into JSON objects 
    during GET-requests.
    """
    class Meta:
        model = RiskOfBias
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Grade model.
    
    Converts JSON representations of a grade into a Grade model 
    object during POST-requests and Grade model objects into JSON objects 
    during GET-requests.
    """
    class Meta:
        model = Grade
        exclude = ['id']

class ParticipantDesignSerializer(serializers.ModelSerializer):
    """
    Serializer for the ParticipantDesign model.
    
    Converts JSON representations of a participant design into a ParticipantDesign 
    model object during POST-requests and ParticipantDesign model objects into 
    JSON objects during GET-requests.
    """
    class Meta:
        model = ParticipantDesign
        fields = '__all__'

class ImplementationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Implementation model.
    
    Converts JSON representations of an implementation into an Implementation 
    model object during POST-requests and Implementation model objects into 
    JSON objects during GET-requests.
    """
    class Meta:
        model = Implementation
        fields = '__all__'

class ExperimentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Experiment model.
    
    Converts Experiment model objects into JSON representations during GET-requests. 
    Provides a nested representation of related objects.
    """

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
    """
    Serializer for creating an Experiment model.
    
    Converts JSON representations of an experiment into an Experiment model 
    object during POST-requests. Handles nested creation of related EffectData objects.
    """

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
        """
        Create a new Experiment instance along with nested EffectData instances.
        
        Args:
            validated_data (dict): Validated data containing experiment and nested 
                                   effect data attributes.
        
        Returns:
            Experiment: The created Experiment instance.
        """

        effects_data = validated_data.pop('effects')
        grade_data = validated_data.pop('grade')
        grade = Grade.objects.get_or_create(**grade_data)[0]
        experiment = Experiment.objects.create(grade=grade, **validated_data)
        for effect in effects_data:
            EffectData.objects.create(experiment_nr=experiment, **effect)
        return experiment

class ExperimentFromParentSerializer(serializers.ModelSerializer):
    """
    Serializer for nested Experiment objects.
    
    Converts JSON representations of an experiment into an Experiment model 
    object, excluding the study_id field. This is used when creating study objects
    """

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
    """
    Serializer for updating the approval status of nested Experiment objects.
    
    Converts JSON representations to update the 'approved' field of Experiment 
    model objects.
    """
    class Meta:
        model = Experiment
        fields = ['approved']