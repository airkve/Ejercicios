# Crear una funcion con una lista de 10 elementos.
# que ubique la posicion de un elemento y lo remplaze por el nuevo ingresado

nums = []

def loadNums():
    for i in range(10):
        question = int(input('Ingresa un numero: '))
        nums.append(question)

def changeNum(num, pos):
    nums.insert(pos, num)
    nums.pop(10)

loadNums()
print(nums)

print('\nIngresa el numero y la posicion a cambiar:')

num = int(input('Numero: '))
pos = int(input('Posicion: '))

changeNum(num, pos)
print(nums)
