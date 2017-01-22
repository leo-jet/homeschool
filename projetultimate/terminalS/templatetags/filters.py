'''
Created on 20 nov. 2016

@author: leo
'''
from django import template

register = template.Library()

@register.filter
def get_type(value):
    return type(value)

@register.filter
def rest_div_3(value):
    return value % 3

@register.filter
def compareToProposition(value):
    if value == "propositions":
        return 0
    return 1

@register.filter
def compareToString(value, string):
    if value == string :
        return 1
    return 0

@register.filter
def toString(value):
    return str(value)       