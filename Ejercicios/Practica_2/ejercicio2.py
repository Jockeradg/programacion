# -*- coding: utf-8 -*-
"""
Descripción: Como en la anterior práctica, este programa resuelve un sistema de ecuaciones lineales de 2x2, mediante la librería numpy y la función solve.

@autor: Adriel Diego
@date: 20/02/2024

"""
import numpy as np # Importar la librería numpy para resolver el sistema de ecuaciones

if __name__ == "__main__": # Si se ejecuta este archivo, se ejecutará lo siguiente, pero si se importa como paquete, no se ejecutará
    
 # Definir las ecuaciones
 
 # Coeficientes de las incógnitas
 coeficientes_1 = np.array([[1, -2], [3.5, -4]])
 coeficientes_2 = np.array([[1, -2], [4, -8]])

 # Términos independientes
 terminos_independientes_1 = np.array([3, 2])
 terminos_independientes_2 = np.array([3, 7])

 # Resolver el sistema de ecuaciones
 try:
    solucion_1 = np.linalg.solve(coeficientes_1, terminos_independientes_1)
    # Imprimir las soluciones
    print("El valor del primer sistema para x es:", solucion_1[0])
    print("El valor del primer sistema para y es:", solucion_1[1])
 except:
    print("El sistema de ecuaciones 1 no tiene solución")
 try:
    solucion_2 = np.linalg.solve(coeficientes_2, terminos_independientes_2)
    # Imprimir las soluciones
    print("El valor del segundo sistema para x es:", solucion_2[0])
    print("El valor del segundo sistema para y es:", solucion_2[1])
 except:
    print("El sistema de ecuaciones 2 no tiene solución")