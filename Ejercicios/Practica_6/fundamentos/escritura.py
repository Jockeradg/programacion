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
escritura.py: Módulo con una clase que permite escribir datos
              en una ventana
-----------------------------------------------------------------------

--------------------
-- Ejemplo de uso --
--------------------

from fundamentos.escritura import Escritura

def main():

    # Paso 1: crear el objeto de la clase Escritura
    escr = Escritura("Datos del experimento")

    # Paso 2: crear las entradas para mostrar datos
    escr.inserta_valor("Número de secuencia", 1)
    escr.inserta_valor("Voltaje (V)", 0.0)
    escr.inserta_valor("Nombre del técnico", "Pedro")

    # Paso 3: esperar a que el usuario se dé por enterado
    escr.espera()

    # Paso 4: destruir la ventana
    escr.destruye()

"""

from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import E
from tkinter import SUNKEN
from tkinter import StringVar

import time

from fundamentos.mensaje import Mensaje


class Escritura():
    """
    Esta clase representa una ventana con entradas para escribir datos
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
        self.__raiz.minsize(300, 40)

        # contenedores para las entradas
        self.__etiquetas: list[Label] = []
        self.__entradas: list[Entry] = []
        self.__textos: list[str] = []

        self.__marco = Frame(self.__raiz, borderwidth=2,
                             relief="raised")
        self.__separador = Frame(self.__marco, height=2, bd=1, relief=SUNKEN)
        self.__boton_ok = Button(self.__marco, text="OK",
                                 command=self._on_ok)

        self.__marco.grid(column=0, row=0, padx=5, pady=5)

        self._colocar_widgets()

        self.__finalize: bool = False
        self.__terminate: bool = False
        self.__raiz.protocol("WM_DELETE_WINDOW", self._on_closing)
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
        fila: int = 0
        for i in range(len(self.__textos)):
            self.__etiquetas[i].grid(column=0, row=fila, sticky=E,
                                     padx=5, pady=5)
            self.__entradas[i].grid(column=1, row=fila, padx=5, pady=5)
            fila += 1
        self.__separador.grid(column=0, row=fila,
                              columnspan=2, padx=5, pady=2)
        fila += 1
        self.__boton_ok.grid(column=0, row=fila,
                             columnspan=2, padx=5, pady=5)

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

    def inserta_valor(self, etiqueta: str, valor: str | int | float):
        """
        Crea una entrada en la que se puede teclear texto

        Args:
            etiqueta: texto colocado al lado de la entrada para identificarla
            valor: el valor escrito
        """
        self.__etiquetas.append(Label(self.__marco, text=etiqueta))
        self.__textos.append("")
        entrada = Entry(self.__marco,
                        textvariable=StringVar(value=""),
                        width=30)
        self.__entradas.append(entrada)
        entrada.focus_force()
        entrada.insert(0, str(valor))
        entrada.configure(state="readonly")
        self._colocar_widgets()

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
