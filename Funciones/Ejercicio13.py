# Crea una funcion que decida si en numero es primo

def numPrimo():
    for i in range(2, 101):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                #print(i, 'Es primo')
                isPrime = False
        if isPrime:
            print(i, 'Es primo')

numPrimo()
