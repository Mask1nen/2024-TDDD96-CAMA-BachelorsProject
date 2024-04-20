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

# RiskOfBias Serializer
class RiskOfBiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskOfBias
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

class StudySerializer(serializers.ModelSerializer):
    experiments = ExperimentSerializer(many=True)
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Study
        fields = '__all__'  


    def create(self, validated_data):
        # Get experiment list
        experiments_data = validated_data.pop('experiments')
        
        

        # Get uploader id
        #uploader_id = validated_data.pop('uploader')
        # Get all dictionaries from json
        # study_year_data = validated_data.pop('study_year')
        # country_data = validated_data.pop('country')
        # category_data = validated_data.pop('category')
    
        # Create tables in order to create a study
        #uploader, _ = CamaUser.objects.get(validated_data['uploader'])
        # study_year = Year.objects.get(pk=study_year_data)
        # country, _ = Country.objects.get_or_create(**country_data)
        # category, _ = Category.objects.get_or_create(**category_data)


        # Create study
        study = Study.objects.create(
            #uploader=uploader,
            # study_year=study_year,
            # country=country,
            # category=category,
            **validated_data
        )

        # Create experiment tables
        for experiment_data in experiments_data:
            # Get all dictionaries from 
            #study_design_data = validated_data.pop('study_design')
            risks_data = experiment_data.pop('risks')
            #grade_data = entry.pop('grade')
            # participant_design_data = validated_data.pop('participant_design')
            # implemented_data = validated_data.pop('implemented')

          #  study_design, _ = StudyDesign.objects.get_or_create(**study_design_data)
            risks, _ = RiskOfBias.objects.get_or_create(**risks_data)
            # grade, _ = Grade.objects.get_or_create(grade_data)
            # participant_design, _ = ParticipantDesign.objects.get_or_create(**participant_design_data)
            # implemented, _ = Implementation.objects.get_or_create(**implemented_data)


            effect_datas = experiment_data.pop('effect_datas')

            experiment = Experiment.objects.create(
                #study_id=study,
                # study_design=study_design,
                risks=risks,
                # grade=grade,
                # participant_design=participant_design,
                # implemented=implemented,
                **experiment_data
            )  


            for effect in effect_datas:
                EffectData.objects.create(experiment_nr = experiment, **effect)



        return study

