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
<<<<<<< HEAD
    cama_user = models.ForeignKey(CamaUser, null=True, on_delete=models.SET_NULL, related_name='studies')
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL, related_name='countries')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='categories')
    study_year = models.IntegerField(null=True)
    peer_reviewed = models.BooleanField(null=True)
    authors = models.CharField(max_length=255, null=True)
    doi = models.CharField(max_length=255, null=True)
    abstract = models.CharField(max_length=255, null=True)
    keywords = models.CharField(max_length=255, null=True)
    nr_downloads = models.CharField(max_length=255, null=True)
=======
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
    nr_downloads = models.IntegerField(null=True, default=0)
    approved = models.BooleanField(null=False, default=False)


    def get_uploader(self):
        return self.uploader.orc_id
>>>>>>> feat/471-api
