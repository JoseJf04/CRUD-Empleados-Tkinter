""" Modulo para la creación de tablas de base de datos """

import sqlite3
from tkinter import messagebox
from querys import CREATE_TAB

def crear_tab_empleados():
    # Creacion de la conexion y Base de
    connection = sqlite3.connect("C:/DB_Empleados/dbempleados.db")

    try:
        # Cracion del cursor
        cursor = connection.cursor()

        # Ejecucion de la instruccion para la creacion de la tabla staff
        cursor.execute(CREATE_TAB)

    # Imprimir excepcion en caso de existir
    except sqlite3.Error as e:
        messagebox.showerror("Error",f"""Error al ejecutar la query {e}""")

    finally:
        cursor.close()
        connection.close()

# crear_tab_empleados()