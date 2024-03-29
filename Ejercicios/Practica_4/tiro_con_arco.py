# -*- coding: utf-8 -*-
"""
Descripción: Este es un ejemplo de un archivo de Python

@autor: Adriel Diego
@date: 06 Febrero

"""
import math
import simulador_trayectoria

# Constants
K:float = 400  # N/m
M:float = 0.055  # kg
G:float = 9.81  # m/s^2
DIST_DIANA:float = 70  # m
RADIO_DIANA:float = 0.6  # m

# Functions
def energia_potencial(estira: float) -> float:
    return 0.5 * K * estira**2

def velocidad_salida(e_p: float) -> float:
    return (2 * e_p / M)**0.5

def altura(despl: float, v_s: float, angulo: float) -> float:
    return despl * math.tan(angulo) - (G * despl**2) / (2 * v_s**2 * math.cos(angulo)**2)

def main():
    # Solicitar el estiramiento del arco realizado por el arquero, en cm
    estiramiento_cm = float(input("Ingrese el estiramiento del arco realizado por el arquero (en cm): "))
    
    # Solicitar el ángulo del disparo realizado por el arquero, en grados
    angulo_grados = float(input("Ingrese el ángulo del disparo realizado por el arquero (en grados): "))
    
    # Convertir unidades al Sistema Internacional
    estira = estiramiento_cm / 100  # Convertir estiramiento a metros
    angulo = math.radians(angulo_grados)  # Convertir ángulo a radianes

    print("Energía potencial: ",energia_potencial(estira),"J")
    print("Velocidad de salida: ",velocidad_salida(energia_potencial(estira)),"km/h")
    print("Altura en la diana: ",(abs(altura(DIST_DIANA, velocidad_salida(energia_potencial(estira)), angulo)))/100,"cm")
    print("Da en la diana: ", abs(altura(DIST_DIANA, velocidad_salida(energia_potencial(estira)), angulo))<RADIO_DIANA)
    simulador_trayectoria.pinta_grafica(estira, angulo)

if __name__ == "__main__":
    main()