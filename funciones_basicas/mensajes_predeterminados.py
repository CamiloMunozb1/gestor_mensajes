
# IMPORTAR LIBRERIAS "SQLITE3" PARA EL MANEJO DE LA BASE DE DATOS Y "RANDOM" PARA ELEGIR MENSAJES ALEATORIOS

import sqlite3
import random

# FUNCION PARA AÑADIRLA A LA BASE DE DATOS

def mensajes_aleatorio():
    try:

        # CONEXION A LA BASE DE DATOS

        with sqlite3.connect("C:/Users/POWER/nuevos_mensajes.db") as mensaje_aleatorio:

            # CURSOR PARA MANEJAR LA BASE DE DATOI

            consulta_cursor = mensaje_aleatorio.cursor()

            # CONSULTA SQL QUE SELECCIONA EL ID DEL MENSAJE Y LOS MENSAJES DE LA TABLA "mensajes_nuevos"

            consulta_cursor.execute("SELECT MensajeID,Mensaje FROM mensajes_nuevos")

            # USO DE "FETCHALL" PARA SELECCIONAR LOS MENSAJES

            mensaje_nuevo=consulta_cursor.fetchall()
            if mensaje_nuevo:

                # SELECCION DE MENSAJES UNO POR UNO 

                contenido_mensaje = mensaje_nuevo[0][1]

            # CONSULTA SQL QUE SUBE LOS CAMBIOS DE LA TABLA ANTERIOR Y LOS JUNTA CON LA DE MENSAJES PREDETERMINADOS

            consulta_cursor.execute("INSERT INTO mensajes_listos (Mensaje_predeterminado) VALUES(?)",(contenido_mensaje,))

            # SE SUBEN LOS CAMBIOS

            mensaje_aleatorio.commit()

            # CONSULTA QUE SELECCIONAR LOS MENSAJES

            consulta_cursor.execute("SELECT mensaje_predeterminado FROM mensajes_listos WHERE mensaje_predeterminado IS NOT NULL")

            # SE SELESCCIONA CON "FETCHALL" LOS MENSAJES

            fila = consulta_cursor.fetchall()
            if fila:

                # CON "RANDOM" SE SELESCCIONAN LOS MENSAJES DESDE 0 HASTA LOS MENSAJES QUE EXISTAN

                random_index = random.randrange(0,len(fila))

                # SE IMPRIME LOS MENSAJES ALEATORIAMENTE DESDE 0

                print(fila[random_index][0])
    
    # MANEJO DE ERRORES
    
    except sqlite3.Error as error:
        print(f"Error en la base {error}")
        