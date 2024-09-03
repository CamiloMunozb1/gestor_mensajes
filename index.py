from funciones_basicas.mensajes_predeterminados import mensajes_aleatorio
from funciones_basicas.mensajes_nuevos import nuevo_mensaje
from funciones_basicas.mostrar_mensajes import mensajes_completos


while True:
    try:
        print(
        """
        Bienvenido al gestor de mensajes:
        1. Generar un nuevo mensaje.
        2. Ingresar un nuevo mensaje.
        3. Ver todos los mensajes.
        4. Salir.
        """)
        usuario = int(input("Ingrese una opcion: "))
        if usuario == 1:
            mensajes_aleatorio()
        elif usuario == 2:
            nuevo_mensaje()
        elif usuario == 3:
            mensajes_completos()
        elif usuario == 4: 
            print("Muchas gracias por usar el gestor de mensajes, hasta pronto.")
            break
    except ValueError:
        print("Error de digitacion, intenta nuevamente.")
