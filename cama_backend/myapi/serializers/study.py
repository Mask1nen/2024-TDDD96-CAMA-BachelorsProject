from rest_framework import serializers
from ..models import *
from .experiment import *

import logging
logger = logging.getLogger(__name__)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class StudySerializer(serializers.ModelSerializer):
    uploader = serializers.PrimaryKeyRelatedField(queryset=CamaUser.objects.all())
    country = CountrySerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    experiments = ExperimentSerializer(read_only=True, many=True)

    class Meta:
        model = Study
        fields = ['study_id', 'title', 'uploader', 'study_year', 'country', 'category', 'peer_reviewed',
                  'authors', 'doi', 'abstract', 'keywords', 'nr_downloads', 'approved', 'experiments']
        
class StudyCreateSerializer(serializers.ModelSerializer):
    uploader = serializers.PrimaryKeyRelatedField(queryset=CamaUser.objects.all())
    country = serializers.SlugRelatedField(read_only=True, slug_field='name')
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    experiments = serializers.ListField(child=ExperimentFromParentSerializer())

    class Meta:
        model = Study
        fields = ['title', 'uploader', 'study_year', 'country', 'category', 'peer_reviewed',
                  'authors', 'doi', 'abstract', 'keywords', 'approved', 'experiments']
        
    def create(self, validated_data):
        experiment_data = validated_data.pop('experiments')
        study = Study.objects.create(**validated_data)
        for experiment in experiment_data:
            effect_data = experiment.pop('effects')
            experiment = Experiment.objects.create(study_id=study, **experiment)
            for effect in effect_data:
                EffectData.objects.create(experiment_nr=experiment, **effect)
        return study




class StudySerializerUpdate(serializers.ModelSerializer):
    experiments = serializers.ListField(child=ExperimentFromParentSerializerApproved())

    class Meta:
        model = Study
        fields = ['approved', 'experiments']
    # def validate(self, data):
    #     """
    #     Validate authenticated user
    #     """

    #     if self.instance.uploader != self.context['request'].uploader:
    #         raise serializers.ValidationError('You can not edit posts from other users')
    #     return data

    def update(self, instance, validated_data):
        # Only update the 'approved' field in all nested tables
        for table in validated_data.get('experiments'):
            table.approved = validated_data.get('approved')
            table.save()  # This is necessary
        instance.save()
        return instance
