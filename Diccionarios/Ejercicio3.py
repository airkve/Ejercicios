# Hacer un programa del juego tic tac toe usando diccionarios

tablero = {
    'topLine': [' ', ' ', ' '],
    'midLine': [' ', ' ', ' '],
    'botLine': [' ', ' ', ' '],
}

def play(board, player, pos):
    pass

def checkWin(board):
    pass

def printBoard():
    print(' {} | {} | {} '.format(tablero['topLine'][0], tablero['topLine'][1], tablero['topLine'][2])
    print('----+----+----')
    print(' {} | {} | {} '.format(tablero['midLine'][0], tablero['midLine'][1], tablero['midLine'][2])
    print('----+----+----')
    print(' {} | {} | {} '.format(tablero['botLine'][0], tablero['botLine'][1], tablero['botLine'][2])
    print()


# while True:
#     print(' {} | {} | {} '.format('topL(7)', 'topM(8)', 'topR(9)'))
#     print('----+----+----')
#     print(' {} | {} | {} '.format('midL(4)', 'midM(5)', 'midR(6)'))
#     print('----+----+----')
#     print(' {} | {} | {} '.format('botL(1)', 'botM(2)', 'botR(3)'))
#     print()
#     print('Turno del jugador 1.')
#     jugador1 = input('Indica el numero que corresponde a la posicion: ')

#     if jugardor1 == '1':
#         tablero['botL'] = 1
#     elif jugador1 == '2':
#         tablero['botM'] = 1
#     elif jugador1 == '3':
#         tablero['botR'] = 1
#     elif jugador1 == '4':
#         tablero['midL'] = 1
#     elif jugador1 == '5':
#         tablero['midM'] = 1
#     elif jugador1 == '6':
#         tablero['midR'] = 1
#     elif jugador1 == '7':
#         tablero['topL'] = 1
#     elif jugador1 == '8':
#         tablero['topM'] = 1
#     elif jugador1 == '9':
#         tablero['topR'] = 1

printBoard()