# Crear una funcion que tenga como parametro una lista y devuelva el numero maximo de la misma

lista = [5, 13, 7, 15, 1, 7, 20]

def getMaxNum(lst):
    maxNum = 0
    for num in lista:
        if num > maxNum:
            maxNum = num

    print(maxNum)

getMaxNum(lista)