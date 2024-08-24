from funciones_basicas.mensajes_predeterminados import generar_mensaje


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
            generar_mensaje()
        elif usuario == 2:
            print("Proxima funcion")
        elif usuario == 3:
            print("Proxima funcion")
        elif usuario == 4: 
            print("Muchas gracias por usar el gestor de mensajes, hasta pronto.")
            break
    except ValueError:
        print("Error de digitacion, intenta nuevamente.")
