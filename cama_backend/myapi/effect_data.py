from django.db import models
from .experiment import Experiment

# Create your models here.

class TestTime(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.CharField(max_length=255, unique=True)

class EffectSizeType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

class EffectData(models.Model):
    effect_size_number = models.AutoField(primary_key=True)
    experiment_nr = models.ForeignKey(Experiment, on_delete=models.CASCADE, related_name="effects")
    effect_size_type = models.ForeignKey(EffectSizeType, on_delete=models.SET_NULL ,null=True)
    test_time = models.ForeignKey(TestTime, null=True, on_delete=models.PROTECT)
    test_name =models.CharField(max_length=255, null=False)

    outcome = models.CharField(max_length=255, null=False)
    outcome_full = models.CharField(max_length=255, null=False)
    outcome_op = models.CharField(max_length=255, null=False)

    gender_1 = models.IntegerField(null=True)
    gender_2 = models.IntegerField(null=True)
    gender_3 = models.IntegerField(null=True)

    d_var = models.FloatField(null=True)
    d = models.FloatField(null=True)
    f_stat = models.FloatField(null=True)
    t = models.FloatField(null=True)
    ri = models.FloatField(null=True)
    icc = models.FloatField(null=False)

    mean_age_1i = models.FloatField(null=True)
    mean_age_2i = models.FloatField(null=True)
    
    ai = models.IntegerField(null=True)
    bi = models.IntegerField(null=True)
    ci = models.IntegerField(null=True)
    di = models.IntegerField(null=True)

    sd1i = models.FloatField(null=True)
    sd2i = models.FloatField(null=True)
    n1i = models.FloatField(null=True)
    n2i = models.FloatField(null=True)
    m1i = models.FloatField(null=True)
    m2i = models.FloatField(null=True)
    
    approved = models.BooleanField(null=False, default=False)


    class Meta:
        unique_together = (("effect_size_number", "experiment_nr"))
