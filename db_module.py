""" Modolo de gestion para la ejecución de instrucciones sql """

import sqlite3
from tkinter import messagebox

# Funcion para ejecutar instrucciones sql
def execute_query(query, params):

    # Creacion de la conexion a la DB
    connection = sqlite3.connect("Database/dbempleados.db")

    # Try para manejar execepciones
    try:

        # Creacion del cursor
        cursor = connection.cursor()

        # Ejecucion de la instruccion
        cursor.execute(query, params)

        # Verificar si la instruccion ha resultado en Insert, Update o Delete
        if query.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
            connection.commit()  # Realizar commit para guardar cambios


        # Verificar si la instruccion ha resultado en un Select
        if query.strip().upper().startswith(('SELECT')):
            return cursor.fetchall()  # Retornar valores consultados

        messagebox.showinfo("Finalizado", "Operacion realizada")

    # Imprimir excepcion en caso de existir
    except sqlite3.Error as e:
        print(f"""Error al ejecutar la consulta: {e}""")

    # Finalizar y cerrar las conexiones
    finally:
        cursor.close()
        connection.close()