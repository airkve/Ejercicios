# Crear un programa que se le ingresen 2 listas de 10 numeros c/u por consola
# combinar ambas listas en una tercera pero en orden creciente.

lst1 = []
lst2 = []

def loadNums():
    for i in range(20):
        question = int(input('Introduce un numero: '))
        if i <= 9:
            lst1.append(question)
        else:
            lst2.append(question)

def putOrder(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

def mergeListsOrdered():
    lstTo100 = range(101)
    newLst = lst1 + lst2
    resultLst = []
    for num in newLst:
        if num > lower:
            
    print(resultLst)

loadNums()
mergeListsOrdered()

    
