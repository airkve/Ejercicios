# Pedir un numero e indicar si es positivo o negativo, repite
# el proceso hasta llegar a cero.

numero = int(input('Escribe un numero: '))

while True:
    if numero == 0:
        break
    elif numero > 0:
        print('{} es positivo'.format(numero))
        numero = int(input('Escribe un numero: '))
    else:
        print('{} es negativo'.format(numero))
        numero = int(input('Escribe un numero: '))
