# -*- coding: utf-8 -*-
"""
Contiene clases y un programa para simular el funcionamiento de un sistema de
evitación de colisiones en un coche autónomo

TODO @author:
TODO @date:
"""

# TODO: otros imports
import math
import sys
from fundamentos.dibujo import Dibujo, Ovalo, Texto, Rectangulo


class Obstaculo:
    """
    Clase que representa un obstáculo en la carretera.

    Attributes:
        __id: entero que identifica al obstaculo
        __v_t: velocidad tangencial, en m/s
        __v_n: velocidad normal, en m/s
        __d: distancia al obstaculo en m
        __alfa: angulo al obstaculo, en radianes
        __r: radio del obstaculo, en m
    """

    def __init__(self, identificador: int, radio: float):
        """
        Constructor de la clase Obstaculo. Recibe como parámetros los valores
        iniciales de los atributos id y r (m) y pone el resto de los atributos
        a cero

        Args:
            identificador (int): Identificador del obstáculo.
            radio (float): Radio del obstáculo en metros (m).
        """
        self.__id: int = identificador
        self.__v_t: float = 0.0
        self.__v_n: float = 0.0
        self.__d: float = 0.0
        self.__alfa: float = 0.0
        self.__r: float = radio

    def set(self, v_t: float, v_n: float, dist: float, alfa: float):
        """
        Actualiza los atributos de velocidad tangencial, velocidad normal,
        distancia y ángulo al obstáculo.

        Args:
            v_t (float): Velocidad tangencial en metros por segundo (m/s).
            v_n (float): Velocidad normal en metros por segundo (m/s).
            dist (float): Distancia al obstáculo en metros (m).
            alfa (float): Ángulo al obstáculo en grados.
        """
        self.__v_t = v_t
        self.__v_n = v_n
        self.__d = dist
        self.__alfa = math.radians(alfa)

    def t_alcance(self, v_c: float) -> float:
        """
        Calcula el tiempo hasta alcanzar el obstáculo en la dirección del
        coche.

        Args:
            v_c (float): Velocidad del coche en metros por segundo (m/s).

        Returns:
            float: Tiempo hasta alcanzar el obstáculo en segundos (s).
        """
        return (self.__d*math.cos(self.__alfa)-self.__r)/(v_c-self.__v_n)

    def t_rebase(self, v_c: float, lng: float) -> float:
        """
        Calcula el tiempo hasta rebasar el obstáculo en la dirección del coche.

        Args:
            v_c (float): Velocidad del coche en metros por segundo (m/s).
            lng (float): Longitud del coche en metros (m).

        Returns:
            float: Tiempo hasta rebasar el obstáculo en segundos (s).
        """
        return (self.__d*math.cos(self.__alfa)+self.__r+lng)/(v_c-self.__v_n)

    def margen_alcance(self, v_c: float) -> float:
        """
        Calcula el margen de distancia tangencial entre el coche y el obstáculo
        cuando transcurra el tiempo de alcance.

        Args:
            v_c (float): Velocidad del coche en metros por segundo (m/s).

        Returns:
            float: Margen de distancia tangencial en metros (m).
        """
        return self.__d*math.sin(self.__alfa)+self.__v_t*self.t_alcance(v_c)

    def margen_rebase(self, v_c: float, lng: float) -> float:
        """
        Calcula el margen de distancia tangencial entre el coche y el obstáculo
        cuando transcurra el tiempo de rebase.

        Args:
            v_c (float): Velocidad del coche en metros por segundo (m/s).
            lng (float): Longitud del coche en metros (m).

        Returns:
            float: Margen de distancia tangencial en metros (m).
        """
        return self.__d*math.sin(self.__alfa) + \
            self.__v_t*self.t_rebase(v_c, lng)

    def get_id(self) -> int:
        """
        Observador del atributo id.

        Returns:
            int: Identificador del obstáculo.
        """
        return self.__id

    def get_radio(self) -> float:
        """
        Observador del atributo r.

        Returns:
            float: Radio del obstáculo en metros (m).
        """
        return self.__r

    def get_distancia(self) -> float:
        """
        Observador del atributo d.

        Returns:
            float: Distancia al obstáculo en metros (m).
        """
        return self.__d

    def get_angulo(self) -> float:
        """
        Observador del atributo alfa, pero en grados

        Returns:
            float: Radio del obstáculo en grados (º).
        """
        return math.degrees(self.__alfa)


class NoEncontradoError(Exception):
    """
    Excepción lanzada cuando no se encuentra un obstáculo.
    """


class Coche:
    """
    Clase que representa un coche y su sistema de detección de colisiones.

    Attributes:
        __lista: una lista de obstaculos
        __v_c: velocidad del coche en m/s
        __A: Semianchura del coche en m
        __L: longitud del coche en m
    """

    def __init__(self, v_c: float, semi_ancho: float, lng: float,
                 nombre_fichero: str):
        """
        Constructor de la clase Coche.

        Args:
            v_c (float): Velocidad del coche en metros por segundo (m/s).
            semi_ancho (float): Semianchura del coche en metros (m).
            lng (float): Longitud del coche en metros (m).
            nombre_fichero (str): Nombre del archivo de texto del que se leen
                                  los datos de los obstáculos.
        """
        # TODO: constructor

    def __leer_obstaculos(self, filename: str):
        """
        Lee los datos de los obstáculos desde un archivo de texto y los
        mete en el atributo __lista
        Si el fichero no existe se finaliza el programa

        Args:
            filename: el nombre del fichero del que se leen los datos
        """
        # Código para leer los datos del archivo y crear los obstáculos
        try:
            with open(filename, "r", encoding="utf-8") as fich:
                fich.readline()  # saltamos la primera línea
                for linea in fich:
                    # separamos por los espacios en blanco
                    numeros = linea.split()
                    iden: int = int(numeros[0])
                    v_t: float = float(numeros[1])
                    v_n: float = float(numeros[2])
                    dist: float = float(numeros[3])
                    alfa: float = float(numeros[4])
                    radio: float = float(numeros[5])
                    # Crear el obstaculo con los datos leidos
                    nuevo = Obstaculo(iden, radio)
                    nuevo.set(v_t, v_n, dist, alfa)
                    # Anadir el obstaculo a la lista
                    self.__lista.append(nuevo)
        except IOError:
            print(f"El fichero {filename} no existe")
            input("Pulsar <intro> para finalizar el programa")
            sys.exit()

    def posibles_choques(self) -> list[Obstaculo]:
        """
        Retorna una lista conteniendo todos los obstáculos para los que se
        detecta un posible choque.

        Returns:
            list[Obstaculo]: Lista de obstáculos que pueden chocar.
        """

        # TODO: posibles_choques()

    def informe(self):
        """
        Pone en pantalla un informe de todos los obstáculos.
        """
        # TODO: Parte avanzada: informe()

    def poco_margen_alcance(self) -> Obstaculo:
        """
        Busca el primer obstáculo cuyo margen de alcance en valor absoluto es
        menor o igual que r+A y lo retorna.

        Returns:
            Obstaculo: El primer obstáculo con poco margen de alcance.

        Raises:
            NoEncontradoError: Si no se encuentra ningún obstáculo con poco
                               margen de alcance.
        """
        # TODO: poco_margen_alcance()

    @staticmethod
    def __coord_x(c_x: float, escala: float, size: float) -> int:
        """
        Transforma un punto c_x al sistema de coordenadas del dibujo

        Args:
            c_x (float): punto en coordenadas del coche en m
            escala (float): factor de escala.
            size (float): tamaño de la ventana.

        Returns:
            La coordenada x en el sistema de coordenadas del dibujo en píxeles

        """
        return int(size/2+c_x*escala)

    @staticmethod
    def __coord_y(c_y: float, escala: float, size: float) -> int:
        """
        Transforma un punto c_y al sistema de coordenadas del dibujo

        Args:
            c_y (float): punto en coordenadas del coche en m
            escala (float): factor de escala.
            size (float): tamaño de la ventana.

        Returns:
            La coordenada y en el sistema de coordenadas del dibujo en píxeles

        """
        return int(size/2+c_y*escala)

    def __pinta(self, dib: Dibujo, obs: Obstaculo, escala: float, size: float,
                color: str):
        """
        Pinta un obstaculo en el dibujo

        Args:
            dib (Dibujo): lienzo donde se dibuja.
            obs (Obstaculo): el obstáculo que se dibuja.
            escala; float (TYPE): escala del dibujo.
            size (float): tamaño de la ventana.
            color: el color del obstáculo, en inglés
        """
        c_x: float = obs.get_distancia() * \
            math.cos(math.radians(90-obs.get_angulo()))
        c_y: float = obs.get_distancia() * \
            math.sin(math.radians(90-obs.get_angulo()))
        radio: float = obs.get_radio()
        # Las indicaciones de que las variables obstaculo y texto no se usan
        # son incorrectas y deben ignorarse
        obstaculo = Ovalo(dib, self.__coord_x(c_x-radio, escala, size),
                          self.__coord_y(-c_y-radio, escala, size),
                          self.__coord_x(c_x+radio, escala, size),
                          self.__coord_y(-c_y+radio, escala, size), color)
        texto = Texto(dib, self.__coord_x(c_x, escala, size)-20,
                      self.__coord_y(-c_y+10, escala, size),
                      f"{obs.get_id()}", "black", 8)
        dib.pinta()

    def dibujo_esquematico(self):
        """
        Hace un dibujo esquematico de los obstaculos y del coche
        """
        size: int = 800
        dib = Dibujo("Obstaculos", size, size)
        # Averiguar la escala del dibujo, buscando la maxima X y la maxima Y
        max_x: float = max((abs(obs.get_distancia() *
                                math.cos(math.radians(90-obs.get_angulo())) +
                                obs.get_radio()) for obs in self.__lista))
        max_y: float = max((abs(obs.get_distancia() *
                                math.sin(math.radians(90-obs.get_angulo())) +
                                obs.get_radio()) for obs in self.__lista))
        maximo: float = max(max_x, max_y)
        # factor de escala
        escala: float = (size/2-5)/(maximo)
        # pinta el coche a escala 5:1
        Rectangulo(dib, self.__coord_x(-self.__A, escala*5, size),
                   self.__coord_y(0, escala*5, size),
                   self.__coord_x(self.__A, escala*5, size),
                   self.__coord_y(self.__L, escala*5, size), "dark blue")

        # Pinta los obstaculos de verde
        for obs in self.__lista:
            self.__pinta(dib, obs, escala, size, "green")

        # Pinta los obstaculos peligrosos de rojo
        peligro: list[Obstaculo] = self.posibles_choques()
        for obs in peligro:
            self.__pinta(dib, obs, escala, size, "red")

        # muestra el dibujo
        dib.espera()
        dib.destruye()


def main():
    """
    Programa que prueba los metodos de la clase Coche
    """
    # TODO: main()
