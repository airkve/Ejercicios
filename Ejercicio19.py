# Crear un programa que pida 6 notas.
# Escribir la cantidad que promocionan (>=6)
# Aprueban 4 o 5
# Recursan <4

alumProm = 0
alumApru = 0
alumRecu = 0

for i in range(5):
    score = int(input('Escribe la nota del 1 al 10: '))

    if score >= 6:
        alumProm += 1
    elif score == 4 or score == 5:
        alumApru += 1
    elif score < 4:
        alumRecu += 1

print('Alumnos que promocionan {}'.format(alumProm))
print('Alumnos que aprueban {}'.format(alumApru))
print('Alumnos que recursan {}'.format(alumRecu))