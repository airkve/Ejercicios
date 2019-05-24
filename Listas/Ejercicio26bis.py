# Crear una funcion que reciba por parametro una lista con 2 listas internas,
# que represente un tablero de ajedrez y la pocicion de las piezas
# Peon, Torre, caballo, Alfil, Rey y Reina.
# La funcion debe retornar True o False, dependiendo de si el Rey está o no en jaque

board = [
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['A', '0', 'T', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', 'P', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['C', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', 'K', '0', '0', '0', '0', '0', '0']
]

def getIndex(lst, char):
    x, y = 0, 0

    for i in range(len(lst)):
        if char in lst[i]:
            x = lst[i].index(char)
            y = i
    return [x, y]

def peon(king):
    posC = getIndex(board, 'P')
    posC.append([posC[0] + 1, posC[1] + 1])
    posC.append([posC[0] + 1, posC[1] - 1])
    posC.append([posC[0] - 1, posC[1] + 1])
    posC.append([posC[0] - 1, posC[1] - 1])
    print(posC)
    for pos in posC:
        print(pos)
        if king == pos:
            return True

def torre(king):
    posT = getIndex(board, 'T')
    if king[0] == posT[0] or king[1] == posT[1]:
        return True
    
def caballo(king):
    posC = getIndex(board, 'C')
    posC.append([posC[0] + 2, posC[1] + 1])
    posC.append([posC[0] + 2, posC[1] - 1])
    posC.append([posC[0] - 2, posC[1] + 1])
    posC.append([posC[0] - 2, posC[1] - 1])
    posC.append([posC[0] + 1, posC[1] + 2])
    posC.append([posC[0] + 1, posC[1] - 2])
    posC.append([posC[0] - 1, posC[1] + 2])
    posC.append([posC[0] - 1, posC[1] - 2])

    for pos in posC:
        if king == pos:
            return True

def alfil(king):
    posA = getIndex(board, 'A')
    alfilXmax = 8 - posA[0]
    alfilYmax = 8 - posA[1]
    alfilXless = 8 - posA[0]
    alfilYless = 8 - posA[1]
    posA.append([posA[0] + y for in range(1, 8), posA[1])
    
print(caballo(getIndex(board, 'K')))


def jaqueMate(data):
    posK = getIndex(board, 'K')
    posC = getIndex(board, 'P')
    posT = getIndex(board, 'T')
    posC = getIndex(board, 'C')
    posA = getIndex(board, 'A')
    posQ = getIndex(board, 'Q')

    # Chequea la posicion del peon respecto al rey
    if posK == [posC[0] + 1, posC[1] + 1]:
        return True
    elif posK == [posC[0] + 1, posC[1] - 1]:
        return True
    elif posK == [posC[0] - 1, posC[1] + 1]:
        return True
    elif posK == [posC[0] - 1, posC[1] - 1]:
        return True
    # else:
    #     return False

    # Chequea la posicion de la torre respecto al rey
    if posK[0] == posT[0] or posK[1] == posT[1]:
        print('jaque con la torre')
        return True

    # Chequea la posicion del caballo respecto al rey
    if posK[0] + 2 == posC[0] or posK[0] - 2 == posC[0]:
        if posK[1] + 1 == posC[1] or posK[1] - 1 == posC[1]:
            return True
    elif posK[0] + 1 == posC[0] or posK[0] - 1 == posC[0]:
        if posK[1] + 2 == posC[1] or posK[1] - 2 == posC[1]:
            return True

    # Chequea la posicion del alfil respecto al rey
    if 8 - posK[0] <= 4: # Calcula el lado mas grande para ubicarse
        for i in range(posK[0], 8):
            for j in range(posK[1], 8):
                if posK[0] + i == posA[0]:
                    if posK[1] + j == posA[1] or posK[1] - j == posA[1]:
                        return True
    else:
        for i in range(posK[0]):
            for j in range(posK[1]):
                if posK[0] + i == posA[0]:
                    if posK[1] + j == posA[1] or posK[1] - j == posA[1]:
                        return True

print(jaqueMate(board))
