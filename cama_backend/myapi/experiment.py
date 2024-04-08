from django.db import models
from .study import Study

# Create your models here.

class StudyDesign(models.Model):
    design = models.CharField(max_length=255, primary_key=True)

class RiskOfBias(models.Model):
    id = models.IntegerField(primary_key=True)
    rob = models.CharField(max_length=255)
    robins = models.CharField(max_length=255)

class Grade(models.Model):
    grade = models.CharField(max_length=255)

class ParticipantDesign(models.Model):
    design = models.CharField(max_length=255)

class Implementation(models.Model):
    implementor = models.CharField(max_length=255)

class Experiment(models.Model):
    study_id = models.ForeignKey(Study, on_delete=models.CASCADE)
    experiment_nr = models.IntegerField()
    study_design = models.ForeignKey(StudyDesign, null=True, on_delete=models.SET_NULL)
    risks = models.ForeignKey(RiskOfBias, null=True, on_delete=models.SET_NULL)
    grade = models.ForeignKey(Grade, null=True, on_delete=models.SET_NULL)
    participant_design = models.ForeignKey(ParticipantDesign, null=True, on_delete=models.SET_NULL)
    implemented = models.ForeignKey(Implementation, null=True, on_delete=models.SET_NULL)
    gender_1 = models.DecimalField(null=True, max_digits=3, decimal_places=3)
    gender_2 = models.DecimalField(null=True, max_digits=3, decimal_places=3)
    intensity_n = models.IntegerField(null=True)
    duration_week = models.IntegerField(null=True)
    frequency_n = models.IntegerField(null=True)
    outcome = models.CharField(max_length=255, null=True)
    outcome_full = models.CharField(max_length=255, null=True)

    class Meta:
        unique_together = (("study_id", "experiment_nr"),)