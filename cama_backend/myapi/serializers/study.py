from rest_framework import serializers
from ..models import Study, Country, Category, CamaUser, Experiment, EffectData
from .experiment import ExperimentSerializer, ExperimentFromParentSerializer

import logging
logger = logging.getLogger(__name__)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']
        
    def create(self, validated_data):
            country_name = validated_data.pop('name')
            country = Country.objects.create(name=country_name)
            return country


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
    
    def create(self, validated_data):
            name = validated_data.pop('name')
            category = Category.objects.create(name=name)
            return category


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
