# Crear un programa que sume numeros hasta que se ingrese el 0

suma = 0

while True:
    n = int(input('Ingresa un numero: '))
    suma += n
    if n == 0:
        break

print('La suma total es: ', suma)
