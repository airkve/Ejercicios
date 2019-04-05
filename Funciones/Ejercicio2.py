# Diseñar una funcion que tenga como parametro dos numeros y que
# calcule cual es mas grande

from random import randint

def mayor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print('El numero mayor es: ', mayor(randint(1, 10), randint(1, 10)))