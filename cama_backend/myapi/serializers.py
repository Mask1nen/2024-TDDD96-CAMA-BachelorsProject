from rest_framework import serializers
from .models import Study, Year, Country, Category
from .camauser import CamaUser

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

        uploader = CamaUser.objects.create(**uploader_data)
        study_year = Year.objects.create(**study_year_data)
        country = Country.objects.create(**country_data)
        category = Category.objects.create(**category_data)

        study = Study.objects.create(
            uploader=uploader,
            study_year=study_year,
            country=country,
            category=category,
            **validated_data
        )
        return study
