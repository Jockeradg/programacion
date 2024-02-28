# -*- coding: utf-8 -*-
"""
Este programa crea una grafica de un

@author: Adriel Diego
@date: 28/02/2024
"""

import math as mt
import numpy as np
import matplotlib.pyplot as plt

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
    grado: float = 2.0
    radianes: float = round((mt.radians(grado)),5) # Grado a radianes
    seno: float = mt.sin(mt.radians(grado)) # Se calculo el seno del angulo
    aprox: float = 100*((mt.radians(grado))-(mt.sin(mt.radians(grado)))) \
        /(mt.radians(grado)) #Se calcula el error relativo en porcentaje
    print("Grados\t\tRadianes\t\t\tSeno\t\tDif(%)")

    print(f"{grado}\t\t{radianes}\t\t{seno}\t\t{aprox}")

    grado: float = 5.0
    radianes: float = round((mt.radians(grado)),5) # Grado a radianes
    seno: float = mt.sin(mt.radians(grado)) # Se calculo el seno del angulo
    aprox: float = 100*((mt.radians(grado))-(mt.sin(mt.radians(grado)))) \
        /(mt.radians(grado)) #Se calcula el error relativo en porcentaje

    print(f"{grado}\t\t{radianes}\t\t{seno}\t\t{aprox}")

    grado: float = 10.0
    radianes: float = round((mt.radians(grado)),5) # Grado a radianes
    seno: float = mt.sin(mt.radians(grado)) # Se calculo el seno del angulo
    aprox: float = 100*((mt.radians(grado))-(mt.sin(mt.radians(grado)))) \
        /(mt.radians(grado)) #Se calcula el error relativo en porcentaje

    print(f"{grado}\t\t{radianes}\t\t{seno}\t\t{aprox}")

    grado: float = 15.0
    radianes: float = round((mt.radians(grado)),5) # Grado a radianes
    seno: float = mt.sin(mt.radians(grado)) # Se calculo el seno del angulo
    aprox: float = 100*((mt.radians(grado))-(mt.sin(mt.radians(grado)))) \
        /(mt.radians(grado)) #Se calcula el error relativo en porcentaje

    print(f"{grado}\t\t{radianes}\t\t{seno}\t\t{aprox}")

def main():
    """
    Función principal
    """
    print("Tiempo: 0.00 s. Angulo",phi_aprox(0), "rad")
    print("Tiempo: 0.50 s. Angulo",phi_aprox(0.5),"rad")
    print("Tiempo: 1.00 s. Angulo",phi_aprox(1),"rad")
    muestra_grafica()
    muestra_diferencias()

main()