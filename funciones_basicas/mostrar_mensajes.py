import sqlite3

def mensajes_completos():
    with sqlite3.connect("C:/Users/POWER/nuevos_mensajes.db") as mostrar_mensajes:
        consulta_cursor = mostrar_mensajes.cursor()
        consulta_cursor.execute("SELECT mensaje_predeterminado FROM mensajes_listos")
        for fila in consulta_cursor:
            print(fila[0])