# -*- coding: utf-8 -*-
'''
Created on 23 déc. 2016

@author: leo
'''

# Quizz limites de référence

from sympy import *
from sympy import oo as infinie

def limitesReference(n, choix, x0, dir):
    x = Symbol('x')
    fonctions = {
        "1": sqrt(1-x)+2*x, 
        "2": 1/x**(2*n-1),
        "3": x-sqrt(x**2+1),
        "5": sin(x)/x,
        "6": (cos(x)-1)/x,
        "7": sqrt(5-x)-sqrt(1-x)
    }
    return (limit(fonctions[choix], x, x0, dir=dir), latex(fonctions[choix]))

print limitesReference(5, "2", 0, "+")