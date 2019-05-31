# Crear una funcion que tome como parametro una lista, con 4
# elementos del tipo str y los muestre por consola, separados
# por un espacio y una coma

lst = ['Bienvenido', 'al', 'curso', 'de', 'python']

def transformList(data):
    for strings in data:
        print(strings + ', ', end='')

transformList(lst)