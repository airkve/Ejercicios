# Crear una funcion que calcule el minimo comun multiplo de 3 numeros

# Crear una funcion que calcule el minimo comun multiplo de 2 numeros

def minComMult(num1, num2, num3):
    result = 0

    if num1 > num2:
        mayor = num1
    else:
        mayor = num2

    if num3 > mayor:
        mayor = num3        

    while True:
        if mayor % num1 == 0 and mayor % num2 == 0 and mayor % num3 == 0:
            result = mayor
            break
        mayor += 1

    return mayor

print(minComMult(40, 60, 50))