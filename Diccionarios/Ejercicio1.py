# Diseñar un programa que poermita consultar el cumpleaños de 3 amigos y en caso de consultar una fecha no existente
# ingresarla en el diccionario.

agenda = {
    'Juan': '11/10/2000',
    'Javier': '01/03/1982',
    'Antonella': '27/12/1973',
    'Richard': '11/08/73'
}

def addContact(agenda, nombre, fecha):
    agenda[nombre.capitalize()] = fecha
    print('Contacto creado')
    print(agenda)

def consulta(agenda, nombre):
    if nombre.capitalize() in agenda.keys():
        print('La fecha de nacimiento de {}, es: {}'.format(nombre.capitalize(), agenda[nombre.capitalize()]))
    else:
        print('La persona no existe en la lista, quieres crearla? S/N')
        respuesta = input('>')
        if respuesta.lower() == 's':
            fecha = input('Ingresa su fecha de nacimiento:')
            addContact(agenda, nombre, fecha)
        else:
            print('Saliendo del programa.')

print('Agenda electronica.')
print('Indica el nombre de la persona a buscar')
busqueda = input('>')
consulta(agenda, busqueda)