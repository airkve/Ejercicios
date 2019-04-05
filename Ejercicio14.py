# Crear un programa que haga la sumatoria de 10 sueldos y
# que indique cuantos hay mayores a 10000

sTotal = 0
counter = 0

for i in range(10):
    print('Ingresa el sueldo N.', i+1)
    sueldo = int(input('>'))
    sTotal += sueldo
    if sueldo > 10000:
        counter += 1

print('La suma de los sueldos es de {:,} y hay {} que pasan los 10000'.format(sTotal, counter))
