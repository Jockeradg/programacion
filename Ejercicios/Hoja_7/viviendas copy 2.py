# -*- coding: utf-8 -*-
"""
Clase que contiene una lista de ciudades y los costes de las viviendas,
así como métodos para trabajar con estos datos

@author: ...
@date: ...
"""
import sys

class CosteViviendas:
    """
    Esta clase contiene como atributos dos listas paralelas.
    La primera lista tiene nombres de ciudades y la segunda el coste
    de un metro cuadrado de vivienda, en €, en cada una de las ciudades
    de la primera lista

    Attributes:
        __ciudades: lista de nombres de ciudades
        __costes: lista de números reales con el coste de un metro cuadrado
                  de vivienda, en €, en cada una de las ciudades de la
                  primera lista
    """

    def __init__(self):
        """
        Constructor que crea las listas de
        ciudades y costes de las viviendas vacías
        """
        self.__ciudades: list[str] = []
        self.__costes: list[float] = []




    def inserta(self, ciudad: str, coste: float):
        """
        Inserta en las listas de ciudades y costes la ciudad y coste que
        se pasan como parámetros

        Args:
            ciudad (str): Nombre de la ciudad a insertar.
            coste (float): Coste de la vivienda por metro cuadrado, en €.
        """
        self.__ciudades.append(ciudad)
        self.__costes.append(coste)

    def informe(self):
        """
        Muestra en pantalla los datos de todas las viviendas
        """
        print("Coste por metro cuadrado de las viviendas, en €")
        for ciudad, coste in zip(self.__ciudades, self.__costes):
            print(f"{ciudad:15s}{coste:8.2f}")
    
    def leer_fichero(self, nombre_fichero: str):
        """
        Lee el fichero indicado por nombre_fichero y carga los datos en las listas
        de ciudades y costes de vivienda.

        Args:
                    nombre_fichero (str): Nombre del fichero a leer.
        """
        try:
            with open(nombre_fichero, 'r') as file:
                for line in file:
                    ciudad, coste = line.strip().split(',')
                    self.inserta(ciudad.strip(), float(coste.strip()))
        except FileNotFoundError:
            print(f"El fichero {nombre_fichero} no existe.")
        except Exception as e:
            print(f"Error al leer el fichero: {e}")

class NoEncontradoError(Exception):
    """
    Excepción personalizada para cuando no se encuentra la ciudad en la lista
    """
    pass
            
        


def main():
    # a) Crea un objeto de la clase CosteViviendas
    coste_viviendas = CosteViviendas()

    # b) Invoca a leer_fichero() para leer los datos de coste de vivienda del fichero de texto costes.txt
    coste_viviendas.leer_fichero("costes.txt")

    try:
        # c) Calcula con el método correspondiente el coste de la vivienda en “Madrid” y lo muestra en pantalla.
        coste_madrid = coste_viviendas.calcular_coste("Madrid")
        print(f"El coste de la vivienda en Madrid es: {coste_madrid} €")
    except NoEncontradoError:
        print("Error grave: No se encontró el coste de la vivienda en Madrid.")
        sys.exit(1)

    try:
        # d) Calcula con el método correspondiente el coste de la vivienda en “Soria” y lo muestra en pantalla.
        coste_soria = coste_viviendas.calcular_coste("Soria")
        print(f"El coste de la vivienda en Soria es: {coste_soria} €")
    except NoEncontradoError:
        print("Error leve: No se encontró el coste de la vivienda en Soria.")

    # e) Invoca al método informe() para mostrar los datos almacenados
    coste_viviendas.informe()
