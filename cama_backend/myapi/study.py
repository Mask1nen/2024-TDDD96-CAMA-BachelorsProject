from django.db import models
from .camauser import CamaUser

# Create your models here.
class Year(models.Model):
    study_year = models.IntegerField(primary_key=True, serialize=True)

class Country(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=255)


class Study(models.Model):
    study_id = models.AutoField(primary_key=True)
    uploader = models.ForeignKey(CamaUser, null=True, on_delete=models.SET_NULL)
    study_year = models.ForeignKey(Year, null=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    peer_reviewed = models.BooleanField(null=True)
    authors = models.CharField(max_length=255, null=True)
    doi = models.CharField(max_length=255, null=True)
    abstract = models.CharField(max_length=255, null=True)
    keywords = models.CharField(max_length=255, null=True)
    nr_downloads = models.CharField(max_length=255, null=True)

    def get_uploader(self):
        return self.uploader.orc_id