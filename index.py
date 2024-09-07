
# FUNCIONES IMPORTADAS PARA EL INDEX

from funciones_basicas.mensajes_predeterminados import mensajes_aleatorio
from funciones_basicas.mensajes_nuevos import nuevo_mensaje
from funciones_basicas.mostrar_mensajes import mensajes_completos


while True:
    try:

        # MENU DE FUNCIONES PARA EL USUARIO

        print(
        """
        Bienvenido al gestor de mensajes:
        1. Generar un nuevo mensaje.
        2. Ingresar un nuevo mensaje.
        3. Ver todos los mensajes.
        4. Salir.
        """)

        # VARIABLE DE ENTRADA PARA QUE EL USUARIO INTERACTUE CON EL MENU 

        usuario = int(input("Ingrese una opcion: "))
        if usuario == 1:
            mensajes_aleatorio()
        elif usuario == 2:
            nuevo_mensaje()
        elif usuario == 3:
            mensajes_completos()
        elif usuario == 4: 

            # MENSAJE DE SALIDA 

            print("Muchas gracias por usar el gestor de mensajes, hasta pronto.")
            break

    # MANEJO DE ERRORES
    
    except ValueError:
        print("Error de digitacion, intenta nuevamente.")
