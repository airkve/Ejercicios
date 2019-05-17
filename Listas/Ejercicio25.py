# Crear una funcion que calcule el valor maximo de una lista de manera recursiva

import random

def randomList(fromNum, toNum, length):
    tempLst = []
    for i in range(length):
        randNum = random.randint(fromNum, toNum)
        if randNum not in tempLst:
            tempLst.append(randNum)
    return tempLst

lst = randomList(1, 20, 10)
print(lst)
        

def maxNum(data):
    if len(data) == 1:
        return data[0]
    else:
        max = maxNum(data[:1])
    
    if max > data[0]:
        return max
    else:
        return data[0]

print(maxNum(lst))