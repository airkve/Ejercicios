from abc import ABC, abstractclassmethod
import re

class Cliente(ABC):

    def __init__(self, email, clave):
        self.email = email
        self.clave = clave
        self.reclave = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")

    def set_email(self, data):
        pass
    def set_clave(self, pw):
        pass