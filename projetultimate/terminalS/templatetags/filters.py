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