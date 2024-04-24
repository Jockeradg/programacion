# -*- coding: utf-8 -*-
"""
TODO: documentación del módulo

TODO @author:
TODO @date:
"""

from __future__ import annotations
import math
import random
from typing import Final
from fundamentos.dibujo import Dibujo, Imagen, Texto, Linea

# Posición inicial del avión, en píxeles
X_INICIAL: Final[int] = 50
Y_INICIAL: Final[int] = 50


class Posicion:
    """
    Clase para representar una posición geográfica en términos de latitud y
    longitud.

    Attributes:
        __lat: Latitud en grados decimales
        __lng: Longitud en grados decimales
    """

    def __init__(self, lat: float, lng: float):
        """
        Inicializa una nueva instancia de la clase Posicion.

        Args:
            lat: Latitud en grados decimales.
            lng: Longitud en grados decimales.
        """
        self.__lat: float = lat
        self.__lng: float = lng

    def get_lat(self) -> float:
        """
        Obtiene la latitud de la posición.

        Returns:
            La latitud en grados decimales.
        """
        return self.__lat

    def get_lng(self) -> float:
        """
        Obtiene la longitud de la posición.

        Returns:
            La longitud en grados decimales.
        """
        return self.__lng

    def __str__(self) -> str:
        """
        Retorna una representación textual de la posición.
        Esta representación se usa automáticamente al hacer un print()
        de un objeto de tipo Posicion

        Returns:
            Una cadena de texto que representa la posición en el formato
            "(latitud, longitud)" redondeada a dos decimales
        """
        return f"({self.__lat:.2f}, {self.__lng:.2f})"

    def distancia(self, pos: Posicion) -> float:
        """
        Calcula la distancia en kilómetros entre la posición actual y otra
        posición dada.

        Args:
            pos: Otra posición.

        Returns:
            La distancia entre las dos posiciones en kilómetros.
        """
        # Radio aproximado de la Tierra en kilómetros
        radio_tierra: float = 6371.0

        # Convertir latitud y longitud de grados decimales a radianes
        lat_1: float = math.radians(self.__lat)
        lng_1: float = math.radians(self.__lng)
        lat_2: float = math.radians(pos.get_lat())
        lng_2: float = math.radians(pos.get_lng())

        # Diferencia de latitud y longitud
        dlat: float = lat_2 - lat_1
        dlng: float = lng_2 - lng_1

        # Fórmula de Haversine para calcular la distancia entre dos puntos
        # en la superficie de una esfera
        a: float = math.sin(dlat / 2)**2 + math.cos(lat_1) * math.cos(lat_2) \
            * math.sin(dlng / 2)**2
        c: float = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Distancia en kilómetros
        return radio_tierra * c


class Pantalla:
    """
    Clase para representar una pantalla para mostrar información de trayectoria
    de aviones.

    Attributes:
        __dibujo: ventana de la clase Dibujo donde se pintará la trayectoria
        __anterior_x: última coordenada X, en pixels
        __anterior_y: última coordenada Y, en pixels
        __angulo: ángulo de la trayectoria, en rad
        __num_errores: número de errores acumulados
        __imagen: Imagen para representar el avión
        __texto_error: mensaje de error para poner en pantalla
    """

    def __init__(self):
        """
        Constructor que crea una ventana para mostrar información de
        trayectoria.
        """
        self.__dibujo = Dibujo("Trayectoria de Aviones", 500, 500)
        self.__anterior_x: int = int(X_INICIAL*400/160+250)
        self.__anterior_y: int = int(Y_INICIAL*400/160)
        self.__angulo: float = 0.0
        self.__num_errores: int = 0
        self.__imagen: Imagen | None = None
        self.__texto_error: Texto | None = None

    def pinta_punto_tray(self, p: Posicion):
        """
        Pinta en la ventana un punto de la trayectoria que ha seguido un avión.

        Args:
            p: La posición del punto a pintar en la trayectoria.
        """
        cx: int = int((p.get_lng()*400/160+250))
        cy: int = 250 - int((p.get_lat()*400/160))
        lin = Linea(self.__dibujo, self.__anterior_x, self.__anterior_y,
                    cx, cy, "blue")
        self.__dibujo.pinta()
        # calcula el angulo de la trayectoria
        self.__angulo = -math.atan2(cy-self.__anterior_y, cx-self.__anterior_x)
        self.__anterior_x = cx
        self.__anterior_y = cy

    def pinta_avion(self, id_avion: int, p: Posicion):
        """
        Muestra en la ventana una foto del avión en la posición actual
        especificada por p.

        Args:
            id_avion: El identificador del avión.
            p: La posición actual del avión.
        """
        cx: int = int(p.get_lng()*400/160+250)
        cy: int = 250 - int(p.get_lat()*400/160)
        ang: int = int((math.degrees(self.__angulo)) % 360) // 45
        nombre_fichero: str = f"avion{int(ang*45)}.png"
        self.__imagen = Imagen(self.__dibujo, cx, cy, nombre_fichero)
        texto = Texto(self.__dibujo, cx+20, cy, str(id_avion), "red", 10)
        self.__dibujo.pinta()

    def muestra_alarma(self, mensaje: str):
        """
        Muestra en pantalla un mensaje de alarma.

        Args:
            mensaje: El mensaje de alarma a mostrar.
        """
        self.__num_errores += 1
        if self.__texto_error is not None:
            self.__texto_error.borra()
        self.__texto_error = Texto(self.__dibujo, 250, 15,
                                   f"Error {self.__num_errores}. {mensaje}",
                                   "dark red", 10)
        self.__dibujo.pinta()

    def destruye_pantalla(self):
        """
        Destruye la ventana en la que se representa la trayectoria
        """
        self.__dibujo.espera()
        self.__dibujo.destruye()


class Radar:
    """
    Se ofrece una simulacion que retorna datos sinteticos

    Class Attributes
        __y: latitud, en grados
        __x: longitud, en grados
        __delta_x: incremento de longitud a cada paso, en grados
        __delta_y: incremento de latitud a cada paso, en grados
    """
    # latitud (y) y longitud (x), en grados
    __y: float = X_INICIAL
    __x: float = Y_INICIAL

    # incrementos de latitud y longitud a cada paso, en grados
    __delta_x: float = 1.4
    __delta_y: float = 3.0/400*160

    @classmethod
    def lee_posicion_actual(cls, id_avion: int) -> Posicion | None:
        """
        Retorna la posicion actual del avion identificado por __id_avion.
        Si el radar no logra encontrar el avion, retorna None

        Args:
            id_avion (int): el identificador del avion cuya posicion se desea.

        Returns:
            la posicion del avion, o None si no se ha encontrado.

        """
        # Al exceder los límites del dibujo vamos en direccion contraria
        if cls.__x > 80 or cls.__x < -80:
            cls.__delta_x = -cls.__delta_x
        if (cls.__y > 80 or cls.__y < -80):
            cls.__delta_y = -cls.__delta_y
        cls.__x += cls.__delta_x
        cls.__y += cls.__delta_y
        # Simulamos un fallo de radar
        if random.random() < 0.01:
            # fallo de radar
            return None
        # retornamos la posicion correcta
        return Posicion(cls.__y, cls.__x)

class Trayectoria:
    lista: list[Posicion] = []
    id_avion: int = 0
    ventana: Pantalla = Pantalla()

    def __init__(self, id_avion: int):
        self.id_avion = id_avion
        self.ventana = Pantalla()
        self.__lista = []

    def muestra_avion(self):
        for punto in self.__lista:
            self.ventana.pinta_punto_tray(punto)
        ultima_posicion = self.__lista[-1]
        self.ventana.pinta_avion(self.id_avion, ultima_posicion)

    def pasa_cerca(self, p: Posicion, dist: float)->bool:
        return next((True for punto in self.__lista if punto.distancia(p) < dist), False)
    
    def recoge_posiciones(self, n:int):
        anadidos: int = 0
        while anadidos < n:
            p: Posicion | None = Radar.lee_posicion_actual(self.id_avion)
            if p is None:
                self.ventana.muestra_alarma("No se pudo obtener la posición del avión")
            else:
                self.__lista.append(p)
                anadidos += 1
                
    #def estan_dentro_rectangulo(self, esquina_sup_dch:Posicion,esquina_inf_izq:Posicion)->list[Posicion]:
        #return [punto for punto in self.__lista if esquina_inf_izq.get_lat() <= punto.get_lat() <= esquina_sup_dch.get_lat() and esquina_inf_izq.get_lng() <= punto.get_lng() <= esquina_sup_dch.get_lng()]
    
    def destruye_ventana(self):
        self.ventana.destruye_pantalla()
        

def main():
    avion1 = Trayectoria(8834)
    avion1.recoge_posiciones(200)
    avion1.muestra_avion()
    p = Posicion(57,57)
    if avion1.pasa_cerca(p, 200):
        print("La trayectoria pasa cerca de la posición de 200 km.")
    else:
        print("La trayectoria no pasa cerca de la posición de 200 km.")

    if avion1.pasa_cerca(p, 1):
        print("La trayectoria pasa cerca de la posición de 1 km.")
    else:
        print("La trayectoria no pasa cerca de la posición de 1 km.")
    
    avion1.destruye_ventana()

if __name__ == "__main__":
    main()