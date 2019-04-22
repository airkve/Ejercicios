# Ejemplos de listas

[1, 2, 3]
['gato', 'perro', 'rata', 'elefante']
spam = ['gato', 'perro', 'rata', 'elefante'] # Lista de cadenas
print(spam)
print(spam[3])
print('hola' + spam[0])
print('El ' + spam[0] + ' se comio la ' + spam[2])

spam1 = [['gato', 'perro'], [10, 20, 30, 40, 50]] # Nested list
print(spam[-1]) # Indice negativo
print(spam[1:3]) # Slices
print(spam[0:-1])

spam[1] = 'prueba'
spam[2] = spam[1]
spam[-1] = 12345

print([1, 2, 3] + ['A', 'B', 'C']) # Concatenacion de listas
print(['x', 'y', 'z'] * 3) # Replicacion de listas
print(spam)

del spam[2]
print(spam)

print(spam.index('gato'))

spam.append('conejo')
spam.append(12)
spam.insert(1, 'ardilla')
spam.remove('gato')
print(spam)