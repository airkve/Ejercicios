# Crear una funcion que reciba por parametro una lista con 2 listas internas,
# que represente un tablero de ajedrez y la pocicion de las piezas
# Peon, Torre, caballo, Alfil, Rey y Reina.
# La funcion debe retornar True o False, dependiendo de si el Rey está o no en jaque

board = [
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', 'K', '0', '0', '0', '0', '0'],
    ['C', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0']
]

def getIndex(lst, char):
    x, y = 0, 0

    for i in range(len(lst)):
        if char in lst[i]:
            x = lst[i].index(char)
            y = i
    return x, y

def jaqueMate(data):
    posK = list(getIndex(board, 'K'))
    posP = list(getIndex(board, 'P'))
    posT = list(getIndex(board, 'T'))
    posC = list(getIndex(board, 'C'))
    posA = list(getIndex(board, 'A'))
    posQ = list(getIndex(board, 'Q'))

    # Chequea la posicion del peon respecto al rey
    if posK[0] + 1 == posP[0] or posk[0] - 1 == posP[0]:
        if posK[1] + 1 == posP[1] or posK[1] - 1 == posP[1]:
            return True

    # Chequea la posicion de la torre respecto al rey
    if posK[0] == posP[0] or posk[1] == posP[1]:
        return True

    # Chequea la posicion del caballo respecto al rey
    if posK[0] + 2 == posP[0] or posk[0] - 2 == posP[0]:
        if posK[1] + 1 == posP[1] or posK[1] - 1 == posP[1]:
            return True
    elif posK[0] + 1 == posP[0] or posk[0] - 1 == posP[0]:
        if posK[1] + 2 == posP[1] or posK[1] - 2 == posP[1]:
            return True
    

def checkMate(data):
    jaqueP = False
    jaqueT = False
    jaqueC = False
    jaqueA = False
    jaqueQ = False

    for i in range(8): # Forloop para recorrer las 8 sub-listas
        for j in range(8): # Forloop para recorrer cada sub-lista

            if data[i][j] == 'P': # Encuentra al peon
                peonX, peonY = j, i # guarda las coordenadas del peon
                reyX, reyY = getIndex(board, 'K') # guarda las coordenadas del rey

                # Chequea si hay un rey 'K' en frente del peon
                if peonY == reyY + 1 or peonY == reyY - 1:
                    if peonX == reyX or peonX == reyX - 1 or peonX == reyX + 1:
                        return True
                    else:
                        return False

            if data[i][j] == 'T': # Encuentra a la torre
                torreX, torreY = j, i # guarda las coordenadas de la torre
                reyX, reyY = getIndex(board, 'K') # guarda las coordenadas del rey

                if torreX == reyX or torreY == reyY:
                    return True
                else:
                    return False

            if data[i][j] == 'C': # Encuentra el caballo
                caballoX, caballoY = j, i # guarda las coordenadas del caballo
                reyX, reyY = getIndex(board, 'K') # guarda las coordenadas del rey

                if caballoY == reyY + 2 or caballoY == reyY - 2:
                    if caballoX == reyX + 1 or caballoX == reyX - 1:
                        return True
                    else:
                        return False

                if caballoX == reyX + 2 or caballoX == reyX -2:
                    if caballoY == reyY + 1 or caballoY == reyY - 1:
                        return True
                    else:
                        return False

            if data[i][j] == 'A': # Encuentra al Alfil
                reinaX, reinaY = j, i # guarda las coordenadas del Alfil
                reyX, reyY = getIndex(board, 'K') # guarda las coordenadas del rey
                jaque = False

                if reinaY == reyY + 1:
                    if reinaX == reyX + 1 or reinaX == reyX - 1:
                        jaque = True
                elif reinaY == reyY + 2:
                    if reinaX == reyX + 2 or reinaX == reyX - 2:
                        jaque = True
                elif reinaY == reyY + 3:
                    if reinaX == reyX + 3 or reinaX == reyX - 3:
                        jaque = True
                elif reinaY == reyY + 4:
                    if reinaX == reyX + 4 or reinaX == reyX - 4:
                        jaque = True
                elif reinaY == reyY - 1:
                    if reinaX == reyX + 1 or reinaX == reyX - 1:
                        jaque = True
                elif reinaY == reyY - 2:
                    if reinaX == reyX + 2 or reinaX == reyX - 2:
                        jaque = True
                elif reinaY == reyY - 3:
                    if reinaX == reyX + 3 or reinaX == reyX - 3:
                        jaque = True
                elif reinaY == reyY - 4:
                    if reinaX == reyX + 4 or reinaX == reyX - 4:
                        jaque = True

                return jaque
                

            if data[i][j] == 'Q':
                reinaX, reinaY = j, i # guarda las coordenadas de la Reina
                reyX, reyY = getIndex(board, 'K') # guarda las coordenadas del rey
                jaque = False

                if reinaY == reyY + 1:
                    if reinaX == reyX + 1 or reinaX == reyX - 1:
                        jaque = True
                elif reinaY == reyY + 2:
                    if reinaX == reyX + 2 or reinaX == reyX - 2:
                        jaque = True
                elif reinaY == reyY + 3:
                    if reinaX == reyX + 3 or reinaX == reyX - 3:
                        jaque = True
                elif reinaY == reyY + 4:
                    if reinaX == reyX + 4 or reinaX == reyX - 4:
                        jaque = True
                elif reinaY == reyY - 1:
                    if reinaX == reyX + 1 or reinaX == reyX - 1:
                        jaque = True
                elif reinaY == reyY - 2:
                    if reinaX == reyX + 2 or reinaX == reyX - 2:
                        jaque = True
                elif reinaY == reyY - 3:
                    if reinaX == reyX + 3 or reinaX == reyX - 3:
                        jaque = True
                elif reinaY == reyY - 4:
                    if reinaX == reyX + 4 or reinaX == reyX - 4:
                        jaque = True
                
                if reinaX == reyX or reinaY == reyY:
                    jaque = True

                return jaque
                


print(checkMate(board))