# -*- coding: utf-8 -*-
"""
Clase que contiene una lista de ciudades y los costes de las viviendas,
así como métodos para trabajar con estos datos

@author: ...
@date: ...
"""
import math

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

def calcular_coste(self, ciudad: str) -> float:
    """
        Calcula y retorna el coste de la vivienda para la ciudad que se pasa como parámetro.

        Args:
            ciudad (str): Nombre de la ciudad.

        Returns:
            float: Coste de la vivienda por metro cuadrado, en €.

        Raises:
            NoEncontradoError: Si ninguna ciudad de la lista coincide con el parámetro ciudad.
        """
    try:
        """
        precio:float = next((self.__costes[i] for i,x in enumerate(self.__ciudades) if x == ciudad), math.nan)
        if math.isnan(precio):
            raise NoEncontradoError("La ciudad no se encuentra en la lista.")
        return precio
        """
        for c, coste in zip(self.__ciudades, self.__costes):
            if c == ciudad:
                return coste
    except Exception:
        raise NoEncontradoError("La ciudad no se encuentra en la lista.")