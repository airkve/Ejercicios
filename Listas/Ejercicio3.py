# Crear una funcion que calcule el promedio de los numeros positivos, negativos y la cantidad de ceros
# de los numeros ingresados

def listaPrint():
    listaNum = []
    for i in range(5):
        question = int(input('Introduce un numero: '))
        listaNum.append(question)
    
    ceros = 0
    promPos = 0
    promNeg = 0
    for num in listaNum:
        if num == 0:
            ceros += 1
        elif num > 0:
            promPos += num
        elif num < 0:
            promNeg += num

    print('Numeros positivos: {}\nNumeros negativos: {}\nCantidad de ceros: {}'.format(promPos, int(promNeg), ceros))

listaPrint()