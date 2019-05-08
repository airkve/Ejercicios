# Crear una funcion que calcule el area y el volumen de un cilindro
# y que devuelva abos valores en una lista [area, volumen]
# la funcion tiene radio y altura como parametros

cilindro = []

def getAreaVol(rad, alt):
    volumen = 3.14 * (rad * rad) * alt
    area = 2 * 3.14 * rad * alt

    cilindro = [area, volumen]

getAreaVol(5, 7)
print(cilindro)
