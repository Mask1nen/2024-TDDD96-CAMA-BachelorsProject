from django.db import models
from .experiment import Experiment
from .study import Study

# Create your models here.

class EffectData(models.Model):
    effect_size_number = models.IntegerField()
    study_id = models.ForeignKey(Study, on_delete=models.CASCADE)
    experiment_nr = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    sd1i = models.FloatField(null=True)
    sd2i = models.FloatField(null=True)
    n1i = models.FloatField(null=True)
    n2i = models.FloatField(null=True)
    m1i = models.FloatField(null=True)
    m2i = models.FloatField(null=True)
    d_var = models.FloatField(null=True)
    d = models.FloatField(null=True)
    f_stat = models.FloatField(null=True)
    t = models.FloatField(null=True)
    ri = models.IntegerField(null=True)
    mean_age = models.FloatField(null=True)
    ni = models.IntegerField(null=True)
    icc = models.FloatField(null=True)
    ai = models.IntegerField(null=True)
    bi = models.IntegerField(null=True)
    ci = models.IntegerField(null=True)
    di = models.IntegerField(null=True)

    class Meta:
        unique_together = (("effect_size_number", "study_id", "experiment_nr"),)