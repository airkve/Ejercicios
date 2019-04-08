# Diseñar una funcion que muestre todos los numeros entre los dos que se piden

def numerosCuenta(num1, num2):
    if num1 > num2:
        for i in range(num2, num1 + 1):
            print(i)
    else:
        for j in range(num1, num2 + 1):
            print(j)

numerosCuenta(10, 5)
