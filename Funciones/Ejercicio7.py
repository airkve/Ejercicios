# Crear una funcion que devuelva la cantidad de divisores del numero introducido,
# que sean numeros primos


def divGet(num):
    counter = 0
    for i in range(1, num):
        if num % i == 0:
            counter += 1
            print(i)
    print('Tiene',counter, ' numeros primos.')

divGet(26)