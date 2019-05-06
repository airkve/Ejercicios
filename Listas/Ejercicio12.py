# Crear un programa que lea 10 numeros y que copie los numeros pares y despues
# los impares, a una nueva lista

nums = []
copyEven = []
posEven = []

def loadNums():
    for i in range(10):
        question = int(input('Ingresa un numero: '))
        nums.append(question)

def changeOrder(lst):
    evenLst = []
    oddLst = []
    for i in lst:
        if i % 2 == 0:
            evenLst.append(i)
        else:
            oddLst.append(i)
    copyEven = evenLst + oddLst
    print(copyEven)

def copyPosOrder(lst):
    evenLst = []
    oddLst = []
    for i in range(len(lst)):
        if i % 2 == 0:
            evenLst.append(lst[i])
        else:
            oddLst.append(lst[i])
    posEven = evenLst + oddLst
    print(posEven)

loadNums()
changeOrder(nums)
copyPosOrder(nums)

