# Crear un programa que muestre el promedio de todos los numeros
# hasta que se instrodusca un numero negativo

n = 0
suma = 0
count = 0

while n >= 0:
    n = int(input('Escribe un numero: '))
    count += 1
    suma += n

print('El promedio de los numeros es: {}'.format(suma / count))
