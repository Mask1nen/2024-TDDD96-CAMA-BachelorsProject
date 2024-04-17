from rest_framework import serializers
from .models import Study, Year, Country, Category, CamaUser,  StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, Experiment



class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ['study_year']

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

class StudySerializer(serializers.ModelSerializer):
    uploader = CamaUserSerializer()
    study_year = YearSerializer()
    country = CountrySerializer()
    category = CategorySerializer()

    class Meta:
        model = Study
        fields = '__all__'

    
    def create(self, validated_data):
        uploader_data = validated_data.pop('uploader')
        study_year_data = validated_data.pop('study_year')
        country_data = validated_data.pop('country')
        category_data = validated_data.pop('category')

        uploader, _ = CamaUser.objects.get_or_create(**uploader_data)
        study_year, _ = Year.objects.get_or_create(**study_year_data)
        country, _ = Country.objects.get_or_create(**country_data)
        category, _ = Category.objects.get_or_create(**category_data)

        study = Study.objects.create(
            uploader=uploader,
            study_year=study_year,
            country=country,
            category=category,
            **validated_data
        )
        return study





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

class ExperimentSerializer(serializers.ModelSerializer):
    #study_id = StudySerializer(many=False)
    study_design = StudyDesignSerializer()
    risks = RiskOfBiasSerializer()
    grade = GradeSerializer()
    participant_design = ParticipantDesignSerializer()
    implemented = ImplementationSerializer()

    class Meta:
        model = Experiment
        fields = ['gender_2', 'study_design', 'risks','grade','participant_design','implemented']

    
    def create(self, validated_data):
        #study_id = validated_data.pop('study_id')
        study_design_data = validated_data.pop('study_design')
        risks_data = validated_data.pop('risks')
        grade_data = validated_data.pop('grade')
        participant_design_data = validated_data.pop('participant_design')
        implemented_data = validated_data.pop('implemented')

        #study_id, _ = Study.objects.get_or_create(**study_id)
        study_design, _ = StudyDesign.objects.get_or_create(**study_design_data)
        risks, _ = RiskOfBias.objects.get_or_create(**risks_data)
        grade, _ = Grade.objects.get_or_create(**grade_data)
        participant_design, _ = ParticipantDesign.objects.get_or_create(**participant_design_data)
        implemented, _ = Implementation.objects.get_or_create(**implemented_data)







        experiment = Experiment.objects.create(
            # study_id=study_id,
            study_design=study_design,
            risks=risks,
            grade=grade,
            participant_design=participant_design,
            implemented=implemented,
            **validated_data
        )
        return experiment


