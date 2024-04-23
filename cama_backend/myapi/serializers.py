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

class CamaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamaUser
        fields = ['orc_id', 'name', 'email', 'organization', 'nr_uploads']

class StudyDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDesign
        fields = '__all__'  # Customize fields as needed



# Grade Serializer
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'  # Customize fields as needed


# ParticipantDesign Serializer
class ParticipantDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantDesign
        fields = '__all__'  # Customize fields as needed

# Implementation Serializer
class ImplementationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Implementation
        fields = ['implementor']


class EffectDataSerializer(serializers.ModelSerializer):
    test_time = serializers.SlugRelatedField(slug_field='time', queryset=TestTime.objects.all())
    effect_size_type = serializers.SlugRelatedField(slug_field='name', queryset=EffectSizeType.objects.all())
    class Meta:
        model = EffectData
        fields = ["effect_size_type",
                            "test_time",
                            "test_name",

                            "outcome",
                            "outcome_full",
                            "outcome_op",


                            "gender_1",
                            "gender_2",
                            "gender_3",

                            "d_var",
                            "d",
                            "f_stat",
                            "t",
                            "ri",
                            "icc",

                            "mean_age_1i",
                            "mean_age_2i",

                            "ai",
                            "bi",
                            "ci",
                            "di",

                            "sd1i",
                            "sd2i",
                            "n1i",
                            "n2i",
                            "m1i",
                            "m2i",
                            ]




# RiskOfBias Serializer
class RiskOfBiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskOfBias
        fields = '__all__'  



class ExperimentSerializer(serializers.ModelSerializer):
    grade = serializers.SlugRelatedField(slug_field='grade', queryset=Grade.objects.all())
    study_design = serializers.SlugRelatedField(slug_field='design', queryset=StudyDesign.objects.all())
    participant_design = serializers.SlugRelatedField(slug_field='design', queryset=ParticipantDesign.objects.all())
    implemented = serializers.SlugRelatedField(slug_field='implementor', queryset=Implementation.objects.all())
    risks=RiskOfBiasSerializer()
    effect_datas = EffectDataSerializer(many=True)

    class Meta:
        model = Experiment
        fields = ['grade', 'study_design', 'participant_design', 'implemented', 'intensity_n', 'ni', 'duration_week','frequency_n', 'intervention', 'intervention_op', 'target_population', 'mean_age', 'source', 'risks', 'effect_datas']


    def to_internal_value(self, data):
        rob = data.pop('rob', None)
        robins = data.pop('robins', None)

        if rob is not None and robins is not None:
            data['risks'] = {'rob' : rob, 'robins': robins}

        return super().to_internal_value(data)


class StudySerializer(serializers.ModelSerializer):
    experiments = ExperimentSerializer(many=True)
    country = serializers.SlugRelatedField(slug_field='name', queryset=Country.objects.all())
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Study
        fields = '__all__'  


    def create(self, validated_data):
        # Get experiment list
        experiments_data = validated_data.pop('experiments')
        
        
        # Create study
        study = Study.objects.create(
         
            **validated_data
        )

        # Create experiment tables
        for experiment_data in experiments_data:
           
            risks_data = experiment_data.pop('risks')
          
            risks, _ = RiskOfBias.objects.get_or_create(**risks_data)
      


            effect_datas = experiment_data.pop('effect_datas')

            risks, _ = RiskOfBias.objects.get_or_create(**risks_data)

            experiment = Experiment.objects.create(
                risks=risks,
                **experiment_data
            )  


            for effect in effect_datas:
                EffectData.objects.create(experiment_nr = experiment, **effect)



        return study

