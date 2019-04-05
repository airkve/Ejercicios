def hola(nombre):
    print('Hola {}!'.format(nombre))
    print('Hola {}!!!'.format(nombre))
    print('Bienvenido {}!'.format(nombre))
    return len(nombre)

hola('Alicia')
hola('Bob')
hola('Richard')

longN = hola(input())
print('El nombre mide: ', longN)

# Declaracion global

def spam():
    global huevos
    huevos = 'spam'

huevos = 'jamon'
spam()
print(huevos)

# Exception Handling

try:
    pass
except: #palabra reservada
    pass
else:
    pass
finally:
    pass