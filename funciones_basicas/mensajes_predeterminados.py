import sqlite3
import pandas as pd

def mensajes_aleatorio():
    with sqlite3.connect("C:/Users/POWER/nuevos_mensajes.db") as mensaje_aleatorio:
        consulta_cursor = mensaje_aleatorio.cursor()
        consulta_cursor.execute("SELECT mensaje_predeterminado FROM mensajes_listos")
        resultado = consulta_cursor.fetchall()
        resultado_df = pd.DataFrame(resultado)
    print(resultado_df)