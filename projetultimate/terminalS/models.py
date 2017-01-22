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
    

class Question(models.Model):
    enonce = models.CharField(max_length=128)
    figure = models.CharField(max_length=128)
    choixMultiple = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.enonce
    def __str__(self):
        return self.enonce
    
class Proposition(models.Model):
    enonce = models.CharField(max_length=128)
    solution = models.CharField(max_length=128)
    point = models.CharField(max_length=128)
    checked = models.CharField(max_length=128)
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.enonce
    def __str__(self):
        return self.enonce

class Personne(models.Model): 
    nom = models.CharField(max_length=128)
    prenom = models.CharField(max_length=128)
    dateNaissance = models.DateField(auto_now=False)
    LieuNaissance = models.CharField(max_length=128)
    region = models.CharField(max_length=128)
    departement = models.CharField(max_length=128)
    arrondissement = models.CharField(max_length=128)
    quartier = models.CharField(max_length=128)
    longitude = models.CharField(max_length=128)
    lattitude = models.CharField(max_length=128)

    def __unicode__(self):
        return self.nom
    def __str__(self):
        return self.nom    
    
class Etablissement(models.Model):
    nom = models.CharField(max_length=128)
    region = models.CharField(max_length=128)
    departement = models.CharField(max_length=128)
    arrondissement = models.CharField(max_length=128)
    quartier = models.CharField(max_length=128)
    longitude = models.CharField(max_length=128)
    lattitude = models.CharField(max_length=128)
