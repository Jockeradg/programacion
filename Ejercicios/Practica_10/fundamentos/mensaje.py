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
mensaje.py: Módulo con una clase que permite mostrar un mensaje
            en una ventana
-----------------------------------------------------------------------

--------------------
-- Ejemplo de uso --
--------------------

from fundamentos.mensaje import Mensaje

def main():
    msg = Mensaje("Prueba de mensaje", "Esto es un mensaje")
    msg.espera()
    msg.destruye()

"""

from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import E
from tkinter import SUNKEN

import time


class Mensaje():
    """
    Esta clase representa una ventana en la que se muestra un mensaje
    de texto
    """

    def __init__(self, titulo: str, texto: str):
        """
        Crea la ventana

        Args:
            titulo: El título de la ventana
            texto: el texto a mostrar en la ventana
        """
        self.__raiz = Tk()
        self.__raiz.transient()
        self.__raiz.title(titulo)
        self.__raiz.resizable(False, False)

        self.__marco = Frame(self.__raiz, borderwidth=2,
                             relief="raised")
        self.__etiqueta = Label(self.__marco, text=texto)
        self.__separador = Frame(self.__marco, height=2, bd=1, relief=SUNKEN)
        self.__boton_ok = Button(self.__marco, text="OK",
                                 command=self._on_ok)

        self.__marco.grid(column=0, row=0, padx=5, pady=5)

        self._colocar_widgets()

        self.__finalize: bool = False
        self.__terminate: bool = False
        self.__raiz.protocol("WM_DELETE_WINDOW", self._on_closing)
        # Bring the window on top
        self.__raiz.wm_attributes("-topmost", True)
        self.__raiz.update()
        self.__raiz.wm_attributes("-topmost", False)

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
        self.__raiz.quit()
        self.__raiz.destroy()

    def _colocar_widgets(self):
        self.__etiqueta.grid(column=0, row=0, sticky=E,
                             padx=15, pady=5)
        self.__separador.grid(column=0, row=1,
                              columnspan=2, padx=5, pady=2)
        self.__boton_ok.grid(column=0, row=2,
                             columnspan=2, padx=5, pady=5)

    def espera(self) -> bool:
        """
        Pinta la ventana y espera hasta que se pulsa OK

        Returns:
            True si se ha matado la ventana, False si se ha pulsado OK
        """
        self.__raiz.update()
        while not self.__finalize:
            self.__raiz.update()
            time.sleep(0.01)
        self.__finalize = False
        return self.__terminate

    def destruye(self):
        """
        Destruir la ventana
        """
        if not self.__terminate:
            self.__raiz.quit()
            self.__raiz.destroy()
