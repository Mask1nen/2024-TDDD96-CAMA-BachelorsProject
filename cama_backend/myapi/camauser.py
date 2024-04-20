from django.db import models

# Create your models here.

class CamaUser(models.Model):
    cama_user_id = models.AutoField(primary_key=True)
    orc_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    organization = models.CharField(max_length=255, null=True)
    nr_uploads = models.IntegerField(null=True)
