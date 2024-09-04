import sqlite3
import random

def mensajes_aleatorio():
    with sqlite3.connect("C:/Users/POWER/nuevos_mensajes.db") as mensaje_aleatorio:
        consulta_cursor = mensaje_aleatorio.cursor()
        consulta_cursor.execute("SELECT mensaje_predeterminado FROM mensajes_listos")
        fila = consulta_cursor.fetchone()
        if fila:
            print(fila[0])