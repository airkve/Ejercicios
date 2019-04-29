# Crear un programa que tome 5 numeros introducidos por consola  de manera ascendente
# luego solicitar el ingreso de un numero y ubicarlo de manera ascendente dentro de la lista

nums = []

def loadNums():
    for i in range(5):
        question = int(input('Ingresa un numero: '))
        nums.append(question)

def changeList(lst, num):
    for i in range(len(lst) - 1):
        if num > lst[i] and num < lst[i + 1]:
            nums.insert(i + 1, num)
        elif num not in lst:
            nums.append(num)

loadNums()
data = int(input('Ingresa un numero para agregar: '))

changeList(nums, data)

print(nums)