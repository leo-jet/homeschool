'''
Created on 27 oct. 2016

@author: leo
'''
from django import forms

from .models import Exercice

class ExerciceForm(forms.ModelForm):
    
    class Meta:
        model = Exercice
        fields = ('manuel', 'chapitre', 'section', 'Page', 'dateCreation', 'correction', 'consigneText','correctionTex')
