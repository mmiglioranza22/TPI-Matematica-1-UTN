# App adivinanzas en binario:

# La aplicación simula un juego de adivinanzas de números binarios.

# Se muestra por consola un número binario y se solicita al usuario que adivine su equivalente en decimal. El usuario debe ingresar su nombre para la tabla de puntaje.

# Si lo logra, suma puntos y se pasa una nueva adivinanza. Si no, puede volver a intentarlo hasta un máximo 3 intentos, y si no lo logra se pasa a una nueva adivinanza.

# El juego consiste en lograr la mayor cantidad de aciertos, de un total de 5 turnos. Cada acierto suma 20 puntos.

# Finalizado los 5 turnos, se muestra en consola el puntaje del usuario y se pregunta si quiere jugar nuevamente. 
# Aquí si el usuario ingresa su mismo nombre, el puntaje anterior sobrescribirá con el nuevo, o bien si ingresa otro nombre se generará un nuevo
# registro en la tabla de puntaje.

from loading_animation import loading_animation
import time
import random

# Carga de variables
total_turnos = 5
turno_actual = 1
listado_números = list(range(0,101))


# Primer etapa: Inicio y registro de usuario

print("------- Adivina el número binario -------")

jugador = input("Ingrese el nombre del jugador: ")

while jugador.strip() == "":
	jugador = input("No entendí, por favor ingrese el nombre del jugador: ")

# Segunda etapa: Ciclo de juego (5 turnos)

while turno_actual < total_turnos:

	print(f"Hola {jugador}! ¿Estás preparado para ejercitar tu cerebro?")
	time.sleep(2)

	print("Voy a pensar un número del 1 al 100 EN BINARIO! Y tenés que adivinarlo!")
	time.sleep(3)

	print("Preparado, listo... YA!")
	loading_animation(3, "Lo estoy pensando")

adivinanza = listado_números[random.randint(0,100)]

print(f"{adivinanza}")














