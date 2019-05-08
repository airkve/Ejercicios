# Crear un programa que nos ayude a gestionar las notas de un centro educativo
# cada grupo o clase, esta compuesto por 5 alumnos.
# Mostrar los promedios de notas del primer, segundo y tercer trimestre de un grupo y
# el promedio del alumno X

alumnos = [[], [], [], [], []]


def loadEstudents():
    for i in range(5):
        for j in range(3):
            print('Ingresa la nota del trimestre {}, para el alumno {}.'.format(j+1, i+1))
            calif = int(input('>'))
            alumnos[i].append(calif)

def notesReport(lst):
    prom_1_trim = 0
    prom_2_trim = 0
    prom_3_trim = 0

    for i in range(5):
        prom_1_trim += lst[i][0]
        prom_2_trim += lst[i][1]
        prom_3_trim += lst[i][2]
    
    print('El promedio para el 1er Trimestre es: {}'.format(prom_1_trim / 5))
    print('El promedio para el 2er Trimestre es: {}'.format(prom_2_trim / 5))
    print('El promedio para el 3er Trimestre es: {}'.format(prom_3_trim / 5))

def getAlumProm(lst):
    alumProm = 0

    alumn = int(input('Indique el numero del alumno, para promediar: '))
    for i in range(3):
        alumProm += lst[alumn-1][i]

    print('El promedio del alumno es: {:f2}'.format(alumProm / 3))

loadEstudents()
notesReport(alumnos)
getAlumProm(alumnos)


