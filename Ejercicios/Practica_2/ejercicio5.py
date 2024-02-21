# -*- coding: utf-8 -*-
"""
Descripción: Este código imprime una casa con un tejado, ventanas y una puerta
y puedes hacer uso de las funciones para imprimir las alturas de las casas

@autor: Adriel Diego
@date: 21/02/2024

"""

def tejado():
    """ 
    Defino la función para imprimir el tejado""

    """
    print("      *      ")
    print("     ***     ")
    print("    *****    ")
    print("   *******   ")
    print("  *********  ")
    print(" ***********")

def ventanas():
    """ 
    Defino la función para imprimir las ventanas

    """
    print("*************")
    print("** *** *** **")
    print("** *** *** **")
    print("*************")
    print("*************")

def puerta():
    """ 
    Defino la función para imprimir la puerta

    """
    print("*****  ******")
    print("*****  ******")
    print("*****  ******")

def main():
    """
    Defino la función principal

    """
    tejado()
    ventanas()
    ventanas()
    ventanas()
    puerta()

main()
