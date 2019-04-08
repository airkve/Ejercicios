# Crear una funcion que calcule el area o el volumen de un cilindro
# para definir area usar 'a' y 'v' para volumen

from math import pi

def areaVolGet(tipo, radio, altura):
    if tipo == 'a':
        return pi * (radio*radio)* altura
    elif tipo == 'v':
        return 2 * radio * altura

print(areaVolGet('a', 5, 7))
print(areaVolGet('v', 9, 20))