# -*- coding: utf-8 -*-
"""
Descripción: Este es un ejemplo de un archivo de Python

@autor: Adriel Diego
@date: 20/02/2024

"""
import numpy as np # Importar la librería numpy para resolver el sistema de ecuaciones


if __name__ == "__main__": # Si se ejecuta este archivo, se ejecutará lo siguiente, pero si se importa como paquete, no se ejecutará

 # Definir las ecuaciones
 
 # Coeficientes de las incógnitas
 coeficientes = np.array([[1, -2], [4, 2]])

 # Términos independientes
 terminos_independientes = np.array([3, 2])

 # Resolver el sistema de ecuaciones
 solucion = np.linalg.solve(coeficientes, terminos_independientes)

 # Imprimir las soluciones
 print("El valor para x es:", solucion[0])
 print("El valor para y es:", solucion[1])