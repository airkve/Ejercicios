# Crear un programa que calcule el factorial del numero introducido

n = int(input('Escriba un numero: '))
factorial = 1

for i in range(n, 0, -1):
    factorial *= i

print('El factorial de {} es {:,}'.format(n, factorial))
