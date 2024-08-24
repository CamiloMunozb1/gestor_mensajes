import random


def generar_mensaje():
    mensajes = ["Cada línea de código es un paso más cerca de crear algo increíble.","El mejor código es el que no tienes que escribir dos veces.","La programación es un arte, y cada desarrollador es un artista.","La programación es la habilidad de convertir ideas en realidad, una línea de código a la vez",
    "La programación es la habilidad de convertir ideas en realidad, una línea de código a la vez."]
    mensaje_random = mensajes[random.randint(0,4)]
    print(mensaje_random)