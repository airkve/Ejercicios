# Crear un programa que pida un numero y lo busque en una lista de 10 numeros previamente
# ingresada por consola y que indique la posicion o error en caso de que no exista

nums = []

def loadNums():
    for i in range(10):
        question = int(input('Ingresa un numero: '))
        nums.append(question)

def getIndex(num):
    if num in nums:
        print(nums.index(num))
    else:
        print('No se encontro el numero indicado.')

loadNums()
question = int(input('Ingresa el numero a buscar: '))
getIndex(question)