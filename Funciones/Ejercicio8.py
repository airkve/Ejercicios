# Crear una funcion que calcule el maximo divisor en comun entre 2 numeros

def divNumGet(num1, num2):
    maxNum = 0
    if num1 > num2:
        for i in range(1, num1):
            if num1 % i == 0 and num2 % i == 0:
                if i > maxNum:
                    maxNum = i
    else:
        for i in range(1, num2):
            if num1 % i == 0 and num2 % i == 0:
                if i > maxNum:
                    maxNum = i
    return maxNum

print(divNumGet(12, 14))