# Crear una funcion que llene 2 listas de elementos numericos y mexclarlos
# en una trecera lista de la siguiente forma:
# 3 de la lista A y 3 de la lista B intercalados

lista1 = [4, 6, 8, 2, 1, 7, 5, 7, 3, 1, 0, 9]
lista2 = [9, 5, 1, 7, 3, 4, 6, 0, 4, 7, 8, 1]
lista3 = []

def listaMix(data):
    for i in range(3):
        lista3.append(data[i])
    del data[:3]

while len(lista1) > 0:
    listaMix(lista1)
    listaMix(lista2)

print(lista3)
