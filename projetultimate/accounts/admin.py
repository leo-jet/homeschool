# -*- coding: utf-8 -*-
from django.contrib import admin 

# Register your models here.
from .models import * 
 
class NiveauClasseAdmin(admin.ModelAdmin):
    list_display = ("intitule","id")
    class Meta:
        model = NiveauClasse

class ExerciceAdmin(admin.ModelAdmin):
    list_display = ("idExercice", "section", "dateCreation", "correction","consigneTexte", "publier")
    class Meta:
        model = Exercice



class CoursAdmin(admin.ModelAdmin):
    list_display = ("intitule","idCours")
    class Meta:
        model = Cours
    
    
class ChapitreAdmin(admin.ModelAdmin):
    list_display = ("idChapitre", "intitule", "cours", "niveau")
    class Meta:
        model = Chapitre

class SectionAdmin(admin.ModelAdmin):
    list_display = ("idSection", "intitule", "chapitre")
    class Meta:
        model = Section
    
class QuestionAdmin(admin.ModelAdmin):
    list_diplay = ("idQuestion", "enonce", "figure", "choixMultiple", "section", "explication")
    class Meta:
        model = Question
    
class PropositionAdmin(admin.ModelAdmin):
    list_display =("idProposition", "enonce", "solution", "point", "checked")
    class Meta:
        model = Proposition
    
class EtablissementAdmin(admin.ModelAdmin):
    list_display = ("nom", "region", "section", "type_enseignement")
    class Meta:
        model = Etablissement

class EnseignantAdmin(admin.ModelAdmin):
    list_display = ("user",)
    class Meta:
        model = Enseignant
        
        
class EleveAdmin(admin.ModelAdmin):
    class Meta:
        model = Eleve
    
class QuizzAdmin(admin.ModelAdmin):
    list_display = ("idQuizz", "dateCreationQuizz", "intitule", "enseignant")
    class Meta:
        model = Quizz
        
        
class CollegeAdmin(EtablissementAdmin):
    class Meta:
        model = College 

class ClasseAdmin(admin.ModelAdmin):
    list_display = ("idClass", "enseignant", "etablissement", "niveau")
    class Meta:
        model = Classe

class LyceeAdmin(EtablissementAdmin):
    class Meta:
        model = Lycee
    
class GroupeDeSoutienAdmin(admin.ModelAdmin):
    class Meta:
        model = GroupeDeSoutien
    
class UniversiteAdmin(EtablissementAdmin):
    class Meta:
        model = Universite
    
class EleveInscritAAdmin(admin.ModelAdmin):
    list_display = ("id","etablissement", "eleve", "cours", "annee")
    class Meta:
        model = EleveInscritA
    
class EnseigneAAdmin(admin.ModelAdmin):
    list_display = ("id",'annee', "etablissement", "enseignant")
    class Meta:
        model = EnseigneA 
    
class RepondAAdmin(admin.ModelAdmin):
    list_display = ("id", "eleve", "quizz", "note", "dateReponQuizz")
    class Meta:
        model = RepondA
        
class FicheEleveAdmin(admin.ModelAdmin):
    list_display = ("idFiche", "createur", "intitule", "url","dateCreation" )
    class Meta:
        model = FicheEleve

    
admin.site.register(Exercice, ExerciceAdmin)
admin.site.register(Cours, CoursAdmin)
admin.site.register(Chapitre, ChapitreAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Proposition, PropositionAdmin)

admin.site.register(Etablissement, EtablissementAdmin)
admin.site.register(Enseignant, EnseignantAdmin)
admin.site.register(Eleve, EleveAdmin)
admin.site.register(Quizz, QuizzAdmin)
admin.site.register(College, CollegeAdmin)


admin.site.register(Lycee, LyceeAdmin)
admin.site.register(Universite, UniversiteAdmin)
admin.site.register(EleveInscritA, EleveInscritAAdmin)
admin.site.register(EnseigneA, EnseigneAAdmin)
admin.site.register(RepondA, RepondAAdmin)
admin.site.register(NiveauClasse, NiveauClasseAdmin)

admin.site.register(Classe, ClasseAdmin)
admin.site.register(GroupeDeSoutien, GroupeDeSoutienAdmin)


admin.site.register(FicheEleve, FicheEleveAdmin)