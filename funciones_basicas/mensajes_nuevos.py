
# SE IMPORTA "SQLITE3" PARA MANEJAR LA BASE DE DATOS

import sqlite3

# SE USA LA FUNCION PARA IMPORTARLA AL INDEX

def nuevo_mensaje():
    try:

        # CONEXION A LA BASE DE DATOS

        with sqlite3.connect("C:/Users/POWER/nuevos_mensajes.db") as ingresar_mensaje:

            # CURSOR PARA EL MANEJO DE LA BASE 
            consulta_cursor = ingresar_mensaje.cursor()

            # INGRESO DE USUARIO PARA UN NUEVO MENSAJE

            ingreso_mensaje = str(input("Ingresa un nuevo mensaje: "))

            # CONSULTA SQL PARA INGRESAR EL MENSAJE NUEVO A LA TABLA "Mensaje"

            consulta_cursor.execute("INSERT INTO mensajes_nuevos (Mensaje) VALUES (?)",(ingreso_mensaje,))

            # SE SUBEN LOS CAMBIOS

            ingresar_mensaje.commit()

            # MESAJE DE EXITO

            print("Mensaje ingresado con exito.")

    # MANEJO DE ERRORES
    
    except ValueError:
        print("Error de digitacion intentar de nuevo.")
    except sqlite3.Error as error:
        print(f"Error en la base: {error}")