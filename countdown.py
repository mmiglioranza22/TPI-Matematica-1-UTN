# Código generado por ChatGPT

import time

def countdown(seconds=10):
    for remaining in range(seconds, 0, -1):
        print(f"\rTiempo restante para pensar (no respondas todavía!): {remaining}  ", end="")
        time.sleep(1)
    # Es necesario dejar espacio en blanco para limpiar todos los caracteres de los mensajes anteriores del conteo
    print("\rSe acabó el tiempo!                                           ") 

