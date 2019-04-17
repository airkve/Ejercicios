# gatoNombre1 = 'Bodoque'
# gatoNombre2 = 'Simon'
# gatoNombre3 = 'Luis'

# gatoNombre1 = input('Ingrese el nombre del gato 1: ')
# gatoNombre2 = input('Ingrese el nombre del gato 2: ')
# gatoNombre3 = input('Ingrese el nombre del gato 3: ')

# print('Los gatos se llaman:\n{}\n{}\n{}'.format(gatoNombre1, gatoNombre2, gatoNombre3))

gatos = []
while True:
    print('Ingrese el nombre del gato ' + str(len(gatos) + 1))
    catName = input('>')
    if catName == '':
        break
    gatos = gatos + [catName]
    
for name in gatos:
    print(name)