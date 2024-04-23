from rest_framework import serializers
from ..models import Study, Country, Category, CamaUser
from .cama_user import CamaUserSerializer

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
    country = CountrySerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    uploader = CamaUserSerializer(read_only=True)

    class Meta:
        model = Study
        fields = ['study_id', 'title', 'uploader', 'study_year', 'country', 'category', 'peer_reviewed',
                  'authors', 'doi', 'abstract', 'keywords', 'nr_downloads', 'approved']
        
class StudyCreateSerializer(serializers.ModelSerializer):
    uploader = serializers.PrimaryKeyRelatedField(queryset=CamaUser.objects.all())
    country = serializers.SlugRelatedField(read_only = True, slug_field='country')
    category = serializers.SlugRelatedField(read_only = True, slug_field='category')

    class Meta:
        model = Study
        fields = ['title', 'uploader', 'study_year', 'country', 'category', 'peer_reviewed',
                  'authors', 'doi', 'abstract', 'keywords', 'nr_downloads', 'approved']