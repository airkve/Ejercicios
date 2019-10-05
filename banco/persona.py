from cliente import Cliente
from base64 import b64encode, b64decode
import re

class Persona(Cliente):

    def __init__(self, email, clave, nombre, apellido, documento):
        super().__init__(email, clave)
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento

    def set_email(self, data):
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", data):
            self.email = data
        else:
            print("Formato de email incorrecto.")

    def set_clave(self, pw):
        if re.match(r"[A-Za-z0-9@#$%^&+=]{8,}", pw):
            self.clave = b64encode(pw.encode())
        else:
            print('La clave tiene que tener 8 caracteres, mayuscula, simbolo, numeros y letras')

    def set_nombre(self, data):
        self.nombre = data
        
    def set_apellido(self, data):
        self.apellido = data

    def set_documento(self, data):
        self.documento = data

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_documento(self):
        return self.documento