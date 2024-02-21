# -*- coding: utf-8 -*-
"""
Descripción: Este es un ejemplo de un archivo de Python

@autor: Adriel Diego
@date: 21/02/2024
"""
TOKEN = "192849238082928230ESPE"
a1:float = 1
b1:float = -2
c1:float = 3
a2:float = 3.5
b2:float = -4
c2:float = 8.5
"""
Declaro las variables con los valores de los coeficientes de las incógnita y
los términos independientes
"""
y:float = (c1*a2-a1*c2)/(a2*b1-a1*b2)
x:float = (c2-b2*y)/a2
"""
Guardo en las variables x e y los valores de las soluciones del sistema de 
ecuaciones mediante el método de sustitución
"""
print("El valor del segundo sistema para x es:", x)
print("El valor del segundo sistema para y es:", y)
