import sqlite3

def nuevo_mensaje():
    try:
        with sqlite3.connect("C:/Users/POWER/nuevos_mensajes.db") as ingresar_mensaje:
            consulta_cursor = ingresar_mensaje.cursor()
            ingreso_mensaje = str(input("Ingresa un nuevo mensaje: "))
            consulta_cursor.execute("INSERT INTO mensajes_nuevos (Mensaje) VALUES (?)",(ingreso_mensaje,))
            ingresar_mensaje.commit()
            print("Mensaje ingresado con exito.")
    except ValueError:
        print("Error de digitacion intentar de nuevo.")
    except sqlite3.Error as error:
        print(f"Error en la base: {error}")