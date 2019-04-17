# Crea una funcion que sume los primeros numeros primos de N

def sumPrimos(num):
    
    for i in range(2, 101):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                #print(i, 'Es primo')
                isPrime = False
        if isPrime:
            print(i + i)

sumPrimos(50)