#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 19 dec. 2016

@author: leo
'''
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import *



from django.contrib.auth import (
    authenticate, 
    get_user_model,
    login,
    logout,
    )

from models import *
from django.forms import ModelForm
from crispy_forms.layout import Layout, Submit, Div


User = get_user_model()

from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Password'}))
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        
        user = authenticate(username=username, password=password)
        
        if not user:
            raise forms.ValidationError("l'utilisateur n'existe pas")
        
        if not user.check_password(password):
            raise forms.ValidationError("mot de pass incorrect")
        
        if not user.is_active:
            raise forms.ValidationError("Cet utilisateur n'est plus actif")
        
        return super(UserLoginForm, self).clean(*args, **kwargs)


class EleveForm(ModelForm):
    class Meta:
        model = Eleve
        fields = '__all__'
        
class ExerciceFormAccount(ModelForm):
    
    def __init__(self, *args, **kwargs):
        
        super(ExerciceFormAccount, self).__init__(*args, **kwargs)
        
        #utilisation de FormHelper pour customiser le formulaire
        self.helper = FormHelper()
        
        #id et class boostrap du formulaire
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id ="exercice-form"
        
        #definition de la taille des labels et des champs sur la grille
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-4'
        
        #affichage du formulaire
        self.helper.layout = Layout(
            Div('consigneTexte', css_class='row'),
            Div('correctionTexte', css_class='row'),
            Div(
                Div(Submit('save', 'Modifier'), css_class='col-md-12'), css_class='row'
            )
        )
    
    class Meta:
        model = Exercice
        fields = [
            "consigneTexte",
            "correctionTexte",
        ]
        labels = {
            'consigneTexte': "Enoncé", 
            'correctionTexte': "Correction"
        }