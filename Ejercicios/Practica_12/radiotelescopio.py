# -*- coding: utf-8 -*-
"""
Se desea hacer parte del software de análisis de las señales de radio captadas
por un radiotelescopio provenientes de una supernova.
Se dispone para ello de los datos del radiotelescopio almacenados en un
fichero con formato "csv".

@author: Adriel Diego González
@date: 15/05/2024
"""

from __future__ import annotations
import math
import matplotlib.pyplot as plt
import numpy as np


class Modelo:
    """
    Clase que representa el modelo de un flujo monocromático de una supernova.

    Attributes:
        __s_t (float): Densidad de flujo máxima en mJy.
        __v_t (float): Frecuencia a la que ocurre la densidad de flujo máxima
                      en GHz.
        __p (float): Exponente de la función de flujo.
    """

    def __init__(self, s_t: float, v_t: float, p: float):
        """
        Constructor de la clase Modelo.

        Args:
            s_t (float): Densidad de flujo máxima en mJy.
            v_t (float): Frecuencia a la que ocurre la densidad de flujo máxima
                         en GHz.
            p (float): Exponente de la función de flujo.
        """
        self.__s_t: float = s_t
        self.__v_t: float = v_t
        self.__p: float = p

    def flujo_modelo(self, frec: float) -> float:
        """
        Método que retorna el flujo monocromático en mJy dado un valor de
        frecuencia.

        Args:
            frec (float): La frecuencia en GHz.

        Returns:
            float: El flujo monocromático en mJy.
        """
        return 1.582*self.__s_t*math.pow(frec/self.__v_t, 5.0/2.0) * \
            (1-math.exp(-(math.pow(frec/self.__v_t, -(self.__p+4.0)/2.0))))


class ObsMonocromatica:
    """
    Contiene los datos de una observación de una supernova a través de un
    radiotelescopio, para una frecuencia única.

    Attributes:
        __frec (float): Frecuencia en GHz.
        __flujo (float): Flujo de radiación monocromática observada en mJy.
        __err_flujo (float): Error en la medida del flujo de radiación
                             monocromática en mJy.
    """

    def __init__(self, frec: float, flujo: float, err_flujo: float):
        """
        Constructor que inicializa los datos de la observación.

        Args:
            frec (float): Frecuencia en GHz.
            flujo (float): Flujo de radiación monocromática observada en mJy.
            err_flujo (float): Error en la medida del flujo de radiación
                               monocromática en mJy.
        """
        self.__frec: float = frec
        self.__flujo: float = flujo
        self.__err_flujo: float = err_flujo

    def get_frec(self) -> float:
        """Retorna la frecuencia en GHz."""
        return self.__frec

    def get_flujo(self) -> float:
        """Retorna el flujo monocromático en mJy."""
        return self.__flujo

    def get_err_flujo(self) -> float:
        """Retorna el error del flujo monocromático en mJy."""
        return self.__err_flujo


class Observacion:
    """
    Contiene los datos de una observación de una supernova a través de un
    radiotelescopio.

    Attributes:
        __lista: recoge los datos de varias observaciones monocromáticas
                 realizadas en el mismo día a diferentes frecuencias.
        __tiempo: el tiempo transcurrido desde el inicio de la supernova,
                  (en días)
    """

    def __init__(self, tiempo: float):
        """
        Constructor al que se le pasa el tiempo transcurrido desde el
        inicio de la supernova.

        Crea la lista vacía y anota el tiempo en un atributo

        Args:
            tiempo: el tiempo transcurrido desde el inicio de la supernova,
                    en días
        """
        self.__lista: list[ObsMonocromatica] = []
        self.__tiempo: float = tiempo

    def anade(self, obs: ObsMonocromatica):
        """
        Añade una observación monocromática a la lista.

        Args:
            obs: Un objeto conteniendo una observación monocromática
        """
        self.__lista.append(obs)

    def elimina(self, indice: int):
        """
        Elimina de la lista la observación monocromática cuyo índice se indica.

        Args:
            indice: el índice de la observacióm monocromática que se desea
                    eliminar

        Raises:
            IndiceIncorrecto: El índice no está comprendido entre 0 y el
                              número de elementos de la lista - 1.
        """
        if indice < 0 or indice >= len(self.__lista):
            raise IndiceIncorrecto
        # Borra de la lista la observación con el índice indicado
        del self.__lista[indice]

    def indice_con_error_grande(self, error_relativo: float) -> int:
        """
        Busca la primera observación que tenga un error relativo superior
        al indicado.

        Args:
            error_relativo: se busca un error relativo superior a este
            parámetro, en tanto por uno

        Returns:
            Índice de la casilla de la lista que contiene una observación
            con error relativo superior al indicado, o -1 si no hubiese
            ninguna.
        """
        for i, obs in enumerate(self.__lista):
            if obs.get_err_flujo() / obs.get_flujo() > error_relativo:
                return i
        return -1

    def chi_cuadrado_ponderado(self, mod: Modelo) -> float:
        """
        Retorna la estadística chi cuadrado ponderada según los errores de
        las medidas, dados los valores de estas por el método
        flujo_modelo() del objeto mod.

        Args:
            mod: el objeto de la clase Modelo que contiene la fórmula del flujo

        Returns:
            El valor de chi cuadrado ponderado.
        """
        # TODO: Parte avanzada: chi_cuadrado_ponderado()

    def frec_flujo_max(self) -> float:
        """
        Retorna la frecuencia a la que el flujo observado es máximo.

        Returns:
            Frecuencia a la que el flujo es máximo (GHz).
        """
        max_flujo_obs = max(obs.get_flujo() for obs in self.__lista)
        frec_max_flujo = next((obs.get_frec() for obs in self.__lista if obs.get_flujo() == max_flujo_obs),None)
        return frec_max_flujo

    @staticmethod
    def lee_fichero(nombre_fichero: str) -> Observacion:
        """
        Lee de un fichero en formato csv los datos de la observación de una
        supernova y los retorna en un objeto de la clase Observacion.

        Raises:
            IOError: El fichero no existe.
            ErrorDeFormato: El formato del fichero csv es incorrecto.
        """
        try:
            with open(nombre_fichero, 'r') as fichero:
                for i in range(4):
                    next(fichero)
                
                tiempo = float(next(fichero).split(',')[1].strip())
                obs = Observacion(tiempo)
                for i in range(4):
                    next(fichero)
                for linea in fichero:
                    campos = linea.strip().split(',')
                    if len(campos) != 3:
                        raise ErrorDeFormato
                    frec = float(campos[0])
                    flujo = float(campos[1])
                    err_flujo = float(campos[2])
                    obs.anade(ObsMonocromatica(frec, flujo, err_flujo))
                return obs
        except FileNotFoundError:
            raise IOError
        except ValueError:
            raise ErrorDeFormato
        """
            with open(nombre_fichero, 'r') as fichero:
                for i in range(3):
                    next(fichero)  
                # Leemos el tiempo de la supernova
                tiempo = float(fichero.readline().strip())
                # Creamos el objeto Observacion
                obs = Observacion(tiempo)
                # Leemos las observaciones monocromáticas
                for linea in fichero:
                    campos = linea.strip().split(',')
                    if len(campos) != 3:
                        raise ErrorDeFormato
                    frec = float(campos[0])
                    flujo = float(campos[1])
                    err_flujo = float(campos[2])
                    obs.anade(ObsMonocromatica(frec, flujo, err_flujo))
                return obs
        except FileNotFoundError:
            raise IOError
        except ValueError:
            raise ErrorDeFormato
        """
    def plot(self, mod: Modelo):
        """
        Dibuja una comparativa entre los valores medidos y el modelo.

        Args:
            mod: el objeto de la clase Modelo que contiene la fórmula del flujo
        """
        # Creamos las listas de frecuencia y flujo observados así como
        # la de los errores
        lista_frec: list[float] = [obs.get_frec() for obs in self.__lista]
        lista_observada: list[float] = [obs.get_flujo()
                                        for obs in self.__lista]
        errores: list[float] = [obs.get_err_flujo() for obs in self.__lista]

        # Creamos las listas de frecuencia y flujo según el modelo
        fr_min: float = min(lista_frec)
        fr_max: float = max(lista_frec)
        lista_frec_modelo: np.ndarray = np.linspace(fr_min, fr_max, 100)
        lista_modelo: list[float] = [mod.flujo_modelo(frec)
                                     for frec in lista_frec_modelo]

        # Hacemos el dibujo de los valores observados, los errores y los
        # valores predichos por el modelo
        plt.plot(lista_frec, lista_observada, color='blue', marker='o',
                 linestyle='None', label='Valores observados')
        plt.errorbar(lista_frec, lista_observada, yerr=errores, color='blue',
                     linestyle='None')
        plt.plot(lista_frec_modelo, lista_modelo, color='red',
                 label='Valores del modelo')
        # Decoraciones
        plt.xlabel('frec(GHz)')
        plt.ylabel('flujo(mJy)')
        plt.title(f'Flujo de la supernova a los {self.__tiempo} días')
        plt.legend()
        plt.show()


class IndiceIncorrecto(Exception):
    """
    El índice no está entre 0 y la longitud de la lista -1
    """


class ErrorDeFormato(Exception):
    """
    El fichero contiene errores de formato
    """


def main():
    """
    Programa principal para analizar las observaciones de una supernova.
    """
    try:
        # a) Lee el fichero CSV llamado SN2011dh.csv
        observacion = Observacion.lee_fichero("SN2011dh.csv")
        
        # b) Busca casillas con error relativo de flujo mayor que 0.5
        indice_error_grande = observacion.indice_con_error_grande(0.5)
        print("Casilla con error relativo de flujo mayor que 0.5: ", indice_error_grande)
        
        # c) Busca casillas con error relativo de flujo mayor que 0.45 y elimina
        indice_error_mayor = observacion.indice_con_error_grande(0.45)
        print("Casilla con error relativo de flujo mayor que 0.45: ", indice_error_mayor)
        if indice_error_mayor != -1:
            observacion.elimina(indice_error_mayor)
        
        # d) Muestra la frecuencia a la que el flujo es máximo
        frec_max_flujo = observacion.frec_flujo_max()
        print(f"La frecuencia a la que el flujo es máximo es: {frec_max_flujo} GHz")
        
        # e) Crea un objeto de la clase Modelo
        modelo = Modelo(7.635, 4.017, 3.0)
        
        # f) Muestra una gráfica comparativa
        observacion.plot(modelo)
        
    except IOError:
        print("El fichero no existe.")
    except ErrorDeFormato:
        print("El formato del fichero csv es incorrecto.")

if __name__ == "__main__":
    main()
