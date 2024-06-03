from rest_framework import serializers
from ..models import CamaUser
from .study import StudySerializer

import logging
logger = logging.getLogger(__name__)

class CamaUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CamaUser model.
    
    Converts CamaUser model objects into JSON representations during GET-requests.
    Provides a nested representation of related studies.
    """
    studies = StudySerializer(read_only=True, many=True)
    class Meta:
        model = CamaUser
        fields = ['orc_id', 'name', 'studies']