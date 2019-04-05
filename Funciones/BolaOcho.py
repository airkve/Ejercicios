from random import randint

def bolaOcho(numero):
    if numero == 1:
        return 'Seguramente si'
    elif numero == 2:
        return 'Tal vez!'
    elif numero == 3:
        return 'Prueba de nuevo'
    elif numero == 4:
        return 'Preguntam mas tarde'
    elif numero == 5:
        return 'Hoy es tu dia de suerte'
    elif numero == 6:
        return 'Vas a conseguir trabajo pronto'
    elif numero == 7:
        return 'No salgas de tu casa'
    elif numero == 8:
        return 'Has el bien'

r = randint(1, 8)
fortuna = bolaOcho(r)
print(fortuna)