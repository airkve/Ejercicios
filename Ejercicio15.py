# Crear un programa que pida la edad y la altura de 5 alumnos
# y mostrar:
# edad media
# altura media
# cantidad de alumnos mayores a 18 años
# cantidad de alumnos que miden mas de 1.75

edad = 0
altura = 0.0
cont18 = 0
cont1_75 = 0

for i in range(5):
    print('Ingresa la edad del alumno N.{}'.format(i+1))
    age = int(input('>'))
    print('Ingresa la altura del alumno N.{}'.format(i+1))
    height = float(input('>'))

    edad += age
    altura += height
    if age >= 18:
        cont18 += 1
    elif height >= 1.75:
        cont1_75 += 1

print('La edad promedio de los alumnos es {}\n\
La altura promedio es de {}\n\
Hay {} mayores de edad\n\
Y {} miden mas de 1.75m'.format((edad / 5), (altura / 5), cont18, cont1_75))
