# Crear una funcion que cree dos listas de numeros y mezclarlas en una tercera lista

def listaPrint():
    lista1 = []
    lista2 = []
    lista3 = []

    for i in range(20):
        question = int(input('Introduce un numero: '))
        if i <= 9:
            lista1.append(question)
        else:
            lista2.append(question)

    for i, j in zip(lista1, lista2):
        lista3.append(i)
        lista3.append(j)
    print(lista3)

listaPrint()