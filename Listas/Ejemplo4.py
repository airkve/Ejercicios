# Crea una funcion que lea 10 numeros enteros y que los muestre en el siguiente orden
# primero, ultimo, segundo, anteultimo, tercero, ante-ante penultimo, etc

def listaPrint():
    listaNum = []
    for i in range(10):
        question = int(input('Introduce un numero: '))
        listaNum.append(question)
    
    for i in range(len(listaNum)):
        print(listaNum[i], listaNum[len(listaNum):i:-1])
    # print(listaNum[0])

    # for i in range(5):
    #     print(listaNum[(i+1)*(-1)])
    #     print(listaNum[i+1])

listaPrint()