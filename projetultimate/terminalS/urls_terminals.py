'''
Created on 11 nov. 2016

@author: leo
''' 
from django.conf.urls import  url
import views 
from accounts.views import (login_view, register_view, logout_view)
 
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^exercice/(?P<chapitre>\w+)$', views.list_exo, name='list_exercice'),
    url(r'^testcart/$', views.testcart, name='test_cart'),
    url(r'^mesclasses/$', views.mesclasses, name='mesclasses'),
    url(r'^accueil/$', views.accueil, name='accueil'),
    url(r'^ajoutEleve/$', views.ajouterEleve, name='ajouterEleve'),
    url(r'^qcm/$', views.qcm, name='qcm'),
    url(r'^login/$', login_view, name='login'),
    url(r'^mathsQuizz/$', views.mathsQuizz, name='mathsQuizzTS'),
    url(r'^logout/$', logout_view, name='logout'),
    #url par niveau
    url(r'^maths/$', views.mathsAccueil, name='maths'),
    url(r'^maths/(?P<typeEx>[\w\-]+)/$', views.mathsAccueil, name='maths'),
    url(r'^maths/(?P<typeEx>[\w\-]+)/(?P<niveau>[\w\-]+)/$', views.mathsAccueil, name='maths'),
    url(r'^maths/(?P<typeEx>[\w\-]+)/(?P<niveau>[\w\-]+)/(?P<chapitre>[\w\-]+)/$', views.mathsAccueil, name='maths'),
    url(r'^maths/(?P<typeEx>[\w\-]+)/(?P<niveau>[\w\-]+)/(?P<chapitre>[\w\-]+)/(?P<section>[\w\-]+)/$', views.mathsAccueil, name='maths'),
    
    url(r'^correction/(?P<id>[\w\-]+)/$', views.corerction, name='correction_exo'),
    url(r'^modifier/(?P<id>[\w\-]+)/$', views.modifier, name='modifier'),
    url(r'^imprimer/(?P<list>[\w\-]+(,[\w\-]+)*)/$', views.imprimer, name='imprimer'),
    
    url(r'^chapitreAjax/$', views.chapitreAjax, name='chapitreAjax'),
    url(r'^sectionAjax/$', views.sectionAjax, name='sectionAjax'),
    url(r'^exercicesAjax/$', views.exercicesAjax, name='exercicesAjax'),
    url(r'^FicheImpressionAjax/$', views.FicheImpressionAjax, name='FicheImpressionAjax'),
]