from clases.Tablero import *
from clases.Conventions import *
from clases.Case import instances
from random import choice
from itertools import product, repeat
from juego import LONGITUDES_BARCOS, HORIZONTAL, ORIENTACIONES

instances = []
casillas_ocupadas = set()

# performance / legibilidad:
class Bote:
    def __init__(self, longitud, casillas):#el parametro no tiene que llevar la misma letra que los atributos
            self.longitud = longitud
            self.orientacion = choice(ORIENTACIONES)
            self.tocado = False
            self.hundido = False
            self.casillas = casillas

    def horizontal(self):

        if self.orientacion == HORIZONTAL:
            rang = choice(range(num_lineas))
            primero = choice(range(num_columnas + 1 - LONGITUDES_BARCOS))
            letra = num2l(rang)
            cifras = [num2c(x) for x in range(primero, primero + LONGITUDES_BARCOS)]
            self.casillas = {instances[l + c]
                            for l, c in product(repeat(letra, LONGITUDES_BARCOS), cifras)}
        else:
            rang = choice(range(num_columnas))
            primero = choice(range(num_lineas + 1 - LONGITUDES_BARCOS))
            cifra = num2c(rang)
            letras = [num2l(x) for x in range(primero, primero + LONGITUDES_BARCOS)]
            # Crear el barco
            self.casillas = {instances[l + c]
                            for l, c in product(letras, repeat(cifra, LONGITUDES_BARCOS))}


    def vertical(self):
            for existente in instances:
                if self.casillas.intersection(existente.casillas):
                    break  # break relativo al "for existente in barcos:"
            else:
                # Agregar el barco en el contenedor de barcos
                instances.append(self)
                # Informar la casilla que contiene un barco.
                for casilla in self.casillas:
                    casilla.barco = self
                # Agregar estas casillas a las casillas ocupadas :
                    
                    casillas_ocupadas |= self.casillas
                

    @classmethod
    def generar_barcos(cls):
        for longitud in Conventions.barcos_longitud:
            longitud = longitud