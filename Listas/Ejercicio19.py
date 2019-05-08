# Crear un programa que calcule el maximo comun divisor de 3 numeros usando listas

def getMaxDiv(num1, num2, num3):
    result = [[], [], []]
    
    for i in range(1, num1):
        if num1 % i == 0:
            result[0].append(i)

    for i in range(1, num2):
        if num2 % i == 0:
            result[1].append(i)

    for i in range(1, num3):
        if num3 % i == 0:
            result[2].append(i)

    for j in range(len(result)):
        for k in result[j]:
            if k in result

    print(result)

getMaxDiv(50, 20, 10)