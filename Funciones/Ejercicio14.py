# Crear una funcion que convierta un numero entero a binario

def numToBinary(num):
    result = ''
    while num > 0:
        result += str(num % 2)
        #print(result, end='')
        num = num // 2
    print(result[::-1])

numToBinary(208)
