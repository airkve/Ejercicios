# Diseñar una funcion que tenga como parametro tres numeros y que
# calcule cual es mas grande

from random import randint

def mayor(num1, num2, num3):
    max = 0
    if num1 > num2:
        max = num1
    else:
        max = num2

    if max > num3:
        return max
    else:
        return num3


print('El numero mayor es: ', mayor(randint(1, 10), randint(1, 10), randint(1, 10)))
print('El numero mayor es: ', mayor(3, 5, 1))