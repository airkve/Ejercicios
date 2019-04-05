# Crear un programa que muestre de 10 numeros:
# Media de los numeros positivos
# Media de los numeros negativos
# Cantidad de ceros

numPos = 0
numPosCount = 0
numNeg = 0
numNegCount = 0
numZer = 0

for i in range(10):
    n = int(input('Escribe un numero positivo, negativo o un cero: '))
    if n == 0:
        numZer += 1
    elif n > 0:
        numPos += n
        numPosCount += 1
    else:
        numNeg += n
        numNegCount += 1

print('El promedio de positivos es: {}, negativos {} y hay {} ceros'. format((numPos / numPosCount), (numNeg / numNegCount), numZer))
