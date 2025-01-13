""" Modulo de definición de las instrucciones sql """

# CREACION DE LA TABLA EMPLEADOS
CREATE_TAB = """CREATE TABLE staff(
ci INTEGER(10) PRIMARY KEY,
name VARCHAR(30),
l_name VARCHAR(30),
gender VARCHAR(9),
age INTEGER(3),
email VARCHAR(40),
direction VARCHAR(80),
post VARCHAR(30),
m_status VARCHAR(10),
salary REAL,
op_status VARCHAR(10)
)"""

# INSERCION DE UN NUEVO REGISTRO EN LA TABLA EMPLEADOS
INSERT_EMP = '''INSERT INTO staff(ci, name, l_name, gender, age, email, direction, post, m_status, salary, op_status) 
VALUES(?,?,?,?,?,?,?,?,?,?,?)'''

# SELECCCION DE TODOS LOS DATOS DE EMPLEADOS POR CEDULA
SELECT_EMP = 'SELECT * FROM staff WHERE ci=?'

# ACTUALIZACION DE TODOS LOS DATOS DE EMPLEADO POR CEDULA
UPDATE_EMP = '''UPDATE staff SET name=?, l_name=?, gender=?, age=?, email=?, direction=?, post=?, m_status=?, salary=?, op_status=?
WHERE ci=?'''

# ELIMINACION DE REGISTROS DE EMPLEADOS POR CEDULA
DELETE_EMP = 'DELETE FROM staff WHERE ci=?'