# Crear un programa que genere automaticamente 7 examenes con 24 pregruntas y las respuesta
# de modo aleatorio, listadas por seleccion simple

import random

provincias = {
    'Buenos Aires': 'La Plata',
    'Catamarca': 'San Fernando del Valle de Catamarca',
    'Chaco': 'Resistencia',
    'Chubut': 'Rawson',
    'Cordoba': 'Cordoba',
    'Corrientes': 'Corrientes',
    'Entre Rios': 'Parana',
    'Formosa': 'Formosa',
    'Jujui': 'San Salvador de Jujui',
    'La Pampa': 'Santa Rosa',
    'La Rioja': 'La Rioja',
    'Mendoza': 'Mendoza',
    'Misiones': 'Posadas',
    'Neuquen': 'Neuquen',
    'Rio Negro': 'Viedma',
    'Salta': 'Salta',
    'San Juan': 'San Juan',
    'San Luis': 'San Luis',
    'Santa Cruz': 'Rio Gallegos',
    'Santa Fe': 'Santa Fe',
    'Santiago del Estero': 'Santiago del Estero',
    'Tierra del Fuego': 'Ushuaia',
    'Tucuman': 'San Miguel de Tucuman'
}

encabezado = "Parcial No. {}\n\nNombre y apellido:\n"

def quizGenerator(cantidad):
    provLst = list(provincias.keys())
    random.shuffle(provLst)
    respLst = list(provincias.values())
    correctas = []
    erroneas = []
    for prov in provLst:
        correctas.append(provincias[prov])
    
    for i in range(7):
        archivo = open('ExamenParcial{}.txt'.format(i + 1), 'w')
