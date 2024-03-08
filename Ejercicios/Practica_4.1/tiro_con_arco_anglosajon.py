# -*- coding: utf-8 -*-
"""
Descripción: Este programa calcula la energía potencial elástica, la velocidad de salida,
la altura alcanzada por una flecha disparada con un arco anglosajón y verifica si el disparo
da en la diana. También muestra una gráfica de la trayectoria.

@autor: Adriel Diego
@date: 06/Marzo/2024

"""
import math
import simulador_trayectoria

# Constantes
K:float = 400  # N/m
M:float = 0.055  # kg
G:float = 9.81  # m/s^2
DIST_DIANA:float = 70  # m
RADIO_DIANA:float = 0.6  # m


PULGADA_TO_CM: float = 2.54
MILLA_TO_KM: float = 1.6093
PIE_TO_CM: float = 30.48
LBF_FT_TO_J: float = 1.3558


def energia_potencial(estira: float) -> float:
    """
    Calcula la energía potencial elástica de un arco.
    
    Parametros:
    estira (float): La distancia de estiramiento del arco en metros.
    
    Returns:
    float: La energía potencial elástica del arco en julios.
    """
    return 0.5 * K * estira**2

def velocidad_salida(e_p: float) -> float:
    """
    Calcula la velocidad de salida de un objeto basado en su energía potencial.

    Parámetros:
    e_p (float): La energía potencial del objeto.

    Returns:
    float: La velocidad de salida del objeto.
    """
    return (2 * e_p / M)**0.5


def altura(despl: float, v_s: float, angulo: float) -> float:
    """
    Calcula la altura alcanzada por una flecha disparada con un arco anglosajón.

    Parámetros:
    despl (float): La distancia horizontal recorrida por la flecha (en metros).
    v_s (float): La velocidad inicial de la flecha (en metros por segundo).
    angulo (float):  El ángulo de disparo del arco (en radianes).

    Retorna:
    La altura alcanzada por la flecha (en metros).
    """
    return despl * math.tan(angulo) - (9.8 * despl**2) / (2 * v_s**2 * math.cos(angulo)**2)


def main():
    """
    Función principal que realiza el cálculo de la energía potencial, velocidad de salida,
    altura en la diana y si el disparo da en la diana. También muestra una gráfica de la trayectoria.
    """
    # Solicitar el estiramiento del arco realizado por el arquero, en pulgadas
    estiramiento_pulgadas = float(input("Ingrese el estiramiento del arco realizado por el arquero (en pulgadas): "))
    
    # Solicitar el ángulo del disparo realizado por el arquero, en grados
    angulo_grados = float(input("Ingrese el ángulo del disparo realizado por el arquero (en grados): "))
    
    # Convertir unidades al Sistema Internacional
    estira = estiramiento_pulgadas * PULGADA_TO_CM / 100  # Convertir a metros
    angulo = math.radians(angulo_grados)  # Convertir ángulo a radianes

    print("Energía potencial: ", energia_potencial(estira) / LBF_FT_TO_J, "Lbf * Ft")
    print("Velocidad de salida: ", velocidad_salida(energia_potencial(estira)) / MILLA_TO_KM, "mph")
    print("Altura en la diana: ", (abs(altura(DIST_DIANA, velocidad_salida(energia_potencial(estira)), angulo)) / PIE_TO_CM), "ft")
    print("Da en la diana: ", abs(altura(DIST_DIANA, velocidad_salida(energia_potencial(estira)), angulo)) < RADIO_DIANA)
    simulador_trayectoria.pinta_grafica(estira, angulo)

if __name__ == "__main__":
    main()
