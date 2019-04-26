# Crear una funcion que indique si los numeros ingresados manalmente, estan
# en orden creciente, decreciente o desordenados

def getOrder(lst):
    result = []

    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            result.append(True)
        elif lst[i] > lst[i + 1]:
            result.append(False)

    if False not in result:
        print('La lista está en orden ascendente')
    elif True not in result:
        print('La lista está en orden decendente')
    else:
        print('La lista está desordenada')

def newList():
    for i in range(10):
        question = int(input('Introduce un numero: '))
        nums.append(question)

newList()
getOrder(nums)
