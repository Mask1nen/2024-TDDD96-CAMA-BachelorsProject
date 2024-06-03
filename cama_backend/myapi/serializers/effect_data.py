from rest_framework import serializers
from ..models import TestTime, EffectSizeType, EffectData, Experiment

import logging
logger = logging.getLogger(__name__)

class TestTimeSerializer(serializers.ModelSerializer):
    """
    Serializer for the TestTime model.
    
    Converts JSON representations of a test time into a TestTime model 
    object during POST-requests and TestTime model objects into JSON objects 
    during GET-requests.
    """

    class Meta:
        model = TestTime
        fields = '__all__'

class EffectSizeTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for the EffectSizeType model.
    
    Converts JSON representations of an effect size type into an EffectSizeType model 
    object during POST-requests and EffectSizeType model objects into JSON objects 
    during GET-requests.
    """

    class Meta:
        model = EffectSizeType
        fields = '__all__'

class EffectDataSerializer(serializers.ModelSerializer):
    """
    Serializer for the EffectData model.
    
    Converts EffectData model objects into JSON representations during GET-requests.
    Provides a nested representation of related objects.
    """

    experiment_nr = serializers.PrimaryKeyRelatedField(queryset=Experiment.objects.all())
    effect_size_type = EffectSizeTypeSerializer()
    test_time = TestTimeSerializer()

    class Meta:
        model = EffectData
        fields = '__all__'

class EffectDataCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating an EffectData model.
    
    Converts JSON representations of effect data into an EffectData model 
    object during POST-requests.
    """

    experiment_nr = serializers.PrimaryKeyRelatedField(queryset=Experiment.objects.all())
    effect_size_type = serializers.SlugRelatedField(queryset=EffectSizeType.objects.all(), slug_field='name')
    test_time = serializers.SlugRelatedField(queryset=TestTime.objects.all(), slug_field='time')

    class Meta:
        model = EffectData
        fields = '__all__'

class EffectDataFromParentSerializer(serializers.ModelSerializer):
    """
    Serializer for nested EffectData objects.
    
    Converts JSON representations of effect data into an EffectData model 
    object, excluding the experiment_nr field. This is used during the creation of a study.
    """
    effect_size_type = serializers.SlugRelatedField(queryset=EffectSizeType.objects.all(), slug_field='name')
    test_time = serializers.SlugRelatedField(queryset=TestTime.objects.all(), slug_field='time')
    
    class Meta:
        model = EffectData
        exclude = ['experiment_nr']