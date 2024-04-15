# -*- coding: utf-8 -*-
"""
Descripción: Programa que calcula el logaritmo de una tupla de números.

@autor: Adriel Diego
@date: 13/04/2024

"""
import math

def calcular_logaritmos(tupla)->tuple:
    """
    Funcion que calcula el logaritmo de una tupla de numeros.

    Args:
        tupla (tuple): Tupla de 5 números reales

    Returns:
        tupla: Devuelve la tupla
    """
    return tuple([math.log(num) for num in tupla])

def main():
    """
    Funcion principal que ejecuta el programa.
    """
    numeros:tuple = (1, 2, 3, 4, 5)
    logaritmos = calcular_logaritmos(numeros)
    print(logaritmos)

if __name__ == "__main__":
    main()
