# Crear un programa que pida 5 numeros y que muestre si alguno
# es multiplo de 3

counter = 0

for i in range(5):
    n = int(input('Escribe un numero: '))

    if n % 3 == 0:
        counter += 1
        print('{} es multiplo de 3.'.format(n))

print('En total, hubieron {} numeros multiplos de 3.'.format(counter))
