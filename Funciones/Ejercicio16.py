# -*- coding: utf-8 -*-
"""
Crear una funcion que muestre el seno, coseno y tangente de un numero N

@author: Richard Jimenez
"""
import math

def calculate(num):
    angle = math.radians(num)
    seno = math.sin(angle)
    coseno = math.cos(angle)
    tangente = math.tan(angle)
    
    print('Seno: {}\nCoseno: {}\nTangente: {}'.format(seno, coseno, tangente))
    
calculate(30)
