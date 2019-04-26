# Crear una funcion que diga cuantas lanzadas de dados son necesarias
# para que cada numero salga la cantidad de veces que los otros numeros

from random import randint

laps = 0
result = [0, 0, 0, 0, 0, 0]

while True:
    dice = randint(1, 6)
    if dice == 1:
        result[0] += 1
    elif dice == 2:
        result[1] += 1
    elif dice == 3:
        result[2] += 1
    elif dice == 4:
        result[3] += 1
    elif dice == 5:
        result[4] += 1
    elif dice == 6:
        result[5] += 1

    laps += 1
    print(result)
    if result[0] == result[1] and result[1] == result[2] and result[2] == result[3] and result[3] == result[4] and result[4] == result[5] and result[5] == result[6]:
        print(laps)
        break


