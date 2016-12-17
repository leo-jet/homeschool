#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 14 déc. 2016

@author: leo
'''
from sympy import *

'''
calcul de limites

'''
#limites d'un polynome
def limitePolynomeDegrePaire(a, b, c, n1, n2):
    x = Symbol("x")
    P = a*(x**n1)+b*(x**n2)+c
    return P

a = limitePolynomeDegrePaire(-2,-3,-5,6,3)

print "l'équation est égale à " + "$" +latex(a)+"$"