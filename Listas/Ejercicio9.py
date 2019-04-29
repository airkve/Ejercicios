# Crear un programa que cargue 10 numeros por consola.
# pedir al usuario un numero que desplace la lista N posiciones
# colocando los N numeros en el tope de la lista

nums = []

def loadNums():
    for i in range(10):
        question = int(input('Ingresa un numero: '))
        nums.append(question)

def changeList(num):
    topList = nums[num * -1:len(nums)]
    cutList = nums[:num * -1]
    newList = topList + cutList
    print(newList)

loadNums()
data = int(input('Ingresa la cantidad de espacios a desplazar: '))
changeList(data)