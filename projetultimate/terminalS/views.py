#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from projetultimate import settings
from django.db import models
from django.shortcuts import redirect
from .models import Exercice
from .form import ExerciceForm
from datetime import datetime
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from subprocess import Popen, PIPE
from backports import tempfile
import os
import codecs
from terminalS.models import *
import json
from django.contrib.auth.decorators import login_required
from accounts.models import Enseignant, Classe
from django.forms.models import model_to_dict
from collections import namedtuple
from operator import attrgetter
from accounts.forms import *
from gtk.keysyms import section
# Create your views here.

        
@login_required(login_url ="/terminals/login/")
def index(request):
    n = 0
    return render(request, "index.html", {"nombre":n})

def testcart(request):
    n = 0
    return render(request, "testcart.html", {"nombre":n})


@login_required(login_url="/terminals/login")
def list_exo(request, chapitre=None):
    queryset = Exercice.objects.filter(chapitre=chapitre)
    content = {
        "url": settings.STATIC_URL,
        "exercices_list": queryset,
        }
    return render(request, "list_exo.html", content)

@login_required(login_url="/terminals/login")
def corriger(request):
    return render(request, "corriger.html", {})
@login_required(login_url="/terminals/login")
def corerction(request, id=None):
    instance = get_object_or_404(Exercice, idExercice=id)
    content = {
        'correction': instance.correctionTexte,
        }
    return render(request, "correction.html", content)


@login_required(login_url="/terminals/login")
def modifier(request, id=None):
    instance = get_object_or_404(Exercice, idExercice=id)
    formu = ExerciceFormAccount(request.POST or None, instance=instance)
    if formu.is_valid():
        instance = formu.save(commit=False)
        instance.save()
        return redirect('accueil')
        
    content = {
        'correction': instance.consigneTexte,
        'instance': instance, 
        'form': formu,
        }
    return render(request, "modifier.html", content)


@login_required(login_url="/terminals/login")
def imprimer(request, list=None):
    liste_id = list.split(',')
    liste_exercice = []
    for id in liste_id:
        instance = Exercice.objects.get(idExercice=id) 
        liste_exercice.append(instance)
    context = Context({
        'content': liste_exercice,
        'user': request.user,
        })
    template = get_template('latex_template.tex')
    rendered_tpl = template.render(context).encode('utf-8')
    with tempfile.TemporaryDirectory() as tempdir:
        for i in range(2):
            process = Popen(
                ['pdflatex', '-output-directory', tempdir],
                stdin=PIPE,
                stdout=PIPE,
            )
        process.communicate(rendered_tpl)
        with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:
            pdf = f.read()
    r = HttpResponse(content_type='application/pdf')
    r['Content-Disposition'] = 'attachment; filename="exercice.pdf"'
    r.write(pdf)
    return r


@login_required(login_url="/terminals/login")
def qcm(request):
    setQuestion = Question.objects.all()
    j = 1
    quest = {}
    for question in setQuestion:
        propositions = Proposition.objects.filter(Question__enonce=question.enonce)
        prop = {}
        i = 1
        for propo in propositions:
            prop[''.join(["propo",str(i)])] = {
                "enonce": propo.enonce, 
                "solution": propo.solution, 
                "point" : propo.point, 
                "checked": propo.checked
            }
            i = i + 1
        quest[''.join(["question",str(j)])] = {
            "enonce": question.enonce,
            "figure": question.figure, 
            "choixMultiple" : question.choixMultiple,
            "propositions": prop
        }
        j = j + 1
    '''with open("/home/leo/Bureau/quizz.json", "w") as fichierJson:
        json.dump(quest, fichierJson)'''
    return render(request, "qcm.html", {"question":quest, "a":"a"})
@login_required(login_url="/terminals/login")
def mathsQuizz(request):
    return render(request, "mathsQuizzTS.html", {})

def mesclasses(request):
    
    if request.user.is_anonymous():
        print "hello"
    else :
        group = request.user.groups.values_list('name', flat=True)[0]
        
    enseignant = Enseignant.objects.get(user=request.user)
    classSet = Classe.objects.filter(enseignant=enseignant)
    
    ClasseCours = namedtuple("Classe", ["id", "niveau", "etablissement", "eleves"])
    
    i = 0
    mesclasses2 = []
    classes2 = []
    etsActu = ""
    for c in classSet:
        
        # __str__() permet d'enlever le type de la colonne. Par exemple <NiveauClasse: terminal C> devient le string terminal c
        niveau = (c.niveau).__str__()
        etablissement = (c.etablissement).__str__()
        eleves = []
        for e in c.eleves.all():
            eleves.append(e.user.first_name)
        classe2 = ClasseCours(i, niveau, etablissement, eleves)
        mesclasses2.append(classe2)
        i = i + 1
   
    mesclasses2 = sorted(mesclasses2, key=attrgetter('etablissement')) 
    i = 0 
    if i < len(mesclasses2):
        etsActu = mesclasses2[i].etablissement
    classes2 = []
    mesclasse = []
    id = 0;
    while i < len(mesclasses2):
        if(etsActu == mesclasses2[i].etablissement):
            classes2.append({"niveau": mesclasses2[i].niveau, "eleves": mesclasses2[i].eleves})
        else :
            mesclasse.append({"etablissement": etsActu, "classes": classes2, "id":id})
            etsActu = mesclasses2[i].etablissement
            classes2 = []
            i = i - 1
            id = id + 1
        i = i + 1
    #pour le dernier 
    if(i==len(mesclasses2)):
        mesclasse.append({"etablissement": etsActu, "classes": classes2, "id":id})

    return render(request, "mesclasses.html", {"group": group, "classes": mesclasse})



@login_required(login_url="/terminals/login")
def accueil(request):
    '''
        group : contient le group de l'utilisateur 
    '''
    fiches = ""
    if request.user.is_anonymous():
        print "hello"
    else :
        group = request.user.groups.values_list('name', flat=True)[0]
        if group == "eleves":
            fiches = FicheEleve.objects.filter(createur=Eleve.objects.get(user=request.user))
    
    '''
        Si c'est un eleve il :
        - la liste de ses cours où il est inscrit
    '''
    
    
    '''
        group : le groupe de l'utilisateur
    '''
    return render(request, "accueil.html", {"group":group, "fiches": fiches})


@login_required(login_url="/terminals/login")
def ajouterEleve(request):
    eleveForm = EleveForm()
    if request.user.is_anonymous():
        print "hello"
    else :
        group = request.user.groups.values_list('name', flat=True)[0]
            
    return render(request, "ajouterEleve.html", {"e":eleveForm, "group":group })

'''
    typeEx : type d'exercices (quizz, entrainement, approfondissement)
    niveau : niveau de la classe
    chapitre : chapitre
    section : section du chapitre
'''
@login_required(login_url="/terminals/login")
def mathsAccueil(request, typeEx = None, niveau = None, chapitre=None, section = None):    
    
    if request.user.is_anonymous():
        print "hello"
    else :
        group = request.user.groups.values_list('name', flat=True)[0]
        
        #si cest un eleve on prend son niveau
        niveauE = ''
        if group == "eleves":
            e = Eleve.objects.get(user = request.user)
            niveauE = e.niveau
            niveau = niveauE
    
    return render(request, "mathsAccueil.html", {"group":group, "niveau":niveauE})



'''
    requête ajax
    
    retour
        data : objet de type json
'''
@login_required(login_url="/terminals/login")
def chapitreAjax(request):
    leschapitres = []
    if request.is_ajax():
        niveau = request.GET["niveau"]
        chapitres = Chapitre.objects.filter(niveau__intitule=niveau, cours__intitule="MATHEMATIQUES")
        for c in chapitres : 
            leschapitres.append(c.intitule)
        data = json.dumps(leschapitres)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404
    
def sectionAjax(request):
    lessections = []
    if request.is_ajax():
        chapitre = request.GET["chapitre"]
        sections = Section.objects.filter(chapitre__intitule=chapitre)
        for s in sections:
            lessections.append(s.intitule)
        data = json.dumps(lessections)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404
    
def exercicesAjax(request):
    lesexercices = []
    section = request.GET["section"]
    exercices = Exercice.objects.filter(section__intitule=section)
    for e in exercices:
        lesexercices.append({"id":e.idExercice,"consigne":e.consigneTexte, "correction": e.correction})
        
        
    if request.user.is_anonymous():
        print "hello"
    else :
        group = request.user.groups.values_list('name', flat=True)[0]
    
    print group
    
    return render(request, "divExercice.html", {"exercices":lesexercices, "group":group })


def FicheImpressionAjax(request):
    if request.is_ajax():
        urlFiche = request.GET["urlFiche"]
        fiche = FicheEleve(url=urlFiche, createur=Eleve.objects.get(user=request.user))
        fiche.save()
        return render(request, "divExercice.html", {})
    else:
        raise Http404











