# Crear una funcion que calcule el maximo divisor en comun entre 3 numeros

def divNumGet(num1, num2, num3):
    maxNum = 0
    if num1 > num2 and num1 > num3:
        for i in range(1, num1):
            if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
                if i > maxNum:
                    maxNum = i
                    print(i)
    elif num2 > num1 and num2 > num3:
        for i in range(1, num2):
            if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
                if i > maxNum:
                    maxNum = i
                    print(i)
    else:
        for i in range(1, num3):
            if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
                if i > maxNum:
                    maxNum = i
                    print(i)
    return maxNum

print(divNumGet(120, 140, 180))