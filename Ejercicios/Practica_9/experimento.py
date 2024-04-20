# -*- coding: utf-8 -*-
"""
Programa que realiza un ajuste por regresión lineal a un conjunto de datos y
muestra los resultados obtenidos.

@author: Adriel Diego
@date: 18/04/2024
"""


import numpy as np
import matplotlib.pyplot as plt
import random
from fundamentos.escritura import Escritura
import math


class Coeficientes:
    """
    Clase para almacenar los resultados de un ajuste por regresión lineal.

    Atributos:
        a (float): Coeficiente 'a' de la ecuación de la recta (y = ax + b).
        b (float): Coeficiente 'b' de la ecuación de la recta (y = ax + b).
        r (float): Coeficiente de correlación entre los datos experimentales
                   y los ajustados.
    """

    def __init__(self, a: float, b: float, r: float):
        """
        Constructor de la clase Coeficientes.

        Args:
            a (float): Coeficiente 'a' de la ecuación de la recta.
            b (float): Coeficiente 'b' de la ecuación de la recta.
            r (float): Coeficiente de correlación.
        """
        self.__a: float = a
        self.__b: float = b
        self.__r: float = r

    def coef_a(self) -> float:
        """
        Método observador para obtener el coeficiente 'a'.

        Returns:
            float: Coeficiente 'a' de la ecuación de la recta.
        """
        return self.__a

    def coef_b(self) -> float:
        """
        Método observador para obtener el coeficiente 'b'.

        Returns:
            float: Coeficiente 'b' de la ecuación de la recta.
        """
        return self.__b

    def correlacion(self) -> float:
        """
        Método observador para obtener el coeficiente de correlación.

        Returns:
            float: Coeficiente de correlación entre los datos experimentales
                   y los ajustados.
        """
        return self.__r


class Estadistica:
    """
    Clase para almacenar un conjunto de datos y realizar un ajuste por regresión.

    Atributos:
        __x (list): Lista con los valores de la variable independiente.
        __y (list): Lista con los valores de la variable dependiente.
    """

    def __init__(self):
        """
        Constructor de la clase Estadistica.

        Crea dos listas vacias para almacenar los valores de las variables.
        """
        self.__x = []
        self.__y = []
    
    def inserta(self, val_x: float, val_y: float):
        """
        Inserta un par de valores en las listas de datos.

        Args:
            val_x (float): Valor de la variable independiente.
            val_y (float): Valor de la variable dependiente.
        """
        self.__x.append(val_x)  
        self.__y.append(val_y)
    
    def num_datos(self):
        """
        Método observador para obtener el número de datos almacenados.

        Returns:
            int: Número de datos almacenados.
        """
        return len(self.__x)
    

    def pinta_regresion_lineal(self, coef: Coeficientes):
        """
        Muestra una gráfica de los puntos y la regresión lineal.

        Args:
            coef: Objeto de la clase Coeficientes que contiene los coeficientes
                  de la regresión y la correlación
        """
        if coef is not None:
            y_pred = coef.coef_a() * np.array(self.__x) + \
                coef.coef_b()
            plt.plot(self.__x, y_pred, color='red', label='Regresión lineal')
            plt.plot(self.__x, self.__y, color='blue', marker='o',
                     label='Datos experimentales')
            plt.xlabel('x')
            plt.ylabel('y=f(x)')
            plt.title('Regresión lineal')
            plt.legend()
            plt.show()
        else:
            print("El tamaño de los datos es insuficiente.")

    def regresion_lineal(self):
        """
        Realiza un ajuste por regresión lineal a los datos almacenados.

        Returns:
            tuple[float,float,float]: Coeficientes de la regresión lineal (a, b, r).
        """
        n = self.num_datos()
        if n < 2:
            return None
        x = (self.__x)
        y = (self.__y)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_x2 = sum(i**2 for i in x)
        sum_y2 = sum(i**2 for i in y)
        sum_xy = sum(x[i]*y[i] for i in range(n))
        a = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
        b = (sum_y - a*sum_x) / n
        r = (n*sum_xy - sum_x*sum_y) / math.sqrt((n*sum_x2 - sum_x**2)*(n*sum_y2 - sum_y**2))
        return Coeficientes(a, b, r)

    def media(self):
        """
        Método que calcula la media de los valores de y=f(x).

        Returns:
            float: Media de los valores de y=f(x).
        """
        if len(self.__x)<=2:
            return math.nan
        else:
            suma = sum((self.__y[i+1]+self.__y[i])/2*\
                       (self.__x[i+1]-self.__x[i]) for i in range(0,len(self.__x)-1))
            return (1/(self.__x[len(self.__x)-1]-self.__x[0])*suma)
        

def main():
    """
    Función principal del programa.
    """
    
    e = Estadistica()
    list_1 = [x*x for x in range(0,31)]
    list_2 = [(2*(list_1[i])+random.randrange(-100,100))  for i in range(0,31)]
    for i in range(0,31):
        e.inserta(list_1[i], list_2[i]) 
    
    escr = Escritura("Regresión Lineal: resultados")
    
    coef = e.regresion_lineal()
    escr.inserta_valor("Coeficiente a", f"{coef.coef_a()}")
    escr.inserta_valor("Coeficiente b", f"{coef.coef_b()}") 
    escr.inserta_valor("Coeficiente de correlación", f"{coef.correlacion()}")
    escr.inserta_valor("Media de y=f(x)",e.media())
    
    escr.espera()

    e.pinta_regresion_lineal(coef)

    escr.destruye()

    
if __name__ == "__main__":
    main()
