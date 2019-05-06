# Crear una aplicacion que lea 10 numeros por consola y que se pregunte
# para eliminar un elemento si dejar un espacio vacio.

nums = []

def loadNums():
    for i in range(10):
        question = int(input('Ingresa un numero: '))
        nums.append(question)

loadNums()
question = int(input('Que numero posicion deseas borrar: '))
nums.pop(question)
print(nums)