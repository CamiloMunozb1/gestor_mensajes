import sqlite3
import random

def mensajes_aleatorio():
    with sqlite3.connect("C:/Users/POWER/nuevos_mensajes.db") as mensaje_aleatorio:
        consulta_cursor = mensaje_aleatorio.cursor()
        consulta_cursor.execute("SELECT MensajeID,Mensaje FROM mensajes_nuevos")
        mensaje_nuevo=consulta_cursor.fetchall()
        if mensaje_nuevo:
            contenido_mensaje = mensaje_nuevo[0][1]
        consulta_cursor.execute("INSERT INTO mensajes_listos (Mensaje_predeterminado) VALUES(?)",(contenido_mensaje,))
        mensaje_aleatorio.commit()
        consulta_cursor.execute("SELECT mensaje_predeterminado FROM mensajes_listos WHERE mensaje_predeterminado IS NOT NULL")
        fila = consulta_cursor.fetchall()
        if fila:
            random_index = random.randrange(0,len(fila))
            print(fila[random_index][0])
        