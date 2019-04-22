# Crear una funcion que lea 5 numeros y los muestre en orden inverso.

def listaPrint():
    listaNum = []
    for i in range(5):
        question = int(input('Introduce un numero: '))
        listaNum.append(question)
        
    for num in listaNum[::-1]:
        print(num, end=' ')

listaPrint()