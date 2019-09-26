#!python3
# Clase que define las propiedades y acciones de los capitanes

from pirata import Pirata
from barco import Barco

class Capitan(Pirata, Barco):
    """ Clase que define los componentes de un capitan. """
    
    def __init__(self, rep):
        self.reputacion = rep
        def Pirata.(self, nombre, habilidad):
            # Atributos de los piratas
            self.nombre = nombre
            self.habilidad = habilidad
        
    def setReputacion(self, rep):
        self.reputacion = rep
        
    def getReputacion(self):
        return self.reputacion
    
    def dar_ordenes(self):
        pass
    
    def crear_tripulacion(self):
        pass
    
    def preguntar_loro(self):
        pass
    
    def enterrar_tesoro(self):
        pass