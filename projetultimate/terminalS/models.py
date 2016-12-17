from django.db import models
from django.core.paginator import Page

# Create your models here.
class Exercice(models.Model):
    
    manuel = models.CharField(max_length=128)
    chapitre = models.CharField(max_length=128)
    section = models.CharField(max_length=128)
    numero =  models.CharField(max_length=8)
    Page = models.CharField(max_length=128)
    dateCreation = models.DateField()
    correction = models.CharField(max_length=128)
    consigneText = models.TextField()
    correctionTex = models.TextField()
    
    def __unicode__(self):
        return self.manuel
    def __str__(self):
        return self.manuel