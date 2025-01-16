"""Ventana para la gestion de personal"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import widgets as wgt
import db_module
import querys
import utils

class ManagementWindow:
    def __init__(self, root):
        # Creacion de la ventana
        self.wn = root
        self.wn.title("Gestion de Personal")
        self.wn.geometry("600x600")

        #   Label de descripción de la ventana de gestion
        self.label_description = tk.Label(self.wn, text="Gestion de empleados", font=("Arial","14"), fg="Green")
        self.label_description.pack(pady=14)

        #   Frame principal de la ventana para los elementos de entrada de datos
        self.frame_app = ttk.Frame(self.wn, padding=10)
        self.frame_app.pack(fill=tk.BOTH, expand=True)

        #   Frame para los botones de la aplicacion
        self.frameBtn = ttk.Frame(self.wn, padding=10)
        self.frameBtn.pack(fill=tk.BOTH, expand=True)

        #   Label y Entry para el ingreso de la cedula del nuevo empleado
        self.label_ci = wgt.BasicLabel(self.frame_app, r=0, col=0, txt="Cedula idt", fnt=("Arial", "12"), fclr="Green")
        self.text_ci = wgt.IntEntry(self.frame_app, r=0, col=1)

        #   Label y Entry para el ingreso de nombre del empleado
        self.label_name = wgt.BasicLabel(self.frame_app, r=1, col=0, txt="Nombres", fnt=("Arial","12"), fclr="Blue")
        self.text_name = wgt.BasicEntry(self.frame_app, r=1, col=1)

        #   Label y Entry para apellido del empleado
        self.label_lastname = wgt.BasicLabel(self.frame_app, r=2, col=0, txt="Apellidos", fnt=("Arial","12"), fclr="Orange")
        self.text_lastname = wgt.BasicEntry(self.frame_app, r=2, col=1)

        #   Combo de seleccion de sexo
        self.combo_gender = wgt.ImmComboBox(self.frame_app, r=3, col=1, vals=["Seleccionar sexo", "Masculino","Femenino"])

        #   Label y Entey para la edad del empleado
        self.label_age = wgt.BasicLabel(self.frame_app, r=4, col=0, txt="Edad", fnt=("Arial","12"), fclr="Purple")
        self.text_age = wgt.IntEntry(self.frame_app, r=4, col=1)

        #   Label y Entry para el ingreso de email
        self.label_email = wgt.BasicLabel(self.frame_app, r=5, col=0, txt="Correo", fnt=("Arial","12"), fclr="Indigo")
        self.text_email = wgt.BasicEntry(self.frame_app, r=5, col=1, wdth=50)
        self.text_email.establish_columnspan(6)
        self.text_email.establish_padd(x=20)

        #   Label y Entry para el ingreso de Direccion de domicilio
        self.label_direction = wgt.BasicLabel(self.frame_app, r=6, col=0, txt="Direccion", fnt=("Arial", "12"), fclr="Red")
        self.text_direction = wgt.BasicEntry(self.frame_app, r=6, col=1, wdth=65)
        self.text_direction.establish_columnspan(10)
        self.text_direction.establish_padd(x=20)

        #   Combo para la seleccion de puesto de trabajo
        self.combo_workstation = wgt.ImmComboBox(self.frame_app, r=7, col=1, vals=["Cargo en la empresa", "Director","Coordinador","Analista"])

        #   Combo para la seleccion del estado civil
        self.combo_marital_status = wgt.ImmComboBox(self.frame_app, r=8, col=1, vals=["Estado civil", "Soltero(@)", "Casado(@)"])

        #   Label y Entry para el ingreso de salario del empleado
        self.label_salary = wgt.BasicLabel(self.frame_app, r=9, col=0, txt="Sueldo B", fnt=("Arial", "12"), fclr="Teal")
        self.text_salary = wgt.NumericEntry(self.frame_app, r=9, col=1)

        #   Combo para la seleccion del estatus operativo
        self.combo_status = wgt.ImmComboBox(self.frame_app, r=10, col=1, vals=["Estatus operativo", "Activo", "Inactivo"])

        # Botones para las acciones de registro, consulta, actualización y eliminación de empleados
        self.Btn_regisrar = wgt.BasicBtn(self.frameBtn, r=0, col=0, txt="Registrar", comm=self.register_empl, clr="Blue", fclr="White")
        self.Btn_regisrar.establish_size(wdth=18)

        self.Btn_consultar = wgt.BasicBtn(self.frameBtn, r=0, col=1, txt="Consultar", comm=self.consult_empl, clr="Green", fclr="White")
        self.Btn_consultar.establish_size(wdth=18)

        self.Btn_actualizar = wgt.BasicBtn(self.frameBtn, r=0, col=2, txt="Actualizar", comm=self.update_empl, clr="Orange", fclr="White")
        self.Btn_actualizar.establish_size(wdth=18)

        self.Btn_eliminar = wgt.BasicBtn(self.frameBtn, r=0, col=3, txt="Eliminar", comm=self.delete_empl, clr="Red", fclr="White")
        self.Btn_eliminar.establish_size(wdth=18)


# Metodos de la ventana de gestion

    # Metodo para obtener el valor del entry ci
    def get_ci_entry(self):
        ci = self.text_ci.get()
        return ci


    # Metodo para obtener los valores de los entrys y combobox de la ventana de gestion
    def get_data_entrys(self):
        #   Obtener valores de los entrys
        name = self.text_name.get()
        l_nm = self.text_lastname.get()
        age = self.text_age.get()
        email = self.text_email.get()
        dir = self.text_direction.get()
        basic_s = self.text_salary.get()

        #   Obtener valores de los combobox
        sex = self.combo_gender.get()
        post = self.combo_workstation.get()
        m_status = self.combo_marital_status.get()
        status = self.combo_status.get()

        return name, l_nm, sex, age, email, dir, post, m_status, basic_s, status


    # Metodo para limpiar las entradas de datos, "limpiar entrys" y "Restablecer combos a su valor por defecto"
    def clean_data_entries(self):
        #   Limpiar entrys
        self.text_ci.clear_entry()
        self.text_name.clear_entry()
        self.text_lastname.clear_entry()
        self.text_age.clear_entry()
        self.text_email.clear_entry()
        self.text_direction.clear_entry()
        self.text_salary.clear_entry()

        #   Restablecer combox
        self.combo_gender.restore()
        self.combo_workstation.restore()
        self.combo_status.restore()
        self.combo_marital_status.restore()


    # Metodo para registrar usuarios en la DB
    def register_empl(self):
        ci = self.get_ci_entry()
        values = self.get_data_entrys()

        validated_values = utils.validate_entrys(ci, *values)

        if validated_values:

            datos = db_module.execute_query(querys.SELECT_EMP, (ci,))

            if datos is None or len(datos) == 0:
                db_module.execute_query(querys.INSERT_EMP, (ci, *values))
                self.clean_data_entries()

            else:
                messagebox.showinfo("Duplicacion de registro", f"Ya existe un empleado registrado con la cedula: {ci}")

        else:
            messagebox.showinfo("Datos incompletos","Debe rellenar todos los campos solicitados")


    # Metodo para consultar empleados registrados en la DB
    def consult_empl(self):
        ci = self.get_ci_entry()

        validate_ci = utils.validate_ci(ci)

        if validate_ci:
            datos = db_module.execute_query(querys.SELECT_EMP, (ci,))

            if len(datos) > 0:
                # Setear datos otenidos en sus respectivos entrys
                self.text_name.insert_value(datos[0][1])
                self.text_lastname.insert_value(datos[0][2])
                self.text_age.insert_value(datos[0][4])
                self.text_email.insert_value(datos[0][5])
                self.text_direction.insert_value(datos[0][6])
                self.text_salary.insert_value(datos[0][9])

                # Setear datos obtenidos en sus respectivos combobox
                self.combo_gender.set_value(datos[0][3])
                self.combo_workstation.set_value(datos[0][7])
                self.combo_marital_status.set_value(datos[0][8])
                self.combo_status.set_value(datos[0][10])

            else:
                messagebox.showinfo("Registro no encontrado", f"El numero de cedula: {ci} no esta registrado")

        else:
            messagebox.showinfo("Datos incompletos","Debe rellenar el campo ci")


    # Metodo para actualizar la información de un empleado en la DB
    def update_empl(self):
        ci = self.get_ci_entry()
        values = self.get_data_entrys()

        validate_values = utils.validate_entrys(ci, *values)

        if validate_values:

            datos = db_module.execute_query(querys.SELECT_EMP, (ci,))

            if len(datos) > 0:
                db_module.execute_query(querys.UPDATE_EMP, (*values,ci))
                self.clean_data_entries()

            else:

                messagebox.showinfo("Registro no encontrado",f"El numero de cedula: {ci} no esta registrado")

        else:
            messagebox.showinfo("Datos incompletos","Debe rellenar todos los campos solicitados")

    # Metodo para eliminar empleado la DB
    def delete_empl(self):
        ci = self.get_ci_entry()

        validate_ci = utils.validate_ci(ci)

        if validate_ci:
            datos = db_module.execute_query(querys.SELECT_EMP, (ci,))

            if len(datos) > 0:
                confirmation = utils.get_response(f"Esta seguro de que desea eliminar los registros del usuario con la CI: {ci} ?")

                if confirmation:
                    db_module.execute_query(querys.DELETE_EMP, (ci,))
                    self.clean_data_entries()

                else:
                    messagebox.showinfo("Cancelado", "La operacion de eliminacion ha sido cancelada")

            else:
                messagebox.showinfo("Registro no encontrado",f"El numero de cedula: {ci} no esta registrado")

        else:
            messagebox.showinfo("Datos incompletos", "Debe rellenar el campo ci con la cedula del empleado a eliminar")

#   Creacion del root
root = tk.Tk()
#   Creacion de la ventana de gestion
app = ManagementWindow(root)
#   Mantener la venata en ejecucion
root.mainloop()
