# Crear una funcion que se le pase una lista como parametro y muestre
# una lista con los pares y que adicionalmente muestre cuantos numeros
# impares fueron introducidos.

nums = []

def loadNums():
    for i in range(10):
        question = int(input('Ingresa un numero: '))
        nums.append(question)

print(nums)

def delOddNums(data):
    lst = []
    cont = 0
    for i in range(len(data)):
        if data[i] % 2 == 0:
            cont += 1
        else:
            lst.append(i)
            
    print('Los numeros pares son {}\nLa cantidad de numeros impares fueron: {}'.format(lst, cont))

loadNums()
delOddNums(nums)
