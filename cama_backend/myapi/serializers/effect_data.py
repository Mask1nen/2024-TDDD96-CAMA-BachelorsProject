from rest_framework import serializers
from ..models import TestTime, EffectSizeType, EffectData, Experiment
from .experiment import ExperimentSerializer

import logging
logger = logging.getLogger(__name__)

class TestTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTime
        fields = ['id,', 'name']

class EffectSizeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EffectSizeType
        fields = ['id', 'name']

class EffectDataSerializer(serializers.ModelSerializer):
    experiment_nr = ExperimentSerializer()
    effect_size_type = EffectSizeTypeSerializer()
    test_time = TestTimeSerializer()

    class Meta:
        model = EffectData
        fields = '__all__'

class EffectDataCreateSerializer(serializers.ModelSerializer):
    experiment_nr = serializers.PrimaryKeyRelatedField(queryset=Experiment.objects.all())
    effect_size_type = serializers.SlugRelatedField(read_only = True, slug_field='estype')
    test_time = serializers.SlugRelatedField(read_only = True, slug_field='testtime')

    class Meta:
        model = EffectData
        fields = '__all__'