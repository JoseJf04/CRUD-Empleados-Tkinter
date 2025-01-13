""" Modulo para la definición de funciones utiles """

from tkinter import messagebox

# Funcion para validar entradas
def validate_entrys(ci, name, l_name, sex, age, email, direction, post, m_status, basic_s, status):

    if (ci == "" or name == "" or l_name == "" or sex == "Seleccionar sexo" or age == "" or email == "" or direction == ""
            or post == "Cargo en la empresa" or m_status == "Estado civil" or basic_s == "" or status=="Estatus operativo"):
        return False
    else:
        return True


#Funcion para validar entrada de ci
def validate_ci(ci):
    if ci == "":
        return False
    else:
        return True


# Funcion para devolver respuestas de confirmacion
def get_response(ask):
    response = messagebox.askyesno("Confimracion", f"{ask}")
    if response:
        return True
    else:
        return False