# Crea una funcion que decida si en numero es primo

def numPrimo():
    for i in range(1, 999):
        if i % 1 == 0 and i % i == 0:
            print(i, 'Es primo')

numPrimo()