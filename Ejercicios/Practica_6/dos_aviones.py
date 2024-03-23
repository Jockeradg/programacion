# -*- coding: utf-8 -*-
"""
Descripción: Este es un programa que simula dos aviones de papel volando que se choca
con un edificio y explota y otro que aterriza.

@autor: Adriel Diego
@date: 23-03-2024

"""

from fundamentos.dibujo import Dibujo, Imagen, Linea


class avionpapel:
    
        def __init__(self, lienzo:Dibujo, punta_x:int, punta_y:int):
            """
            Constructor de la clase avionpapel.
    
            Args:
                lienzo (Dibujo): Ventana de dibujo.
                punta_x (int): Coordenada x de la punta del avion.
                punta_y (int): Coordenada y de la punta del avion.
    
            Returns:
                None
            """
            lon:float = 30
            anch:float = 30
    
            # Crear una imagen para el avion
            self.linea_1 = Linea(lienzo, punta_x-lon, punta_y-anch//2,punta_x-(lon*3)//4, punta_y, "red")
            self.linea_2 = Linea(lienzo, punta_x-(lon*3)//4, punta_y, punta_x-lon, punta_y+anch//2, "red")
            self.linea_3 = Linea(lienzo, punta_x-lon, punta_y+anch//2, punta_x, punta_y, "red")
            self.linea_4 = Linea(lienzo, punta_x, punta_y, punta_x-lon, punta_y-anch//2, "red")
        
        def mueve(self, delta_x:int, delta_y:int):
            """
            Mueve el avion en la ventana de dibujo.
    
            Args:
                delta_x (int): Cantidad de pixeles a mover en el eje x.
                delta_y (int): Cantidad de pixeles a mover en el eje y.
    
            Returns:
                None
            """
            self.linea_1.mueve(delta_x, delta_y)
            self.linea_2.mueve(delta_x, delta_y)
            self.linea_3.mueve(delta_x, delta_y)
            self.linea_4.mueve(delta_x, delta_y)
def main():
    """
    Función principal que ejecuta la simulación de un avion volando y luego 
    chocando.

    La función crea una ventana de dibujo y muestra una imagen de un edificio y
    dos aviones.
    Luego, mueve el avion hacia arriba y hacia la derecha para simular un vuelo 
    y un choque.
    Finalmente, muestra una imagen de explosión y espera a que el usuario 
    cierre la ventana.

    Args:
        None

    Returns:
        None
    """
    
    # Crear la ventana
    lienzo = Dibujo("Título", 900, 800)
    
    # Crear una imagen para el edificio
    edificio = Imagen(lienzo, 700, 500, "edificio.png")
    
    
    # Creamos los dos objetos
    avion1: avionpapel = avionpapel(lienzo, 500, 700)
    avion2: avionpapel = avionpapel(lienzo, 400, 700)

    # Mover el avion hacia arriba
    for _ in range(200):
        avion1.mueve(0, -2)
        avion2.mueve(0, -2.8)
        lienzo.pinta()
    
    # Mover el avion hacia la derecha y simular un choque
    for _ in range(50):
        avion1.mueve(2, 0)
        avion2.mueve(6.5, 0)
        lienzo.pinta()
    
    # Simular una explosión
    explosion = Imagen(lienzo, 600, 300, "boom.png")
    
    # Esperar a que se cierre la ventana y destruirla
    lienzo.espera()
    lienzo.destruye()

if __name__ == "__main__":
    main()