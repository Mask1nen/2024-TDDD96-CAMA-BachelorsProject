from rest_framework import serializers
from ..models import TestTime, EffectSizeType, EffectData, Experiment

import logging
logger = logging.getLogger(__name__)

class TestTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTime
        fields = '__all__' #['id,', 'name']
    
    def create(self, validated_data):
            time = validated_data.pop('time')
            test_time = TestTime.objects.create(time=time)
            return test_time


class EffectSizeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EffectSizeType
        fields = '__all__' #['id', 'name']
    
    def create(self, validated_data):
            type = validated_data.pop('name')
            effect_size_type = EffectSizeType.objects.create(name=type)
            return effect_size_type


class EffectDataSerializer(serializers.ModelSerializer):
    experiment_nr = serializers.PrimaryKeyRelatedField(queryset=Experiment.objects.all())
    effect_size_type = EffectSizeTypeSerializer()
    test_time = TestTimeSerializer()

    class Meta:
        model = EffectData
        fields = '__all__'

class EffectDataCreateSerializer(serializers.ModelSerializer):
    experiment_nr = serializers.PrimaryKeyRelatedField(queryset=Experiment.objects.all())
    effect_size_type = serializers.SlugRelatedField(read_only = True, slug_field='name')
    test_time = serializers.SlugRelatedField(read_only = True, slug_field='name')

    class Meta:
        model = EffectData
        fields = '__all__'

class EffectDataFromParentSerializer(serializers.ModelSerializer):
    effect_size_type = serializers.SlugRelatedField(read_only = True, slug_field='name')
    test_time = serializers.SlugRelatedField(read_only = True, slug_field='name')
    
    class Meta:
        model = EffectData
        exclude = ['experiment_nr']