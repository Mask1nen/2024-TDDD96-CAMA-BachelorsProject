from django.db import models
from .camauser import CamaUser
from .study import Country, Category, Study
from .experiment import StudyDesign, RiskOfBias, Grade, ParticipantDesign, Implementation, Experiment
from .effect_data import EffectData, EffectSizeType, TestTime

def get_id_from_name(model, name):
    try:
        obj = model.objects.get(name=name)
        return obj.id
    except model.DoesNotExist:
        return None


# Mapping dictionary for field names to model names
FIELD_MODEL_MAP = {
    'study_design': StudyDesign,
    'participant_design': ParticipantDesign,
    'test_time': TestTime,
    'effect_size_type': EffectSizeType,
}
