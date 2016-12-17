'''
Created on 11 nov. 2016

@author: leo
''' 
from django.conf.urls import  url
import views 
 
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^exercice/(?P<chapitre>\w+)$', views.list_exo, name='list_exercice'),
    url(r'^testcart/$', views.testcart, name='test_cart'),
    url(r'^qcm/$', views.qcm, name='qcm'),
    url(r'^correction/(?P<id>[0-9]+)/$', views.corerction, name='correction_exo'),
    url(r'^modifier/(?P<id>[0-9]+)/$', views.modifier, name='modifier'),
    url(r'^imprimer/(?P<list>\d+(,\d+)*)/$', views.imprimer, name='imprimer'),
]