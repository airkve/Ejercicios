# 

nombre = ''

while True:
    nombre = input('Quien eres?\n')
    if nombre != 'Richard':
        continue
    
    pasw = input('Hola Richard, cual es la contraseña? (Es un pez)\n')

    if pasw == 'bacalao':
        break

print('Acceso permitido!')