# -*- coding: utf-8 -*-
"""
Este módulo contiene funciones para mostrar una grafica de
la simulación del lanzamiento de una flecha con un arco de cuerda

@author: Michael
@date:   Feb 2024
"""

from fundamentos.dibujo import Dibujo
from fundamentos.dibujo import Ovalo
from fundamentos.dibujo import Imagen
import tiro_con_arco


def pinta_grafica(estira: float, angulo: float):
    """
    Realiza una simulación gráfica del lanzamiento de una flecha
    con un arco

    Args:
        estira (float): el estiramiento del arco, en m.
        angulo (float): el ángulo de tiro, en radianes.
    """

    # Datos para el dibujo
    size_x: int = 640
    size_y: int = 480
    origen_x: int = 145  # píxeles
    final_x: int = 60
    origen_y: int = 157  # píxeles
    # píxeles/m
    escala_x: float = (size_x-origen_x-final_x) / \
        tiro_con_arco.DIST_DIANA
    # píxeles/m
    escala_y: float = (size_y-origen_y)/50

    # Obtener velocidad inicial
    v_i: float = tiro_con_arco.velocidad_salida(
        tiro_con_arco.energia_potencial(estira))

    # Dibuja el escenario
    dib = Dibujo("Simulación de tiro con arco", 640, 480)
    escenario = Imagen(dib, size_x//2, size_y//2+(size_y-255)//2,
                       "escenario.png")

    # Dibuja la posición de la flecha en diversos puntos
    for pos_x in range(0, int(tiro_con_arco.DIST_DIANA)+1):
        alt: float = tiro_con_arco.altura(pos_x, v_i, angulo)
        # dibuja un punto de la trayectoria
        c_x: int = int(round(pos_x*escala_x+origen_x))
        c_y: int = 480-int(round(alt*escala_y+origen_y))
        circ = Ovalo(dib, c_x-3, c_y-3, c_x+3, c_y+3, "red")

    # Pintamos el dibujo y esperamos a que se cierre la ventana
    dib.espera()

    # Destruimos el dibujo
    dib.destruye()
