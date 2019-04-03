# Crear un programa que pida un numero N e introducir sueldos por ese cantidad de N
# Mostrar el sueldo maximo

n = int(input('Introduce un numero: '))

for i in range(n):
    sueldo = int(input('Ingrese el sueldo: '))
    compare = sueldo

    if sueldo > compare:
        result = sueldo
    else:
        result = compare

print(result)