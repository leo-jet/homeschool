# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.core.paginator import Page

# Create your models here.
AD = "Adamaoua" 
CE = "Centre" 
ES = "Est "
EX ="ExtremeNord "
LI ="Littoral" 
NO = "Nord" 
NOO = "Nord-Ouest"
OU = "Ouest" 
SU = "Sud" 
SUO = "Sud-Ouest" 

MAT = "MATHEMATIQUES"
PHY = "PHYSIQUES"
CHI = "CHIMIE"
SVT = "SCIENCE DE LA VIE ET DE LA TERRE"

MATIERE_CHOIX = (
    (MAT, "MATHEMATIQUES"),
    (PHY, "PHYSIQUES"),
    (CHI, "CHIMIE"),
    (SVT, "SCIENCE DE LA VIE ET DE LA TERRE"),
    )

TLEA = "Terminale A"
TLEB = "Terminale A"
TLEC = "Terminale C"
TLED = "Terminale D"
TLEE = "Terminale E"

PREA = "PREMIERE A"
PREB = "PREMIERE B"
PREC = "PREMIERE C"
PRED = "PREMIERE D"
PREE = "PREMIERE E"
ET = "Enseignement Technique"
EG = "Enseignement Génerale"
NIVEAU_CHOIX = (
    (EG, (
            (TLEA, "Terminale A"),
            (TLEB, "Terminale B"), 
            (TLEC, "Terminale C"), 
            (TLED, "Terminale D"), 
            (TLEE, "Terminale E"), 
        )
     ), 
    )

REGION_CAMEROUN_CHOIX = (
    (AD, "Adamaoua"),
    (CE, "Centre"), 
    (ES, "Est"),
    (EX, "Extrême-Nord"), 
    (LI, "Littoral"),
    (NO, "Nord"),
    (NOO, "Nord-Ouest"), 
    (OU, "Ouest"),
    (SU, "Sud"),
    (SUO, "Sud-Ouest"),
)
FR = "FRANCOPHONE"
ANGL = "ANGLOPHONE"
BIL = "BILINGUE"
SECTION_CHOIX = (
    (FR, "FRANCOPHONE"),
    (ANGL, "ANGLOPHONE"),
    (BIL, "BILINGUE"),
    )
GEN = "GENERAL"
TECH = "TECHNIQUE"
TYPE_ENSEIGNEMENT_CHOIX = (
    (GEN, "GENERAL"),
    (TECH, "TECHNIQUE"),
    )
ARRONDISSEMENT_CHOIX = (
    (CE, (
            ('MBANDJOCK', 'BANDJOCKS'),
            ('MINTA', 'MINTA'),
        )
    ),
    (OU, (
            ('MBOUDA', 'MBOUDA'),
            ('BATCHAM', 'BATCHAM'),
        )
    ),
)



class Matiere(models.Model):
    id = models.AutoField(primary_key=True)
    intitule = models.CharField(max_length=128, choices = MATIERE_CHOIX, default=MAT)
    def __str__(self):
        return self.intitule
    class Meta:
        unique_together = (("intitule"),)

class NiveauClasse(models.Model):
    id = models.AutoField(primary_key=True)
    intitule = models.CharField(max_length=128, choices = NIVEAU_CHOIX, default=TLEC)
    def __str__(self):
        return self.intitule
    class Meta:
        unique_together = (("intitule"),)

class Personne(models.Model): 
    user = models.OneToOneField(User) 
    dateNaissance = models.DateField(auto_now=False)
    LieuNaissance = models.CharField(max_length=128, default="Test")
    region = models.CharField(max_length=128, choices = REGION_CAMEROUN_CHOIX, default=AD)
    departement = models.CharField(max_length=128, default="Test")
    arrondissement = models.CharField(max_length=128, choices = ARRONDISSEMENT_CHOIX)
    quartier = models.CharField(max_length=128, default="Test")
    longitude = models.CharField(max_length=128, default="Test")
    lattitude = models.CharField(max_length=128, default="Test")

    def __unicode__(self):
        return self.user.username
    def __str__(self):
        return self.user.username    
    
    class Meta:
        unique_together = (("user", "dateNaissance"),)
        abstract = True


class Enseignant(Personne):
    idEnseignant = models.CharField(max_length=128, primary_key=True, default="Test")
    niveau = models.ManyToManyField(NiveauClasse)
    specialite = models.CharField(max_length=128, default="Test") 
     
class Eleve(Personne):
    idEleve = models.CharField(max_length=128, primary_key=True, default="Test")
    niveau = models.ForeignKey(NiveauClasse)
    def __unicode__(self):
        return self.user.username
    def __str__(self):
        return self.user.username

class Cours(models.Model):
    idCours = models.CharField(max_length=128, primary_key=True, default="COURS")
    intitule = models.CharField(max_length=128, choices = MATIERE_CHOIX, default = MAT)
    enseignant = models.ManyToManyField(Enseignant)
    def __unicode__(self):
        return self.intitule
    def __str__(self):
        return self.intitule

class Chapitre(models.Model):
    idChapitre = models.CharField(max_length=128, primary_key=True, default="Test")
    intitule = models.CharField(max_length=128, default="Test")
    niveau = models.ForeignKey(NiveauClasse)
    cours = models.ForeignKey(Cours)
    
    def __unicode__(self):
        return self.intitule
    def __str__(self):
        return self.intitule


class Section(models.Model):
    idSection = models.CharField(max_length=128, primary_key=True, default="Test")
    intitule = models.CharField(max_length=128, default="Test")
    chapitre = models.ForeignKey(Chapitre)
    def __unicode__(self):
        return self.intitule
    def __str__(self):
        return self.intitule    

class Proposition(models.Model):
    idProposition = models.CharField(max_length=128, primary_key=True, default="Test")
    enonce = models.CharField(max_length=128, default="Test")
    solution = models.CharField(max_length=128, default="Test")
    point = models.DecimalField(max_digits=3, decimal_places=2)
    checked = models.CharField(max_length=128, default="Test")
    
    def __unicode__(self):
        return self.enonce
    def __str__(self):
        return self.enonce
    class Meta:
        unique_together = (("enonce"),)
    

class Question(models.Model):
    idQuestion = models.CharField(max_length=128, primary_key=True, default="Test")
    enonce = models.CharField(max_length=128, default="Test")
    figure = models.CharField(max_length=128, default="Test")
    choixMultiple = models.CharField(max_length=128, default="Test")
    explication = models.TextField(max_length=500, default="Test")
    niveauDifficulte = models.IntegerField(default=0)
    section = models.ForeignKey(Section)
    propositions = models.ManyToManyField(Proposition)
    def __unicode__(self):
        return self.enonce
    def __str__(self):
        return self.enonce
    class Meta:
        unique_together = (("enonce"),)
    

class Exercice(models.Model):
    idExercice = models.CharField(max_length=128, primary_key=True, default="Test")
    section = models.ForeignKey(Section)
    dateCreation = models.DateField(auto_now=True)
    correction = models.BooleanField(default=False)
    publier = models.BooleanField(default=False)
    consigneTexte = models.TextField(default="Test")
    correctionTexte = models.TextField(default="Test2")
    
    def __unicode__(self):
        return self.idExercice
    def __str__(self):
        return self.idExercice
    
    
class Etablissement(models.Model):
    nom = models.CharField(max_length=128, default="Test")
    region = models.CharField(max_length=128, choices = REGION_CAMEROUN_CHOIX, default=AD)
    departement = models.CharField(max_length=128, default="Test")
    arrondissement = models.CharField(max_length=128, choices = ARRONDISSEMENT_CHOIX, default=CE)
    section = models.CharField(max_length=128, choices = SECTION_CHOIX)
    type_enseignement = models.CharField(max_length=128, choices = TYPE_ENSEIGNEMENT_CHOIX)
    quartier = models.CharField(max_length=128, default="Test")
    longitude = models.CharField(max_length=128, default="Test")
    lattitude = models.CharField(max_length=128, default="Test")
    
    def __unicode__(self):
        return self.nom
    def __str__(self):
        return self.nom    
    
class Quizz(models.Model):
    idQuizz = models.CharField(max_length=128, primary_key=True, default="Test")
    dateCreationQuizz = models.DateTimeField(auto_now=True)
    intitule = models.CharField(max_length=128, default="Test")
    question = models.ManyToManyField(Question)
    eleve = models.ManyToManyField(Eleve)
    enseignant = models.ForeignKey(Enseignant)
    
    class Meta:
        unique_together = (("dateCreationQuizz", "intitule"),)
        
    def __unicode__(self):
        return self.intitule
    def __str__(self):
        return self.intitule    
    
    
class College(Etablissement):
    idCollege = models.CharField(max_length=128, primary_key=True, default="Test")
    directeur = models.CharField(max_length=128, default="Test")
    def __unicode__(self):
        return self.nom
    def __str__(self):
        return self.nom    
    
class Lycee(Etablissement):
    idLycee = models.CharField(max_length=128, primary_key=True, default="Test")
    principal = models.CharField(max_length=128, default="Test")
    def __unicode__(self):
        return self.nom
    def __str__(self):
        return self.nom    
    
    
class Universite(Etablissement):
    idLycee = models.CharField(max_length=128, primary_key=True, default="Test")
    recteur = models.CharField(max_length=128, default="Test")
    def __unicode__(self):
        return self.nom
    def __str__(self):
        return self.nom    
    
class GroupeDeSoutien(Etablissement):
    idGroupeDeSoutien = models.CharField(max_length=128, primary_key=True, default="Test")
    def __unicode__(self):
        return self.nom
    def __str__(self):
        return self.nom   
    
    
class EleveInscritA(models.Model):
    etablissement = models.ForeignKey(Etablissement)
    eleve = models.ForeignKey(Eleve)
    cours = models.ForeignKey(Cours)
    annee = models.DateField(auto_now=False)
    
    class Meta:
        unique_together =("etablissement", "eleve", "cours", "annee")
    
    def __str__(self):
        return str(self.eleve)    
    
class EnseigneA(models.Model):
    annee = models.DateField(auto_now=False)
    etablissement = models.ForeignKey(Etablissement)
    enseignant = models.ForeignKey(Enseignant) 
    
    class Meta:
        unique_together = ("annee", "etablissement", "enseignant")
    def __str__(self):
        return str(self.enseignant)   
    
        
class RepondA(models.Model):
    eleve = models.ForeignKey(Eleve)
    quizz = models.ForeignKey(Quizz)
    note = models.DecimalField(max_digits=2, decimal_places=1)
    dateReponQuizz = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ("dateReponQuizz", "quizz")
        
    def __str__(self):
        return str(self.eleve)  

    
class Classe(models.Model):
    idClass = models.CharField(max_length=128, primary_key=True, default="Test")
    enseignant = models.ForeignKey(Enseignant)
    etablissement = models.ForeignKey(Etablissement)
    niveau = models.ForeignKey(NiveauClasse)
    eleves = models.ManyToManyField(Eleve)
    def __unicode__(self):
        return self.idClass
    def __str__(self):
        return self.idClass
    
class FicheEleve(models.Model):
    idFiche = models.AutoField(primary_key=True)
    createur = models.ForeignKey(Eleve)
    dateCreation = models.DateTimeField(auto_now=True)
    intitule = models.CharField(max_length=128, default="Test")
    url = models.CharField(max_length=128, default="Test")
    def __unicode__(self):
        return self.intitule
    def __str__(self):
        return self.intitule
    class Meta:
        unique_together = (("url"),)