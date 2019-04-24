# Crear una funcion que indique si los numeros ingresados manalmente, estan
# en orden creciente, decreciente o desordenados

def listaAsc(lista):
    result = False
    for i in range(len(lista)):
        if lista[i] < lista[i+1]
            result = True
    return result

def listaPrint():
    nums = []

    for i in range(10):
        question = int(input('Introduce un numero: '))
        nums.append(question)

    for j in range(len(nums)):
        if nums[j] < nums[j+1]:
            print('Es ascendente')
        elif nums[j] > nums[j+2]:
            print('Es decendente')
        else:
            print('Esta desordenada')
            
listaPrint()