# Código generado por ChatGPT

import time

def loading_animation(duration=3, message="Loading"):
    animation = ["|", "/", "-", "\\"]
    # animation = ["", ".", "..", "..."]
    idx = 0
    start_time = time.time()

    while (time.time() - start_time) < duration:
        print(f"\r{message} {animation[idx % len(animation)]}", end="", flush=True)
        idx += 1
        time.sleep(0.1)
    # Es necesario dejar espacio en blanco para limpiar todos los caracteres del mensaje de carga
    print("\r                                  ")


