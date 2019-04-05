# Pedir un numero hasta que se ingrese uno negativo.
# muestra en pantalla los numeros que se ingresan.

numero = int(input('Escribe un numero: '))
numeros = 0

while numero > 0:
    numeros += 1
    numero = int(input('Escribe un numero: '))
print('Se ingresanron {} numeros.'.format(numeros))