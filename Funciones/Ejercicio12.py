# Crear una funcion que decida si dos numeros enteros positivos, son amigos
# 2 numeros son amigos si, la suma de sus divisores son iguales al otro numero.

def numAmigos(num1, num2):
    totalNum1 = 0
    totalNum2 = 0
    for i in range(1, num1):
        if num1 % i == 0:
            totalNum1 += i
    for j in range(1, num2):
        if num2 % j == 0:
            totalNum2 += j
    if totalNum1 == num2 and totalNum2 == num1:
        #print('Los numeros {} y {}, son amigos'.format(num1, num2))
        return True
    else:
        #print('Los numeros {} y {}, no son amigos'.format(num1, num2))
        return False

#numAmigos(496, 496)

def allNumsAmigos():
    for i in range(1, 1300):
        for j in range(i+1, 1300):
            if i != j:
                if numAmigos(i, j):
                    print(i, j, 'Son amigos')

allNumsAmigos()
