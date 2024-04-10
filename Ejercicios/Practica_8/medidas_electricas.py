# -*- coding: utf-8 -*-
"""
Descripción: Programa que calcula la tensión en un condensador en un circuito.

@autor: Adriel Diego
@date: 10/04/2024

"""
import fundamentos
import math
from fundamentos.escritura import Escritura
from fundamentos.lectura import Lectura
import numpy as np
import matplotlib.pyplot as plt

class Circuito:
    """
    Creaacion de clase de un circuito.
    """
    def __init__(self, c: float, r: float, v_e: float):
        """
        Clase constructora de un circuito, la cual guarda los valores de cada objeto

        Args:
            c (float): Capacidad del condesador
            r (float): Resistencia del circuito
            v_e (float): Voltaje de la fuente
        """
        self.__c = c
        self.__r = r
        self.__v_e = v_e

    def tension_condensador (self, t: float, t_0: float) ->float:
        """
        Funcion que calcula la tensión en un condensador en un circuito.

        Args:
            t (float): tiempo en segundos
            t_0 (float): tiempo en segundos

        Returns:
            float: Devuelve la tensión en el condensador en un circuito.
        """
        if t <= t_0:
            return self.__v_e*(1 - math.exp(-t/(self.__r*self.__c)))
        elif t > t_0:
            return self.tension_condensador(t_0,t_0)*(math.exp(-(t-t_0)/(self.__r*self.__c)))
        

def alcanza_tension(circ: Circuito, t_0: float, valor_tension: float)->float:
    """
    Funcion que calcula el instante en el que se alcanza una tensión en un condensador en un circuito.

    Args:
        circ (Circuito): El objeto de la clase Circuito
        t_0 (float): Tiempo inicial en segundos
        valor_tension (float): Valor de la tensión en el condensador en un circuito

    Returns:
        float: Devuelve el tiempo en segundos en que se llega a la tension querida
        y si nunca llega devuelve nan
    """
    incremento: float = 0.0001 # s
    tiempo: float = 0.0 # s
    repetir: bool = True
    tension: float # V
    while repetir:

        tiempo = tiempo + incremento
        tension = circ.tension_condensador(tiempo, t_0)
        repetir = tension < valor_tension and tiempo <= t_0

    if tension >= valor_tension:
        return tiempo
    else:
        return math.nan
    

def voltaje_vs_tiempo(Circ: Circuito, t0: float,tmax: float):
    """
    Función que grafica el voltaje de un circuito

    Args:
        Circuito1 (Circuito): Objeto de la clase Circuito
        t0 (float): Tiempo inicial en segundos
        tmax (float): Tiempo final en segundos
    """
    list_x: list[float]= list(np.linspace(0, tmax, 100))
    list_vol: list[float] = []
    for i in list_x:
        list_vol.append(Circ.tension_condensador(i,t0))

    plt.title('Tension del condensador')
    plt.plot(list_x, list_vol, 'red',)
    plt.xlabel('t(ms)')
    plt.ylabel('Vc(V)')
    plt.grid(True)
    plt.legend()
    plt.show()
    
def main():
 
    # Paso 1: crear el objeto de la clase Lectura
    lec = Lectura("Datos del circuito")
 
    # Paso 2: crear las entradas para leer datos
    lec.crea_entrada("C (F)", 2e-6)
    lec.crea_entrada("R (ohm)", 1000)
    lec.crea_entrada("Ve (V)", 5)
    lec.crea_entrada("t0 (s)", 0.005)
 
    # Paso 3: esperar a que el usuario teclee
    lec.espera()
 
    # Paso 4: leer los valores tecleados
    c: float = float(lec.lee_float("C (F)"))
    r: float = float(lec.lee_float("R (ohm)"))
    ve: float = float(lec.lee_float("Ve (V)"))
    t0:float = float(lec.lee_float("t0 (s)"))
 
    # Usar los valores obtenidos
    Circuito1 = Circuito(c, r, ve)
 
    # Paso final: destruir la ventana
    lec.destruye()

    # Paso 1: crear el objeto de la clase Escritura
    escr = Escritura("Tensión del condesador")
 
    # Paso 2: crear las entradas para mostrar datos
    escr.inserta_valor(f"Vc en t=0ms",f"{Circuito1.tension_condensador(0, t0):.4} V")
    escr.inserta_valor(f"Vc en t=1ms ",f"{Circuito1.tension_condensador(0.001, t0):.4} V")
    escr.inserta_valor(f"Vc en t=2ms" ,f"{Circuito1.tension_condensador(0.002, t0):.4} V")
    escr.inserta_valor(f"Vc en t=10ms",f"{Circuito1.tension_condensador(0.01, t0):.4} V")

    # Paso 3: esperar a que el usuario se dé por enterado
    escr.espera()
 
    # Paso 4: destruir la ventana
    escr.destruye()

    print(f"Instante en el que se alcanza 4 V: {str(alcanza_tension(Circuito1, t0, 4)):.6}")
    print(f"Instante en el que se alcanza 6 V: {str(alcanza_tension(Circuito1, t0, 6)):.6}")

    voltaje_vs_tiempo(Circuito1, t0,0.020)
if __name__ == "__main__":
    main()
