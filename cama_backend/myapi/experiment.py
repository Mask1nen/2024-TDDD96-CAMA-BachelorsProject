from django.db import models
from .study import Study

# Create your models here.

class StudyDesign(models.Model):
    id = models.AutoField(primary_key=True)
    design = models.CharField(max_length=255, unique=True)

class RiskOfBias(models.Model):
    id = models.AutoField(primary_key=True)
    rob = models.CharField(max_length=255, null=True)  

class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    k = models.BooleanField(default=False)
    first = models.BooleanField(default=False)
    second = models.BooleanField(default=False)
    third = models.BooleanField(default=False)
    forth = models.BooleanField(default=False)
    fifth = models.BooleanField(default=False)
    sixth = models.BooleanField(default=False)
    seventh = models.BooleanField(default=False)
    eighth = models.BooleanField(default=False)
    ninth = models.BooleanField(default=False)
    tenth = models.BooleanField(default=False)
    eleventh = models.BooleanField(default=False)
    twelfth  = models.BooleanField(default=False)
    
    class Meta:
        unique_together = (("k", "first", "second", "third", "forth", "fifth", "sixth",
                            "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"))

class ParticipantDesign(models.Model):
    id = models.AutoField(primary_key=True)
    design = models.CharField(max_length=255, unique=True)

class Implementation(models.Model):
    id = models.AutoField(primary_key=True)
    implementor = models.CharField(max_length=255, unique=True)
    

class Experiment(models.Model):
    study_id = models.ForeignKey(Study, on_delete=models.CASCADE, null=True, related_name='experiments')
    experiment_nr = models.AutoField(primary_key=True)
    study_design = models.ForeignKey(StudyDesign, null=True, on_delete=models.SET_NULL)
    risks = models.ForeignKey(RiskOfBias, null=True, on_delete=models.SET_NULL)
    robins = models.CharField(max_length=255, null=True)
    grade = models.ForeignKey(Grade, null=True, on_delete=models.SET_NULL)
    participant_design = models.ForeignKey(ParticipantDesign, null=True, on_delete=models.SET_NULL)
    implemented = models.ForeignKey(Implementation, null=True, on_delete=models.SET_NULL)
    intensity_n = models.IntegerField(null=True)
    duration_week = models.IntegerField(null=True)
    frequency_n = models.IntegerField(null=True)
    ni = models.IntegerField(null=False)
    intervention = models.CharField(max_length=255, null=False)
    intervention_op = models.CharField(max_length=255, null=False)
    target_population = models.CharField(max_length=255, null=False)
    mean_age = models.FloatField(null=True)
    source = models.CharField(max_length=255, null=True)
    approved = models.BooleanField(null=False, default=False)


    class Meta:
        unique_together = (("study_id", "experiment_nr"))
