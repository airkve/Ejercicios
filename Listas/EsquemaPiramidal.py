# Desarrollar un programa que indique lo que genera un esquema piramidal como Amway o Herbalife

def maxLvl(replicacion, totalHab):
    nivelMax = 0

    while replicacion**nivelMax < totalHab:
        nivelMax += 1
    
    return print('Se repite {} veces'.format(nivelMax))

maxLvl(2, 2890000)