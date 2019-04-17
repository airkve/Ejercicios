# Manejo de Excepciones

# try:
#     pass
# except expression as identifier:
#     pass
# else:
#     pass
# finally:
#     pass

def spam(dividirPor):
    return 42 / dividirPor

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Dividiste por cero')