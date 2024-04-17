from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ['study_year']

    #def to_representation(self, instance):
    #    return instance.study_year


class StudyDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDesign
        fields = ['design']

class RiskOfBiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskOfBias
        fields = ['id', 'rob', 'robins']

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

class EffectDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EffectData
        fields = '__all__'  # add other fields if needed

class ExperimentSerializer(serializers.ModelSerializer):
    effect_sizes = EffectDataSerializer(many=True)

    class Meta:
        model = Experiment
        fields = '__all__'  # add other fields if needed

    def create(self, validated_data):
        effect_sizes_data = validated_data.pop('effect_data')
        experiment = Experiment.objects.create(validated_data)
        #for effect_size_data in effect_sizes_data:
        #    EffectData.objects.create(experiment=experiment, **effect_size_data)
    
        study_id = validated_data.pop('study_id')
        study_design_data = validated_data.pop('study_design')
        risks_data = validated_data.pop('risks')
        grade_data = validated_data.pop('grade')
        participant_design_data = validated_data.pop('participant_design')
        implemented_data = validated_data.pop('implemented')

        study_id, _ = Study.objects.get_or_create(**study_id)      
        study_design, _ = StudyDesign.objects.get_or_create(**study_design_data)
        risks, _ = RiskOfBias.objects.get_or_create(**risks_data)
        grade, _ = Grade.objects.get_or_create(**grade_data)
        participant_design, _ = ParticipantDesign.objects.get_or_create(**participant_design_data)
        implemented, _ = Implementation.objects.get_or_create(**implemented_data)

        experiment = Experiment.objects.create(
            study_id=study_id,
            study_design=study_design,
            risks=risks,
            grade=grade,
            participant_design=participant_design,
            implemented=implemented,
            **validated_data
        )
        return experiment

class StudySerializer(serializers.ModelSerializer):
    experiments = ExperimentSerializer(many=True)

    class Meta:
        model = Study
        fields = '__all__'  # add other fields if needed

    def create(self, validated_data):
        experiments_data = validated_data.pop('experiments')
        study = Study.objects.create(validated_data)
        for experiment_data in experiments_data:
            Experiment.objects.create(study=study, **experiment_data)
        return study

class CamaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamaUser
        fields = ['orc_id', 'name', 'email', 'organization', 'nr_uploads']
    def create(self, validated_data):
        studies_data = validated_data.pop('uploader')
        cama_user = CamaUser.objects.create(validated_data)
        for study_data in studies_data:
            Study.