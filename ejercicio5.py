# Pedir un numero hasta que se ingrese uno negativo.
# muestra en pantalla los numeros que se ingresan.

from random import randint

numero = int(input('Escribe un numero del 1 al 100: '))
randNum = randint(1, 100)

while numero != randNum:
    if numero > randNum:
        print('El numero es mayor.')
    else:
        print('El numero es menor')
    numero = int(input('Escribe un numero: '))
print('Acertaste el numero, felicidades!')