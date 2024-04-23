from django.db import models
from .camauser import CamaUser

# Create your models here.


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)

class Study(models.Model):
    study_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    uploader = models.ForeignKey(CamaUser, null=True, on_delete=models.SET_NULL)
    study_year = models.IntegerField(null=False)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    peer_reviewed = models.BooleanField(null=False)
    authors = models.CharField(max_length=255, null=False)
    doi = models.CharField(max_length=255, null=False)
    abstract = models.CharField(max_length=3000, null=False)
    keywords = models.CharField(max_length=255, null=False)
    nr_downloads = models.IntegerField(null=True)
    approved = models.BooleanField(null=False, default=False)


    def get_uploader(self):
        return self.uploader.orc_id