# Pedir un numero y mostrar su cuadrado, repetir este proceso hasta
# que se introduzca un mumero negativo

numero = 0

while numero >= 0:
    numero = int(input('Escribe un numero positivo: '))
    print('{}'.format(numero**2))
print('Programa terminado.')