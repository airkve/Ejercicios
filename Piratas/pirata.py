#!python3
# Clase que define las propiedades y acciones de los piratas

class Pirata(object):
    """ Clase que define la creacion de un pirata. """
    def __init__(self, nombre, habilidad):
        # Atributos de los piratas
        self.nombre = nombre
        self.habilidad = habilidad
        
    # Setters y getters
    def setNombre(self, data):
        self.nombre = data
    
    def getNombre(self):
        return self.nombre
    
    def setHabilidad(self, data):
        self.habilidad = data
        
    def getHabilidad(self):
        return self.habilidad
    
    # Acciones de los piratas
    def saquear(self):
        pass
    
    def tomar_ron(self):
        pass
    
    def luchar(self):
        pass
    
    def volar(self):
        pass
    
    def leer_mapa(self):
        pass
    
    def sumergirse(self):
        pass