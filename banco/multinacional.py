from cliente import Cliente
from base64 import b64encode, b64decode
import re

class Multinacional(Cliente):

    def __init__(self, email, clave, razon_soc, cuit, direccion):
        super().__init__(email, clave)
        self.razon_soc = razon_soc
        self.cuit = cuit
        self.direccion = direccion

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

    def set_razon_soc(self, data):
        self.razon_soc = data
        
    def set_cuit(self, data):
        self.cuit = data

    def set_direccion(self, data):
        self.direccion = data

    def get_razon_soc(self):
        return self.razon_soc

    def get_cuit(self):
        return self.cuit

    def get_direccion(self):
        return self.direccion