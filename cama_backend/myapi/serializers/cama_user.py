from rest_framework import serializers
from ..models import CamaUser

import logging
logger = logging.getLogger(__name__)

 
class CamaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamaUser
        fields = ['orc_id', 'name', 'nr_uploads']