# -*- coding: utf-8 -*-
"""
                       Paquete fundamentos
  Conjunto de módulos para hacer entrada/salida sencilla en Python

                       Copyright (C) 2019-2024
                 Universidad de Cantabria, SPAIN
                         Versión 1.4
                         Febrero 2024

 @author: Michael Gonzalez   <mgh@unican.es>

 Licencia: GPL
 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU General Public
 License as published by the Free Software Foundation; either
 version 3 of the License, or (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

-----------------------------------------------------------------------
dibujo.py: Módulo con clases que permiten hacer dibujos sencillos
           en una ventana
-----------------------------------------------------------------------

-----------------------
Sistema de coordenadas:
-----------------------

Las coordenadas se miden en píxeles, siendo el origen de coordenadas la
esquina superior izquierda de la ventana, el sentido positivo horizontal
hacia la derecha y el sentido positivo vertical hacia abajo

 0,0
  |----------> X
  |
  |
  |
  Y

--------------------------------------
Ejemplo de uso para dibujos estáticos:
--------------------------------------

from fundamentos.dibujo import Dibujo
from fundamentos.dibujo import Ovalo
from fundamentos.dibujo import Poligono

def main():

    # Creamos el dibujo
    dib = Dibujo("Prueba de dibujo", 640, 480)

    # Creamos un par de figuras en el dibujo dib
    ball = Ovalo(dib, 0, 0, 25, 25, "red")
    triangulo = Poligono(dib, [150, 300, 200, 320, 240, 380], "blue")

    # Pintamos el dibujo y esperamos a que se cierre la ventana
    dib.espera()

    # Destruimos el dibujo
    dib.destruye()


    # Si queremos hacer algo más con el dibujo hay que comprobar que
    # no se haya matado la ventana. Para ello cambiamos la llamada a espera():
    #
    # terminar: bool = dib.espera()
    # if not terminar:
    #     ...

-----------------------------
Ejemplo de un dibujo animado:
-----------------------------

from fundamentos.dibujo import Dibujo
from fundamentos.dibujo import Ovalo
from fundamentos.dibujo import Poligono

def main():

    # Creamos el dibujo
    dib = Dibujo("Prueba de dibujo", 640, 480)

    # Creamos un par de figuras en el dibujo dib
    ball = Ovalo(dib, 0, 0, 25, 25, "red")
    triangulo = Poligono(dib, [150, 300, 200, 320, 240, 380], "blue")

    finalizar: bool = False
    while not finalizar:
        # Determinar cuánto hay que moverse
        delta_x = ...
        delta_y = ...

        # Mover las figuras
        ball.mueve(delta_x, delta_y)
        triangulo.mueve(delta_x, delta_y)

        # Redibujar y mirar a ver si se ha matado la ventana
        finalizar = dib.pinta()
    # destruir el dibujo al finalizar del bucle
    dib.destruye()

-----------------
-- Nota de uso --
-----------------
Cuando un programa que usa este módulo tiene un fallo y la ventana no se
destruye correctamente, el terminal de IPython del entorno Spyder redibuja
la ventana anterior cuando se vuelve a ejecutar el programa, apareciendo
ventanas duplicadas. Para recuperarse de esta situación basta reiniciar
el terminal (botón derecho en el terminal, y "Salir")

@author: Michael.
@date:   Feb 2019
"""

from tkinter import Tk
from tkinter import PhotoImage
from tkinter import Button
from tkinter import Canvas

import time


class Dibujo():
    """
    Esta clase representa una ventana con un lienzo de dibujo

    El lienzo de dibujo se usará al crear figuras tales como rectángulos,
    polígonos, etc., usando el resto de las clases de este módulo
    """

    def __init__(self, titulo: str, width: int = 500, height: int = 400):
        """
        Crea la ventana

        Args:
            titulo: El título de la ventana
            width: Anchura de la ventana en píxeles. Valor por defecto, 500
            height: Altura de la ventana en píxeles. Valor por defecto, 400
        """
        self._tk = Tk()
        self._tk.title(titulo)
        self._tk.resizable(False, False)
        self._tk.wm_attributes("-topmost", 1)

        self.__canvas = Canvas(self._tk, width=width, height=height, bd=0,
                               highlightthickness=0)
        self.__canvas.pack()

        self.__button = Button(self._tk, text="OK", command=self._on_ok)
        self.__button.configure(width=10, activebackground="#33B5E5")
        self.__button_window = self.__canvas.create_window(
            width//2, height-15, window=self.__button)
        # anchor = N

        self.__finalize: bool = False
        self.__terminate: bool = False
        self._tk.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _on_ok(self):
        """
        Anotar que la ventana debe cerrarse
        """
        self.__finalize = True

    def _on_closing(self):
        """
        Destruir la ventana y salir de la aplicación
        """
        self.__finalize = True
        self.__terminate = True
        self._tk.quit()
        self._tk.destroy()

    def get_canvas(self):
        """
        Obtener el lienzo interno de dibujo
        """
        return self.__canvas

    def pinta(self) -> bool:
        """
        Pinta el dibujo y espera un poco

        Returns:
            Booleano que indica si se debe destruir la ventana o no
        """
        self._tk.update()
        time.sleep(0.01)
        return self.__finalize

    def espera(self) -> bool:
        """
        Pinta el dibujo y espera hasta que se pulsa OK o se mata la ventana

        Returns:
            True si se ha matado la ventana, False si se ha pulsado OK
        """
        self._tk.update()
        while not self.__finalize:
            self._tk.update()
            time.sleep(0.01)
        self.__finalize = False
        return self.__terminate

    def destruye(self):
        """
        Destruir la ventana
        """
        if not self.__terminate:
            self._tk.quit()
            self._tk.destroy()


class Figura:
    """
    Clase abstracta que define una figura genérica. No usar directamente
    """

    def __init__(self, dib):
        """
        Crea la figura
        """
        self._canvas = dib.get_canvas()
        self._id = None

    def mueve(self, delta_x: int, delta_y: int):
        """
        Mueve la figura en sentido horizontal y vertical

        Args:
            delta_x: Píxeles a mover en sentido horizontal
            delta_y: Píxeles a mover en sentido vertical
        """
        self._canvas.move(self._id, delta_x, delta_y)

    def get_canvas(self):
        """
        Obtener el lienzo interno de dibujo
        """
        return self._canvas

    def borra(self):
        """
        Borra la figura del dibujo
        """
        self._canvas.delete(self._id)
        self._id = None

    def coloca(self, c_x: int, c_y: int):
        """
        Coloca la figura en las coordenadas indicadas

        Args:
            c_x: Coordenada x donde se coloca el centro de la figura
            c_y: Coordenada y donde se coloca el centro de la figura
         """
        coords: tuple[int, int, int, int] = self._canvas.bbox(self._id)
        center_x: int = (coords[0]+coords[2])//2
        center_y: int = (coords[1]+coords[3])//2
        self._canvas.move(self._id, c_x-center_x, c_y-center_y)


class Linea(Figura):
    """
    Define una línea para dibujar en un objeto de la clase Dibujo
    """

    def __init__(self, dib: Dibujo, x1: int, y1: int, x2: int, y2: int,
                 color: str):
        """
        Crea la línea entre (x1, y1) y (x2, y2)

        Args:
            dib: El objeto de la clase Dibujo que representa la ventana
            x1: Coordenada x del punto 1
            y1: Coordenada y del punto 1
            x2: Coordenada x del punto 2
            y1: Coordenada y del punto 2
            color: El color de la línea. Ejemplo "red", "dark green"
        """
        super().__init__(dib)
        self._id = self.get_canvas().create_line(
            x1, y1, x2, y2, fill=color)


class Ovalo(Figura):
    """
    Define un ovalo para dibujar en un objeto de la clase Dibujo
    """

    def __init__(self, dib: Dibujo, xmin: int, ymin: int, xmax: int,
                 ymax: int, color: str):
        """
        Crea el ovalo inscrito en el rectángulo de esquinas en
        (xmin, ymin) y (xmax, ymax)

        Args:
            dib: El objeto de la clase Dibujo que representa la ventana
            xmin: Coordenada x de la esquina superior izquierda del rectángulo
            ymin: Coordenada y de la esquina superior izquierda del rectángulo
            xmax: Coordenada x de la esquina inferior derecha del rectángulo
            ymax: Coordenada y de la esquina inferior derecha del rectángulo
            color: El color de la línea. Ejemplo "red", "dark green"
        """
        super().__init__(dib)
        self._id = self.get_canvas().create_oval(
            xmin, ymin, xmax, ymax, fill=color)


class Rectangulo(Figura):
    """
    Define un rectángulo para dibujar en un objeto de la clase Dibujo
    """

    def __init__(self, dib: Dibujo, xmin: int, ymin: int, xmax: int, ymax: int,
                 color: str):
        """
        Crea el rectángulo de esquinas situadas en (xmin, ymin) y (xmax, ymax)

        Args:
            dib: El objeto de la clase Dibujo que representa la ventana
            xmin: Coordenada x de la esquina superior izquierda del rectángulo
            ymin: Coordenada y de la esquina superior izquierda del rectángulo
            xmax: Coordenada x de la esquina inferior derecha del rectángulo
            ymax: Coordenada y de la esquina inferior derecha del rectángulo
            color: El color de la línea. Ejemplo "red", "dark green"
        """
        super().__init__(dib)
        self._id = self.get_canvas().create_rectangle(
            xmin, ymin, xmax, ymax, fill=color)


class Poligono(Figura):
    """
    Define un polígono para dibujar en un objeto de la clase Dibujo
    """

    def __init__(self, dib: Dibujo, puntos: list[int], color: str = "black",
                 abierto: bool = False):
        """
        Crea el poligono abierto o cerrado. Las coordenadas del polígono
        se definen en una lista que alterna las coordenadas x,y, de la forma
        [x1, y1, x2, y2, x3, y3, ...]

        Args:
            dib: El objeto de la clase Dibujo que representa la ventana
            puntos: una lista de puntos con las coordenadas del polígono
            color: El color del polígono. Ejemplo "red", "dark green"
            abierto: Determina si el polígono es abierto o cerrado
        """
        super().__init__(dib)
        if abierto:
            self._id = self.get_canvas().create_line(
                puntos, fill=color)
        else:
            self._id = self.get_canvas().create_polygon(
                puntos, outline="black", fill=color)


class Imagen(Figura):
    """
    Define una imagen obtenida a partir de un archivo .gif, o .png
    (no .jpg) para dibujar en un objeto de la clase Dibujo
    """

    def __init__(self, dib: Dibujo, pos_x: int, pos_y: int,
                 nombre_fichero: str):
        """
        Crea la imagen en la posición indicada

        Args:
            dib: El objeto de la clase Dibujo que representa la ventana
            pos_x: Coordenada x del centro de la imagen
            pos_y: Coordenada y del centro de la imagen
            nombre_fichero: El nombre del fichero, incluyendo la extensión
        """
        super().__init__(dib)
        my_im = PhotoImage(file=nombre_fichero, master=dib.get_canvas())
        self._image = my_im
        self._id = self.get_canvas().create_image(
            pos_x, pos_y, image=my_im)


class Texto(Figura):
    """
    Define un texto para representar en un objeto de la clase Dibujo
    """

    def __init__(self, dib: Dibujo, pos_x: int, pos_y: int, texto: str,
                 color: str, size: int = 14):
        """
        Crea el texto situado en la posición indicada

        Args:
            dib: El objeto de la clase Dibujo que representa la ventana
            pos_x: Coordenada x del centro del texto
            pos_y: Coordenada y del centro del texto
            texto: El texto a representar
            color: El color de la línea. Ejemplo "red", "dark green"
            size: El tamaño de la letra
        """
        super().__init__(dib)
        self._id = self.get_canvas().create_text(
            pos_x, pos_y, text=texto, font=("Arial", str(size)), fill=color)
