#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from projetultimate import settings
from django.db import models
from django.shortcuts import redirect
from .models import Exercice
from .form import ExerciceForm
from datetime import datetime
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from subprocess import Popen, PIPE
from backports import tempfile
import os
import codecs


# Create your views here.

def charger_exercice():
    with codecs.open("/home/leo/Bureau/dossier latex/arithmetiques.tex", mode="r+", encoding='utf8') as fp2:
        fichier = []
        for line in fp2:
                fichier.append(line)
        exercices = {}
        i = 0
        n = 0
        for line in fichier: 
            if "\paragraph*{}" in line:
                j = i+1
                n = n+1
                exercice = []
                while j<len(fichier) and len(fichier[j])>1:
                    exercice.append(fichier[j])
                    j = j+1
                exercices[str(n)] = exercice
                exo = Exercice(manuel = "CIAM" , 
                               chapitre = "Arithmétiques" , 
                               section = "..",
                               numero = str(n) ,
                               Page = "" ,
                               correction = "non",
                               consigneText = ' '.join(exercice),
                               correctionTex = "non")                
                exo.save()
            i = i + 1
        
        
def index(request):
    n = 0
    return render(request, "index.html", {"nombre":n})

def testcart(request):
    n = 0
    return render(request, "testcart.html", {"nombre":n})

def list_exo(request, chapitre=None):
    queryset = Exercice.objects.filter(chapitre=chapitre)
    content = {
        "url": settings.STATIC_URL,
        "exercices_list": queryset,
        }
    return render(request, "list_exo.html", content)

def corriger(request):
    return render(request, "corriger.html", {})

def corerction(request, id=None):
    instance = get_object_or_404(Exercice, id=id)
    content = {
        'correction': instance.correction_tex,
        }
    return render(request, "correction.html", content)

def modifier(request, id=None):
    instance = get_object_or_404(Exercice, id=id)
    formu = ExerciceForm(request.POST or None, instance=instance)
    if formu.is_valid():
        instance = formu.save(commit=False)
        instance.save()
        return redirect('home')
        
    content = {
        'correction': instance.consigneText,
        'instance': instance, 
        'form': formu,
        }
    return render(request, "modifier.html", content)

def imprimer(request, list=None):
    liste_id = list.split(',')
    liste_exercice = []
    for id in liste_id:
        instance = Exercice.objects.get(id=id) 
        liste_exercice.append(instance)
    context = Context({
        'content': liste_exercice,
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
    r.write(pdf)
    return r

def qcm(request):
    return render(request, "qcm.html", {})