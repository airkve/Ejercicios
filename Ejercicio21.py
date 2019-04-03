# Crear un programa que pida 10 numeros y que muestre:
# Si se introdujo algun numero negativo
# Si se introdujo algun numero multiplo de 3
# Si se introdujo algun numero menor que 6

neg = 0
mult3 = 0
less6 = 0

for i in range(10):
    n = int(input('Escribe un numero: '))

    if n < 0:
        neg += 1
    elif n % 3 == 0:
        mult3 += 1
    elif n < 6:
        less6 += 1
if neg > 0:
    print('Se encontraron numeros negativos')
elif mult3 > 0:
    print('Se encontraron numeros multiplos de 3')
if less6 > 0:
    print('Se encontraron numeros menores a 6')

print('Se ingresaron {} numeros negativos, {} numeros multiplos de 3 y {} numeros menor que 6.'.format(neg, mult3, less6))