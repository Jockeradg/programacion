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
menu.py: Módulo con una clase que permite mostrar un menú con opciones
         en una ventana, y obtener la opción elegida por el usuario
-----------------------------------------------------------------------

--------------------
-- Ejemplo de uso --
--------------------

from fundamentos.menu import Menu

def main():
    menu_opciones = Menu("Elige una opción")
    menu_opciones.inserta_opcion("Editar ficha de cliente")
    ... otras opciones
    menu_opciones.inserta_opcion("Salir")

    terminar: bool = False
    while not terminar:
        resultado: str = menu_opciones.espera()
        ... trabajar con la opción elegida
        terminar = resultado.lower() in ("kill", "salir")

    menu_opciones.destruye()

"""

from tkinter import Tk
from tkinter import Frame
from tkinter import Button
from tkinter import N

import time

from fundamentos.mensaje import Mensaje


class Menu():
    """
    Esta clase representa una ventana con un menú de opciones
    """

    def __init__(self, titulo: str):
        """
        Crea la ventana

        Args:
            titulo: El título de la ventana
        """
        self.__raiz = Tk()
        self.__raiz.title(titulo)
        self.__raiz.resizable(False, False)

        # contenedor para los botones
        self.__botones: list[Button] = []

        self.__marco = Frame(self.__raiz, borderwidth=2,
                             relief="raised")

        self.__marco.grid(column=0, row=0, padx=5, pady=5)

        # self._colocar_widgets()

        self.__finalize: bool = False
        self.__terminate: bool = False
        self.__boton_pulsado: str = ""
        self.__raiz.protocol("WM_DELETE_WINDOW", self._on_closing)
        # Poner la ventana encima de las demás
        self.__raiz.wm_attributes("-topmost", True)
        self.__raiz.update()
        self.__raiz.wm_attributes("-topmost", False)

    def _on_button(self, text: str):
        """
        Anotar que la ventana debe cerrarse
        """
        self.__boton_pulsado = text
        self.__finalize = True

    def _on_closing(self):
        """
        Destruir la ventana y salir de la aplicación
        """
        self.__finalize = True
        self.__terminate = True
        self.__raiz.quit()
        self.__raiz.destroy()

    def _colocar_widgets(self):
        fila: int = 0
        for i in range(len(self.__botones)):
            self.__botones[i].grid(column=0, row=fila, sticky=N,
                                   padx=30, pady=5)
            fila += 1

    def _muestra_error(self, texto: str):
        """
        Muestra un mensaje de error en pantalla

        Args:
            texto: el texto del mensaje de error
        """
        self.__raiz.withdraw()
        msg = Mensaje("Error", texto)
        msg.espera()
        msg.destruye()
        self.__raiz.update()
        self.__raiz.deiconify()

    def inserta_opcion(self, etiqueta: str):
        """
        Crea un botón para una nueva opción en el menú

        Args:
            etiqueta: el texto que se colocará en el botón de la nueva opción
        """

        boton_opcion = Button(self.__marco, text=etiqueta,
                              command=lambda: self._on_button(etiqueta))
        self.__botones.append(boton_opcion)
        self._colocar_widgets()

    def espera(self) -> str:
        """
        Pinta la ventana y espera hasta que se pulsa OK

        Returns:
            el texto "Kill" si se ha matado la ventana,
            o la etiqueta de la opción elegida
        """
        self.__raiz.update()
        while not self.__finalize:
            self.__raiz.update()
            time.sleep(0.01)
        self.__finalize = False
        if self.__terminate:
            return "Kill"
        return self.__boton_pulsado

    def destruye(self):
        """
        Destruir la ventana
        """
        if not self.__terminate:
            self.__raiz.quit()
            self.__raiz.destroy()
