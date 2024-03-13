# -*- coding: utf-8 -*-
"""
Contiene un programa para realizar una gráfica del crecimiento
del hongo RhizopusOrizae en un alimento.

@author: Michael
@date: Feb 2024
"""

import matplotlib.pyplot as plt
import hongo


def main():
    """
    Programa principal que crea el sistema para el hongo Rhizopus Orizae
    y pone datos en pantalla
    """
    # Se crea el sistema para un hongo Rhizopus Orizae con estos parámetros:
    # y_0=0: diámetro inicial de las colonias (mm)
    # y_max=3.5: diámetro máximo de las colonias (mm)
    # vel_max=0.36: velocidad de crecimiento (mm/h)
    # v=10/24: parámetro de curvatura de transición a la fase exponencial (1/h)
    # condiciones: T=20C, pH=3, aW=0.895
    y_0: float = 0.0
    y_max: float = 3.5
    vel_max: float = 0.36
    v: float = 10.0/24.0
    condiciones: str = "T=20C, pH=3, aW=0.895"

    # Dibujar la gráfica de crecimiento del sistema 1
    # Creamos dos listas vacías para los puntos de la gráfica
    list_tiempo: list[float] = []
    list_diametro: list[float] = []

    # bucle para incrementar el tiempo entre 0 y 200 h, con 1h de incremento
    for tiempo in range(0, 201):
        # se simula el sistema insertando los datos en la gráfica
        list_tiempo.append(tiempo)
        list_diametro.append(hongo.diametro(tiempo, y_0, vel_max, y_max, v))

    # dibujar la gráfica
    plt.plot(list_tiempo, list_diametro, "red", label=condiciones)

    # Decoraciones
    plt.ylabel("diámetro (mm)")
    plt.xlabel("Tiempo(h)")
    plt.title("Crecimiento de Rhizopus Orizae")
    plt.grid(True)
    plt.legend()

    # Mostrar la gráfica
    plt.show()

if __name__ == "__main__":
    main()