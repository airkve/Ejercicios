# Crear un programa que muestre el producto de los 10
# primeros numeros impares

result = 1

for i in range(1, 20, 2):
    print(i)
    result *= i

print('El producto final es: {:,}'.format(result))
