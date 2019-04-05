# Crear un programa que muestre un contador con 5 digitos 0-0-0-0-0
# que muestre los numeros del 0-0-0-0-0 al 9-9-9-9-9
# cambiar el numero 3 por una E


for dig1 in range(10):
    for dig2 in range(10):
        for dig3 in range(10):
            for dig4 in range(10):
                for dig5 in range(10):
                    if dig1 == 3:
                        dig1 = 'E'
                    elif dig2 == 3:
                        dig2 = 'E'
                    elif dig3 == 3:
                        dig3 = 'E'
                    elif dig4 == 3:
                        dig4 = 'E'
                    elif dig5 == 3:
                        dig5 = 'E'
                    print('{}-{}-{}-{}-{}'.format(dig1, dig2, dig3, dig4, dig5), end='\r')
    
    
