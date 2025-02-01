""" Módulo para la definición de clases de elementos """

import tkinter as tk
from tkinter import ttk
import re

# BasicLabel : Default Label
class BasicLabel(tk.Label):
    def __init__(self, master, r=0, col=0, txt="Label", fnt=("Roboto","12"), fclr="Black"):
        super().__init__(master, text=txt, font=fnt, fg=fclr )

        # Establecer filas y columnas de la etiqueta, y el padding por defecto
        self.grid(row=r, column=col, padx=5, pady=5)

        # Metodo para establer una nueva posicion para la etiqueta
    def establish_position(self, r, col):
        self.grid(row=r, column=col)

        # Metodo para establecer la extencion de columnas de la etiqueta
    def establish_columnspan(self, include):
        self.grid(columnspan=include)

        # Metodo para establecer nuevo padding de la etiqueta
    def establish_padd(self, x=5, y=10):
        self.grid(padx=x, pady=y)


# BasicEntry : Default entry
class BasicEntry(tk.Entry):
    def __init__(self, master, r=0, col=0, wdth=25, fnt=("Arial","12"), **kwargs):
        super().__init__(master, width=wdth, font=fnt, **kwargs)

        # Establecer filas y columnas del entry,  y el padding por defecto
        self.grid(row=r, column=col, padx=5, pady=10)

        # Metodo para establecer nueva posicion del entry
    def establish_position(self, r, col):
        self.grid(row=r, column=col)

        # Metodo para establecer la extencion de columnas del entry
    def establish_columnspan(self, include):
        self.grid(columnspan=include)

        # Metodo para establecer nuevo padding del Entry
    def establish_padd(self, x=5, y=10):
        self.grid(padx=x, pady=y)

        # Metodo para bloquear el entry
    def block_entry(self):
        self.config(state="disabled")

        # Metodo para desbloquear en entry
    def unlock_entry(self):
        self.config(state="normal")

        # Metodo para limpiar el entry
    def clear_entry(self):
        self.delete(0, tk.END)

        # Metodo para insertar nuevo valor en el entry
    def insert_value(self, new_value):
        self.clear_entry()
        self.insert(0, new_value)


# NumericEntry : Entry for numbers
class NumericEntry(BasicEntry):
    def __init__(self, master, r=0, col=0, wdth=25, fnt=("Arial","12"), **kwargs):
        super().__init__(master, r=r, col=col, wdth=wdth, fnt=fnt, **kwargs)

            # Registro de la validacion
        self.validate_command = master.register(self.validate)

            # Configuracion del entry con la validacion de numeros
        self.config(validate="key", validatecommand=(self.validate_command, '%P'))

        # Metodo de validacion para numeros: enteros y decimales
    def validate(self, value):

        decimal_pattern = r'^\d*\.?\d*$'
        if value == "" or re.match(decimal_pattern, value):
            return True
        else:
            return False


# IntEntry : Entry for integer
class IntEntry(NumericEntry):
    def __init__(self, master, r=0, col=0, wdth=25, fnt=("Arial","12"), **kwargs):
        super().__init__(master, r=r, col=col, wdth=wdth, fnt=fnt,**kwargs)

            # Registro de la validacion
        self.validate_command = master.register(self.validate)

            # Configuracion del Entry con la validacion de numeros enteros
        self.config(validate="key", validatecommand=(self.validate_command,'%P'))

        # Creacion del Metodo de validacion : Solo para numeros enteros
    def validate(self, value):
        if value == "" or value.isdigit():
            return True
        else:
            return False


    # BasicComboBox : Basic Combobox
class BasicComboBox(ttk.Combobox):
    def __init__(self, master, r=0, col=0, vals=[""], wdth=23, fnt=("Arial","12"), **kwargs):
        super().__init__(master, values=vals, width=wdth, font=fnt, **kwargs)

        #Obtener los valores pasados al combobox
        self.valores = vals

        # Setear el valor del índice 0 como opción por defecto del combobox
        self.set(self.valores[0])

        # Establecer fila y columna del combobox, y el paddding por defecto
        self.grid(row=r, column=col, padx=5, pady=10)

        # Metodo para establecer una nueva posición del Combo
    def establish_position(self, r, col):
        self.grid(row=r, column=col)

        # Metodo para establecer la extension de columnas del Combo
    def establish_columnspad(self, include):
        self.grid(columnspan=include)

        # Metodo para establecer nuevo padding del Combo
    def establish_padd(self, x, y):
        self.grid(padx=x, pady=y)

        # Metodo para setear un valor
    def set_value(self, value):
        self.set(value)

        # Metodo para restablecer el primer valor como opción a mostrar por defecto
    def restore(self):
        self.set(self.valores[0])


    # ImmComboBox : Immutable Combobox
class ImmComboBox(BasicComboBox):
    def __init__(self, master, r=0, col=0, vals=[""], wdth=23, fnt=("Arial","12"), **kwargs):
        super().__init__(master, r=r, col=col, vals=vals, wdth=wdth, fnt=fnt, **kwargs)

            # Establercer los textos del combo como no editables
        self['state'] = "readonly"


    # BasicBtn : Basic Button
class BasicBtn(tk.Button):
    def __init__(self, master, r=0, col=0, wdth=10, hght=2, comm=None, txt="button", clr="Black", fclr="White",
                 fnt=("Roboto","12"), **kwargs):

        super().__init__(master, width=wdth, height=hght, command=comm, text=txt, bg=clr, fg=fclr, font=fnt, **kwargs)

        # Establecer la fila y columna del boton, y el padding por defecto
        self.grid(row=r, column=col, padx=5, pady=10)

        # Metodo para establecer una nueva posicion del Boton
    def establish_position(self, r, col):
        self.grid(row=r, column=col)

        # Metodo para establercer la extencion columnas del Boton
    def establish_columnspan(self, include):
        self.grid(columnspan=include)

        # Metodo para establercer nuevo padding del Boton
    def establish_padd(self, x=5, y=10):
        self.grid(padx=x, pady=y)

        # Metodo para establecer tamaño "Ancho y Alto"
    def establish_size(self, wdth=10, hght=2):
        self.config(width=wdth, height=hght)