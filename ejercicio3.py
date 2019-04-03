# Pedir un numero e indicar si es par o impar, repite
# el proceso hasta llegar a cero.

numero = int(input('Escribe un numero: '))

while True:
    if numero == 0:
        break
    elif numero % 2 == 0:
        print('{} es par'.format(numero))
        numero = int(input('Escribe un numero: '))
    else:
        print('{} es impar'.format(numero))
        numero = int(input('Escribe un numero: '))
