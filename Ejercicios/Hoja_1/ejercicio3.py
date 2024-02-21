# -*- coding: utf-8 -*-
"""
Simula el movimiento oscilatorio de una masa que
pende de un muelle, sin considerar rozamientos

Se usan unidades del sistema internacional:

@author: Michael
@date  : ene-2022
"""

from typing import Final

# Constantes:
#    CTE_ELASTICA: Constante elástica del muelle, en N/m
#    G: Gravedad terrestre, en m/s^2
CTE_ELASTICA: Final[float] = 0.52
G: Final[float] = 9.8


def fuerza_muelle(alt: float) -> float:
    """
    Calcula la fuerza que ejerce el muelle
    dada la altura de su extremo

    Args:
    alt: la altura del extremo del muelle, en m
    Returns:
    la fuerza que ejerce el muelle, en N
    """

    # Retornamos la fuerza calculada por medio de la ley de Hooke
    return -CTE_ELASTICA*alt


def avanza_tiempo(alt: float, vel: float, masa: float, tiempo: float) -> tuple[float, float]:
    """
    Calcula la nueva altura y velocidad de la masa,
    transcurrido un tiempo especificado

    El tiempo debe ser pequeño, para poder considerar la
    aceleración constante en ese intervalo

    Args:
    alt: la altura actual del extremo del muelle, en m
    vel: la velocidad actual del extremo del muelle, m/s
    masa: la masa del cuerpo que pende del muelle, en Kg
    tiempo: el tiempo transcurrido, en s
    Returns:
    la nueva altura y velocidad de la masa,
    después de transcurrido un tiempo t
    """

    # Calculamos la fuerza aplicada sobre la masa, en N
    fuerza = fuerza_muelle(alt) - masa*G
    # Aceleración por la ley de newton
    aceleracion = fuerza/masa
    # Ecuacion del movimiento uniformemente acelerado
    return (alt + vel*tiempo + (aceleracion*tiempo**2)/2,vel + aceleracion*tiempo)


def main():
    pass
"""
Simula el movimiento de una masa suspendida de un
muelle durante un tiempo, y pone en pantalla
altura y velocidad. Unidades del S.I.
"""
masa: float = 0.25
incremento: float = 0.01
alt: float = 0.2
vel: float = 0

# Avanzar la simulación y mostrar resultados
print("Altura=", alt, "m. Velocidad=", vel, "m/s")
alt, vel = avanza_tiempo(alt, vel, masa, incremento)
print("Altura=", alt, "m. Velocidad=", vel, "m/s")
alt, vel = avanza_tiempo(alt, vel, masa, incremento)
print("Altura=", alt, "m. Velocidad=", vel, "m/s")
