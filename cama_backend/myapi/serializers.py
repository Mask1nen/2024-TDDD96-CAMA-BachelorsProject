from rest_framework import serializers
from .models import *


class CamaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamaUser
        fields = ['orc_id', 'name', 'email', 'organization', 'nr_uploads']


# Grade Serialize

class EffectDataSerializer(serializers.ModelSerializer):
    test_time = serializers.SlugRelatedField(slug_field='time', queryset=TestTime.objects.all())
    effect_size_type = serializers.SlugRelatedField(slug_field='name', queryset=EffectSizeType.objects.all())
    class Meta:
        model = EffectData
        fields = [
                "effect_size_type",
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




    def create(self, validated_data):
        return validated_data

# RiskOfBias Serializer
class RiskOfBiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskOfBias
        fields = '__all__'  




class ExperimentSerializer(serializers.ModelSerializer):
    effects = EffectDataSerializer(many=True)
    grade = serializers.SlugRelatedField(slug_field='grade', queryset=Grade.objects.all())
    study_design = serializers.SlugRelatedField(slug_field='design', queryset=StudyDesign.objects.all())
    participant_design = serializers.SlugRelatedField(slug_field='design', queryset=ParticipantDesign.objects.all())
    implemented = serializers.SlugRelatedField(slug_field='implementor', queryset=Implementation.objects.all())
    rob = serializers.CharField(source="risks")

    class Meta:
        model = Experiment
        fields = [
            'grade',
            'study_design', 
            'participant_design', 
            'implemented', 
            'rob', 
            'effects',
            'intensity_n',
            'ni',
            'duration_week',
            'frequency_n',
            'intervention',
            'intervention_op',
            'target_population',
            'mean_age',
            'source',
            'robins',
        ]



    def create(self, validated_data):
        # Get experiment list
        
        print(validated_data)
           
        risks_data = validated_data.pop('risks')

        
        risks, _ = RiskOfBias.objects.get_or_create(rob=risks_data)
    


        # effect_datas = validated_data.pop('effects')


        experiment = Experiment.objects.create(
            risks=risks,
            **validated_data
        )  


        # for effect in effect_datas:
        #     EffectData.objects.create(experiment_nr = experiment, **effect)



        return experiment


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

            
            risks, _ = RiskOfBias.objects.get_or_create(rob=risks_data)
        

            effects = experiment_data.pop('effects')


            experiment = Experiment.objects.create(
                study_id=study,
                risks=risks,
                **experiment_data
            )  


            for effect in effects:
                EffectData.objects.create(experiment_nr = experiment, **effect)




        return study

