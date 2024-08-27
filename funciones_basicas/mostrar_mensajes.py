import sqlite3
import pandas as pd

def mensajes_completos():
    with sqlite3.connect("C:/Users/POWER/nuevos_mensajes.db") as mostrar_mensajes:
        consulta_cursor = mostrar_mensajes.cursor()
        consulta_cursor.execute("SELECT * FROM mensajes_nuevos WHERE Mensaje IS NOT NULL")
        resultado = consulta_cursor.fetchall()
        resultado_df = pd.DataFrame(resultado)
    print(resultado_df)