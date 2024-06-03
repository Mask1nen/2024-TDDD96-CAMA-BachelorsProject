from rest_framework import serializers
from ..models import *
from .experiment import *

import logging
logger = logging.getLogger(__name__)

class CountrySerializer(serializers.ModelSerializer):
    """
    Serializer for the Country model.
    
    Converts JSON representations of a country into a Country model object 
    during POST-requests and Country model objects into JSON objects during 
    GET-requests.
    """
    class Meta:
        model = Country
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    
    Converts JSON representations of a category into a Category model object 
    during POST-requests and Category model objects into JSON objects during 
    GET-requests.
    """

    class Meta:
        model = Category
        fields = '__all__'

class StudySerializer(serializers.ModelSerializer):
    """
    Serializer for the Study model.
    
    Converts Study model objects into JSON representations during GET-requests.
    Provides a nested representation of related objects.
    """

    uploader = serializers.PrimaryKeyRelatedField(queryset=CamaUser.objects.all())
    country = CountrySerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    experiments = ExperimentSerializer(read_only=True, many=True)

    class Meta:
        model = Study
        fields = ['study_id', 'title', 'uploader', 'study_year', 'country', 'category', 'peer_reviewed',
                  'authors', 'doi', 'abstract', 'keywords', 'nr_downloads', 'approved', 'experiments']

   
class StudyCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a Study model.
    
    Converts JSON representations of a study into a Study model object during 
    POST-requests. Handles nested creation of experiments and their related data.
    """

    uploader = serializers.PrimaryKeyRelatedField(queryset=CamaUser.objects.all())
    country = serializers.SlugRelatedField(queryset=Country.objects.all(), slug_field='name')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    experiments = serializers.ListField(child=ExperimentFromParentSerializer())

    class Meta:
        model = Study
        fields = ['title', 'uploader', 'study_year', 'country', 'category', 'peer_reviewed',
                  'authors', 'doi', 'abstract', 'keywords', 'approved', 'experiments']
        
    def create(self, validated_data):
        """
        Create a new Study instance along with nested Experiment and EffectData instances.
        
        Args:
            validated_data (dict): Validated data containing study and nested 
                                   experiment and effect_data attributes.
        
        Returns:
            Study: The created Study instance.
        """
        experiment_data = validated_data.pop('experiments')
        study = Study.objects.create(**validated_data)
        for experiment in experiment_data:
            grade_data = experiment.pop('grade')
            grade = Grade.objects.get_or_create(**grade_data)[0]
            effect_data = experiment.pop('effects')
            experiment = Experiment.objects.create(grade=grade, study_id=study, **experiment)
            for effect in effect_data:
                EffectData.objects.create(experiment_nr=experiment, **effect)
        return study


class StudySerializerUpdate(serializers.ModelSerializer):
    """
    Serializer for updating a Study model.
    
    Converts JSON representations of a study into a Study model object during 
    POST-requests. Used for updating the approval status of studies and their 
    nested experiments.
    """

    experiments = serializers.ListField(child=ExperimentFromParentSerializerApproved())

    class Meta:
        model = Study
        fields = ['approved', 'experiments']

    def update(self, instance, validated_data):
        """
        Update the approval status of a Study instance and its nested Experiment instances.
        
        Args:
            instance (Study): The existing Study instance to be updated.
            validated_data (dict): Validated data containing the new approval status and 
                                   nested experiment attributes.
        
        Returns:
            Study: The updated Study instance.
        """

        # Only update the 'approved' field in all nested tables
        for table in validated_data.get('experiments'):
            table.approved = validated_data.get('approved')
            table.save()  # This is necessary
        instance.save()
        return instance
