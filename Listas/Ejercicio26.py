# Crear una funcion que reciba por parametro una lista con 2 listas internas,
# que represente un tablero de ajedrez y la pocicion de las piezas
# Peon, Torre, Caballo, Alfil, Rey y Reina.
# La funcion debe retornar True o False, dependiendo de si el Rey está o no en jaque

board = [
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', 'T', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '', '0', '0'],
    ['0', '0', '0', 'K', '0', '0', '0', '0']
]

def getIndex(lst, char):
    for lista in lst:
        if char in lista:
            return lst.index(lista)

def checkMate(data):
    for i in range(8): # Forloop para recorrer las 8 listas
        for j in range(8): # Forloop para recorrer cada lista

            if data[i][j] == 'P': # Encuentra al Peon
                # Chequea si diagonal al peon hay un rey 'K'
                if data[i - 1][j - 1] == 'K' or data[i - 1][j + 1] == 'K':
                    return True
                elif data[i + 1][j - 1] == 'K' or data[i + 1][j + 1] == 'K':
                    return True
                else:
                    return False

            if data[i][j] == 'T': # Encuentra a la Torre
                x, y = i, j # guarda las coordenadas de la torre
                print(x, y)
                print(data[i][y])
                if 'K' in data[x]:
                    print("Jaque mate!")

                for k in data[i]:
                    if k.index('K') == y
                elif data[i][y] == 'K':
                    print("Jaque mate!")
                else:
                    print('No hay jaque.')

            # if data[i][j] == 'C': # Encuentra el Caballo
            #     x, y = i, j # guarda las coordenadas de la torre
            #     if data[i - 1][j - 1] == 'K' or data[i - 1][j + 1] == 'K':
            #         print("Jaque mate!")
            #     elif data[i + 1][j - 1] == 'K' or data[i + 1][j + 1] == 'K':
            #         print("Jaque mate!")
            #     else:
            #         print('No hay jaque.')

            # if data[i][j] == 'A': # Encuentra al Alfil
            #     if data[i - 1][j - 1] == 'K' or data[i - 1][j + 1] == 'K':
            #         print("Jaque mate!")
            #     elif data[i + 1][j - 1] == 'K' or data[i + 1][j + 1] == 'K':
            #         print("Jaque mate!")
            #     else:
            #         print('No hay jaque.')

            # if data[i][j] == 'K':
            #     if data[i - 1][j - 1] == 'K' or data[i - 1][j + 1] == 'K':
            #         print("Jaque mate!")
            #     elif data[i + 1][j - 1] == 'K' or data[i + 1][j + 1] == 'K':
            #         print("Jaque mate!")
            #     else:
            #         print('No hay jaque.')

            # if data[i][j] == 'Q':
            #     if data[i - 1][j - 1] == 'K' or data[i - 1][j + 1] == 'K':
            #         print("Jaque mate!")
            #     elif data[i + 1][j - 1] == 'K' or data[i + 1][j + 1] == 'K':
            #         print("Jaque mate!")
            #     else:
            #         print('No hay jaque.')

checkMate(board)
                
                