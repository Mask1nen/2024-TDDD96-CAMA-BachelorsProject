from django.db import models
from .study import Study

# Create your models here.

class StudyDesign(models.Model):
    design = models.CharField(max_length=255, primary_key=True)

class RiskOfBias(models.Model):
    id = models.AutoField(primary_key=True)
    rob = models.CharField(max_length=255, null=True)
    robins = models.CharField(max_length=255, null=True)

class Grade(models.Model):
    grade = models.CharField(max_length=255)

class ParticipantDesign(models.Model):
    design = models.CharField(max_length=255)

class Implementation(models.Model):
    implementor = models.CharField(max_length=255)
    
class TargetPopulation(models.Model):
    target = models.CharField(max_length=255)

class Experiment(models.Model):
    study_id = models.ForeignKey(Study, on_delete=models.CASCADE, null=True, related_name='experiment')
    experiment_nr = models.AutoField(primary_key=True)
    study_design = models.ForeignKey(StudyDesign, null=True, on_delete=models.PROTECT)
    risks = models.ForeignKey(RiskOfBias, null=True, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, null=True, on_delete=models.SET_NULL)
    participant_design = models.ForeignKey(ParticipantDesign, null=True, on_delete=models.PROTECT)
    implemented = models.ForeignKey(Implementation, null=True, on_delete=models.SET_NULL)
    intensity_n = models.IntegerField(null=True)
    duration_week = models.IntegerField(null=True)
    frequency_n = models.IntegerField(null=True)
    ni = models.IntegerField(null=True)
    intervention = models.CharField(max_length=255, null=True)
    intervention_op = models.CharField(max_length=255, null=True)
    target_population = models.CharField(max_length=255, null=True)
    mean_age = models.FloatField(null=True)
    source = models.CharField(max_length=255, null=True)


    class Meta:
        unique_together = (("study_id", "experiment_nr"),)