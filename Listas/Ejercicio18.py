# Crear una funcion que devuelva una lista con todos los divisores primos de un numero N

def primeNums(num):
    result = []
    for i in range(1, num):
        if num % i == 0:
            result.append(i)
    print(result)

question = int(input('Escribe un numero: '))
primeNums(question)
