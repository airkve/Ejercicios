# Realizar una funcion que el parametro sea un numero N
# mostrar en pantalla N veces el mensaje:
# Modulo ejecutandose

from random import randint

def ejecucion(numero):
    for i in range(numero):
        print('Módulo ejecutandose')

ejecucion(randint(1, 10))