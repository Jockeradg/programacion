# -*- coding: utf-8 -*-
"""
Descripción: Este es un ejemplo de un archivo de Python

@autor: Adriel Diego
@date: 21/02/2024
"""

a1 = 1
b1 = -2
c1 = 3
a2 = 3.5
b2 = -4
c2 = 8.5
"""
Declaro las variables con los valores de los coeficientes de las incógnitas y los términos independientes
"""
y = (c1*a2-a1*c2)/(a2*b1-a1*b2)
x = (c2-b2*y)/a2
"""
Guardo en las variables x e y los valores de las soluciones del sistema de ecuaciones mediante el método de sustitución
"""
print("El valor del segundo sistema para x es:", x)
print("El valor del segundo sistema para y es:", y)
""" 
Imprimo las soluciones del sistema de ecuaciones
"""