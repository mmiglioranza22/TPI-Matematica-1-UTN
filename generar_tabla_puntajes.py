# Código generado por ChatGPT

def generar_tabla_puntajes(jugadores):
    # Asegúrate de que la lista de jugadores tenga 5 elementos
    while len(jugadores) < 5:
        jugadores.append(("---", 0))

    # Ancho fijo de la tabla
    ancho_total = 40

    # Crear bordes y título
    borde_superior = "┌" + "─" * (ancho_total - 2) + "┐"
    borde_inferior = "└" + "─" * (ancho_total - 2) + "┘"
    separador = "├" + "─" * (ancho_total - 2) + "┤"

    # Centrar el título
    titulo = "Tabla de jugadores"
    titulo_centrado = "│" + titulo.center(ancho_total - 2) + "│"

    # Generar filas de puntajes
    filas = []
    for i, (nombre, puntaje) in enumerate(jugadores, 1):
        fila = f"│ {i}. {nombre.ljust(20)} {str(puntaje).rjust(10)} │"
        filas.append(fila)

    # Armar la tabla completa
    tabla = [borde_superior, titulo_centrado, separador] + filas + [borde_inferior]

    # Imprimir la tabla
    for linea in tabla:
        print(linea)

# Ejemplo de uso
# Hacer un sort en las posiciones
jugadores = [
    ("AAA", 15000),
    ("BBB", 12500),
    ("CCC", 10000),
    ("DDD", 7500),
    ("EEE", 5000)
]

generar_tabla_puntajes(jugadores)

# ┌──────────────────────────────────────┐
# │           Tabla de jugadores         │
# ├──────────────────────────────────────┤
# │ 1. AAA                 	      15000  │
# │ 2. BBB                 	      12500  │
# │ 3. CCC                 	      10000  │
# │ 4. DDD                 	       7500  │
# │ 5. EEE                 	       5000  │
# └──────────────────────────────────────┘
