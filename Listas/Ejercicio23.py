# Crear una funcion que ordene de manera creciente o decreciente, una lista desordenada
# de numeros enteros

def message():
    print('Indica si deseas ordernar la lista de manera (C)reciente o (D)ecreciente')
    msg = input('>')
    return msg

def listOrder(data, option):
    minimum = 0
    tmpOrder = []
    if option.lower() == 'c':
        for i in data:
            if i > minimum:
                minimum = i
                tmpOrder.append(minimum)

    print(tmpOrder)

choice = message()

