# Crear una funcion que lea 5 numeros e imprimirla en el mismo orden en que se creó

def listaPrint():
    listaNum = []
    for i in range(5):
        question = int(input('Introduce un numero: '))
        listaNum.append(question)
        
    for num in listaNum:
        print(num, end=' ')

listaPrint()