# -*- coding: utf-8 -*-
"""
Descripción: Este programa calcula el diámetro de las colonias del hongo 
Rhizopus Orizae en función del tiempo.


@autor: Adriel Diego
@date: 13/03/2024

"""
import math
from fundamentos.escritura import Escritura

M:float = 0.06 # 1/mm
HO:float = 2.757 # Sin dimensiones

def ajuste(tiempo: float, v: float)->float:
    """
    Función que devuelve el ajuste del crecimiento del hongo a una función 
    exponencial.
    Args:
        tiempo (float): tiempo de crecimiento del hongo
        v (float): velocidad de crecimiento del hongo

    Returns:
        float: crecimiento ajustado
    """
    q_0:float = (1)/(math.exp(HO)-1)
    a:float = tiempo + (1/v)*math.log((math.exp(-v*tiempo)+q_0)/(1+q_0))
    return a

def diametro(tiempo:float, y_0:float, vel_max:float, y_max:float, v:float)->float:
    """
    Función que devuelve el diámetro de las colonias del hongo Rhizopus Orizae 
    en función del tiempo.

    Args:
        tiempo (float): tiempo dado en horas
        y_0 (float): diámetro inicial de las colonias (mm)
        vel_max (float): velocidad de crecimiento (mm/h)
        y_max (float): diámetro máximo de las colonias (mm)
        v (float): parámetro de curvatura de transición a la fase exponencial 
        en horas-1

    Returns:
        float: diámetro en milímetros
    """
    a: float = ajuste(tiempo, v)
    diametro:float = y_0 + vel_max*a - (1/M)*math.log(1+((math.exp(M*vel_max*a)-1) \
                                                         /(math.exp(M*(y_max-y_0)))))
    return diametro


 

def main():
    # Se crea el sistema para un hongo Rhizopus Orizae con estos parámetros:
    y_0:float = 0 # diámetro inicial de las colonias (mm)
    y_max:float = 3.5 # diámetro máximo de las colonias (mm)
    v_max:float = 0.36 # velocidad de crecimiento (mm/h)
    v:float = 10/24 # parámetro de curvatura de transición a la fase exponencial (1/h)
    condiciones:str = "T=20C, pH=3, aW=0.895"

    # Dibujar una tabla con los datos del sistema
    print(f"Sistema para condiciones {condiciones}")
    print(f"diámetro( 0h): {diametro(0, y_0, v_max, y_max, v):.4f} mm")
    print(f"diámetro( 50h): {diametro(50, y_0, v_max, y_max, v):.4f} mm")
    print(f"diámetro(100h): {diametro(100, y_0, v_max, y_max, v):.4f} mm")
    print(f"diámetro(150h): {diametro(150, y_0, v_max, y_max, v):.4f} mm")

    """
    Mediante el paquete fundamentos.escritura, se crea un objeto de la clase 
    Escritura, se insertan los valores de la función diametro en la tabla y se 
    espera a que el usuario
    se dé por enterado para destruir la ventana.
    """
    # Paso 1: crear el objeto de la clase Escritura
    escr = Escritura("Datos del experimento")
 
    # Paso 2: crear las entradas para mostrar datos
    escr.inserta_valor("diametro( 0h)", f"{diametro(0, y_0, v_max, y_max, v):.5f} mm")
    escr.inserta_valor("diametro( 50h)", f"{diametro(50, y_0, v_max, y_max, v):.5f} mm")
    escr.inserta_valor("diametro(100h)", f"{diametro(100, y_0, v_max, y_max, v):.5f} mm")
    escr.inserta_valor("diametro(150h)", f"{diametro(150, y_0, v_max, y_max, v):.5f} mm")
    
 
    # Paso 3: esperar a que el usuario se dé por enterado
    escr.espera()
 
    # Paso 4: destruir la ventana
    escr.destruye()


if __name__ == "__main__":
    main()
