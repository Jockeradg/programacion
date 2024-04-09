# -*- coding: utf-8 -*-
"""
Descripción: Programa que calcula el periodo, velocidad inicial, posición 
y velocidad de una partícula cargada en un campo eléctrico

@autor: Adriel Diego
@date: 27/03/2024

"""

from typing import Final
import math
import numpy as np
import matplotlib.pyplot as plt

EPSILON: Final[float] = 8.85e-12

class ParticulaCargada:
    """
    Creación de una clase ParticulaCargada que calcula el periodo, velocidad inicial, posición
    y velocidad de una partícula cargada en un campo eléctrico con los siguientes atributos:
    - masa: float
    - pos_ini: float
    - fuerza: float
    """
    
    def __init__(self,q:float, sigma:float, masa:float, pos_ini:float):
        """
        Constructor de la clase ParticulaCargada

        Args:
            q (float): Carga de la partícula
            sigma (float): Valor sigma del campo eléctrico
            masa (float): Masa de la partícula
            pos_ini (float): Posición inicial de la partícula
        """
        self.__masa:float = masa
        self.__pos_ini:float = pos_ini
        self.__fuerza:float = abs(sigma/(2*EPSILON)*q)

    def pos_ini(self)->float:
        """
        Método que devuelve la posición inicial de la partícula

        Returns:
            float: Posición inicial de la partícula
        """
        return self.__pos_ini
    
    def periodo(self)->float:
        """
        Método que devuelve el periodo del movimiento oscilatorio de la partícula

        Returns:
            float: Periodo del movimiento oscilatorio
        """
        return 4*math.sqrt(2*self.__masa*self.__pos_ini/self.__fuerza)
    
    def velocidad_origen(self)->float:
        """
        Método que devuelve la velocidad inicial de la partícula

        Returns:
            float: Velocidad inicial de la partícula
        """
        return math.sqrt(2*self.__fuerza*self.__pos_ini/self.__masa)
    
    def posicion(self,t:float)->float:
        """
        Método que devuelve la posición de la partícula en función del tiempo

        Args:
            t (float): Tiempo

        Returns:
            float: Posición de la partícula
        """
        tiempo = t%self.periodo()
        t_0:float = self.periodo()/4
        v_0: float = self.velocidad_origen()
        delta_t: float = tiempo - t_0
        delta_3t_0: float = tiempo - 3*t_0
        d: float = 1/2*self.__fuerza/self.__masa

        if tiempo < t_0:
            return self.pos_ini() - d*tiempo**2
        
        elif tiempo < 3*t_0:
            return -v_0*delta_t + d*delta_t**2
        
        else:   
            return v_0*delta_3t_0 - d*delta_3t_0**2
        
    def velocidad(self,t:float)->float:
        """
        Método que devuelve la velocidad de la partícula en función del tiempo

        Args:
            t (float): Tiempo

        Returns:
            float: Velocidad de la partícula
        """
        tiempo = t%self.periodo()
        t_0:float = self.periodo()/4
        if tiempo < t_0:
            return -self.__fuerza/self.__masa*tiempo
        
        elif tiempo < 3*t_0:
            return -self.velocidad_origen() + self.__fuerza/self.__masa*(tiempo-(t_0))
        
        else:
            return self.velocidad_origen() - self.__fuerza/self.__masa*(tiempo-(3*t_0))
  
def plot_posicion_vs_tiempo(particle):
    """
    Función que grafica la posición y velocidad de una partícula en función del tiempo

    Args:
        particle ()
    """
    list_x: list[float]= list(np.linspace(0, 1.5*ParticulaCargada.periodo(particle), 100))
    list_vel: list[float] = []
    list_pos: list[float] = []
    for i in list_x:
        list_vel.append(particle.velocidad(i)/particle.velocidad_origen())
        list_pos.append(particle.posicion(i)/particle.pos_ini())

    plt.plot(list_x, list_pos, 'g^', label='Posición normalizada')
    plt.plot(list_x, list_vel, 'ro', label='Velocidad normalizada')
    plt.xlabel('Tiempo/periodo')
    plt.ylabel('Valor normalizado')
    plt.grid(True)
    plt.legend()
    plt.show()
 
def main():
    """
    Función principal que crea una partícula cargada y muestra el periodo, velocidad inicial, posición
    y velocidad de la partícula en función del tiempo
    """
    Particula_1 = ParticulaCargada(-1.602e-19,150e-6 ,9.1e-31,0.001)
    print(f"Periodo del movimiento oscilatorio (4t0): {Particula_1.periodo():10.3e} s")   
    print(f"Velocidad inicial (v0): {Particula_1.velocidad_origen():10.3e} m/s")
    print("Posiciones y velocidades para valores de t entre 0 y 6t0 con salto de 0.5t0:")
    print("Tiempo(s)    \t    Posicion(m)    \t  Velocidad(m/s)")
    tiempo = 0
    for i in range(13):
        print(f"{tiempo}\t {Particula_1.posicion(tiempo):10.3e}\t{Particula_1.velocidad(tiempo):10.3e}")
        tiempo += 0.5*Particula_1.periodo()/4
    plot_posicion_vs_tiempo(Particula_1)


if __name__ == "__main__":
    main()
