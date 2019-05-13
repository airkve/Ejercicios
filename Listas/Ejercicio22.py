# Crear una funcion que haga una operacion aritmetica segun se le indique por
# medio de una letra, 's' suma, 'r' resta, 'm' multiplica y 'd' dividir
# los datos de entrada, son 2 listas y la letra de la operacion, el resultado
# tiene que ser el total de la operacion, por cada numero respecto a su indice.

nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]

def calculator(data1, data2):
    totalLst = []
    print('Indique la operacion que desee realizar: (S)uma, (R)esta, (M)ultiplicacion o (D)ivision.')
    calc = input('>')
    print(calc)
    if calc.lower() == 's':
        for i in range(len(data1)):
            totalLst.append(data1[i] + data2[i])
    elif calc.lower() == 'r':
        for i in range(len(data1)):
            totalLst.append(data1[i] - data2[i])
    elif calc.lower() == 'm':
        for i in range(len(data1)):
            totalLst.append(data1[i] * data2[i])
    elif calc.lower() == 'd':
        for i in range(len(data1)):
            totalLst.append(data1[i] / data2[i])
        
    print(totalLst)

calculator(nums1, nums2)
