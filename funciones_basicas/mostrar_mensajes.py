
# LIBRERIA "SQLITE3" PARA MANEJAR LA BASE DE DATOS

import sqlite3

# FUNCION PARA AÑADIRLA AL INDEX

def mensajes_completos():
    try:

        # CONEXION A LA BASE SQL

        with sqlite3.connect("C:/Users/POWER/nuevos_mensajes.db") as mostrar_mensajes:

            # CURSOR PARA MANEJAR LA BASE DE DATOS

            consulta_cursor = mostrar_mensajes.cursor()

            # CONSULTA QUE PERMITE MOSTRAR LOS MENSAJES DE LA BASE DE DATOS

            consulta_cursor.execute("SELECT mensaje_predeterminado FROM mensajes_listos")

            # ITERAR SOBRE LOS MENSAJES

            for fila in consulta_cursor:

                # IMPRIME LOS MENSAJES UNO POR UNO 
                print(fila[0])

    # MANEJO DE ERRORES
    
    except sqlite3.Error as error:
        print(f"Error en la base:{error}")