# Crear una funcion que decida si dos numeros enteros son amigos, utilizando listas.

def numAmigos(num1, num2):
    lstNum1 = []
    lstNum2 = []

    for i in range(1, num1):
        if num1 % i == 0:
            lstNum1.append(i)
    for j in range(1, num2):
        if num2 % j == 0:
            lstNum2.append(j)

    if sum(lstNum1) == num2 and sum(lstNum2) == num1:
        print('Los numeros {} y {}, son amigos'.format(num1, num2))
        return True
    else:
        print('Los numeros {} y {}, no son amigos'.format(num1, num2))
        return False

numAmigos(1184, 1211)