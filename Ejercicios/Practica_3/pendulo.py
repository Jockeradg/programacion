# -*- coding: utf-8 -*-
"""
TODO Descripción del módulo

@author: Adriel Diego
@date: 28/02/2024
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt

# Constantes

L: float = 1.0  # Longitud del péndulo, en m
PHI_MAX: float = 0.2  # Amplitud máxima, en radianes
G: float = 9.81  # m/s^2

# Funciones


def phi_aprox(tiempo:float)->float:
    """
    Calcula la posición angular de un péndulo simple
    para pequeñas amplitudes

    Args:
        tiempo (float): tiempo en segundos

    Returns:
        phi (float): posición angular en radianes
    """
    phi: float = PHI_MAX*mt.cos(mt.sqrt(G/L)*tiempo)
    return phi

def muestra_grafica():
    """
    Muestra una gráfica de la oscilación de un péndulo simple

    Permite ver gráficamente los resultados para la aproximación
    de pequeñas amplitudes
    """

    # Intervalo entre un tiempo y el siguiente, en s
    intervalo: float = 0.01

    # Creamos una lista para el tiempo, entre 0 y 10 segundos,
    # con valores separados por el valor intervalo
    list_t: list[float] = list(np.linspace(0.0, 10.0, int(10.0/intervalo)))

    # creamos una lista vacía para las posiciones
    # con pequeñas amplitudes
    list_pa: list[float] = []

    # Recorremos la lista del tiempo y añadimos a la lista
    # de posiciones la posición angular para cada valor del tiempo
    for tiempo in list_t:
        list_pa.append(phi_aprox(tiempo))

    # Creamos la grafica para dibujar la trayectoria
    # con la aproximación de pequeñas amplitudes
    plt.plot(list_t, list_pa, "red", label="pequeñas amplitudes")

    # Decoraciones
    plt.ylabel("Angulo (rad)")
    plt.xlabel("Tiempo(s)")
    plt.title("Trayectoria de un péndulo")
    plt.grid(True)
    plt.legend()

    # Mostrar la gráfica
    plt.show()

def muestra_diferencias():
    """
    Muestra en pantalla la tabla con las diferencias relativas
    entre los ángulos en radianes y el seno.
    """
    # Añadimos los datos en grados
    grado1: float = 2.0
    grado2: float = 5.0
    grado3: float = 10.0
    grado4: float = 15.0

    print("Grados\t\tRadianes\t\t\tSeno\t\tDif(%)")
    print(f"{grado1}\t\t{round((mt.radians(grado1)),5)}\t\t{mt.sin(mt.radians(grado1))}\t\t{100*((mt.radians(grado1))-(mt.sin(mt.radians(grado1))))/(mt.radians(grado1))}")
    print(f"{grado2}\t\t{round((mt.radians(grado2)),5)}\t\t{mt.sin(mt.radians(grado2))}\t\t{100*((mt.radians(grado2))-(mt.sin(mt.radians(grado2))))/(mt.radians(grado2))}")
    print(f"{grado3}\t\t{round((mt.radians(grado3)),5)}\t\t{mt.sin(mt.radians(grado3))}\t\t{100*((mt.radians(grado3))-(mt.sin(mt.radians(grado3))))/(mt.radians(grado3))}")
    print(f"{grado4}\t\t{round((mt.radians(grado4)),5)}\t\t{mt.sin(mt.radians(grado4))}\t\t{100*((mt.radians(grado4))-(mt.sin(mt.radians(grado4))))/(mt.radians(grado4))}")
    """
        Se calcula la diferencia relativa entre el ángulo en radianes y el seno
    """

def main():
    """
    Función principal
    """
    print(phi_aprox(0))
    print(phi_aprox(0.5))
    print(phi_aprox(1))
    muestra_grafica()
    muestra_diferencias()

main()