# -*- coding: utf-8 -*-
'''
Created on 4 janv. 2017

@author: leo
'''


import codecs
from accounts.models import *
from __builtin__ import str

'''
    Entrées : nomFichier (nom du fichier)
    Sorties : rien
    Cette fonction prend un fichier tex d'exercices type cnam qu'il enregistre dans la base
'''
def charger_exercice(nomFichier):
    with codecs.open(nomFichier, mode="r+", encoding='utf8') as fp2:
        fichier = []
        for line in fp2:
                fichier.append(line)
        exercices = {}
        i = 0
        n = 0
        # section par defaut à tout les exercices
        section = Section.objects.get(idSection="Test")
        for line in fichier: 
            if "\paragraph*{}" in line:
                j = i+1
                n = n+1
                exercice = []
                while j<len(fichier) and len(fichier[j])>1:
                    exercice.append(fichier[j])
                    j = j+1
                exercices[str(n)] = exercice
                exo = Exercice(idExercice = "ARITH"+str(n) , 
                               consigneTexte = ' '.join(exercice),
                               section = section)         
                exo.save()
            i = i + 1

def charger_etablissement(nomFichier):
    with codecs.open(nomFichier, mode="r+", encoding='utf8') as fp2:
        fichier = []
        region = ""
        idEts = 0
        ets = ""
        sectionEts = ""
        genEts = ""
        for line in fp2:
            if len(line)>0:
                if line[0] == "P":
                    region = str(line[3:]).strip()
                    print region 
                    print len(region)
                else :
                    #college = 1 ou lycee = 0
                    lycee = 1
                    #section anglophone, francophone, bilingue
                    sectionEts = "FRANCOPHONE"
                    #general = 1 ou technique = 0
                    genEts = "GENERAL"
                    
                    
                    ets = line[3:]
                    if "col" in ets or "Col" in ets : 
                        lycee = 0
                    if "high" in ets or "College" in ets:
                        sectionEts = "ANGLOPHONE"
                    if "Bili" in ets or "bili" in ets:
                        sectionEts = "BILINGUE"
                    if "Tech" in ets or "tech" in ets:
                        genEts = "TECHNIQUE"  
                    if lycee == 1: 
                        l = Lycee(idLycee = "LYC" + str(idEts), nom = ets, region =region,section = sectionEts, type_enseignement = genEts)
                        l.save()
                    else:
                        c = College(idCollege = "COL" + str(idEts), nom = ets, region =region,section = sectionEts, type_enseignement = genEts)
                        c.save()  
                    idEts = idEts + 1           
                fichier.append(line)           
                
#charger_exercice("/home/leo/Bureau/dossier latex/arithmetiques.tex")

#charger_etablissement("/home/leo/Bureau/ets")



















