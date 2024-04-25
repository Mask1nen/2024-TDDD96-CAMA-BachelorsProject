from rest_framework import serializers
from ..models import CamaUser
from .study import StudySerializer

import logging
logger = logging.getLogger(__name__)

 
class CamaUserSerializer(serializers.ModelSerializer):
    studies = StudySerializer(read_only=True, many=True)
    class Meta:
        model = CamaUser
        fields = ['orc_id', 'name', 'studies']