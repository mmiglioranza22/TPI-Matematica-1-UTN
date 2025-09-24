# App adivinanzas en binario:

# La aplicación simula un juego de adivinanzas de números binarios.

# Se muestra por consola un número binario y se solicita al usuario que adivine su equivalente en decimal. El usuario debe ingresar su nombre.

# Si lo logra, suma puntos y se pasa una nueva adivinanza. Si no lo logra, se pasa a una nueva adivinanza.

# El juego consiste en lograr la mayor cantidad de aciertos, de un total de 5 turnos. Cada acierto suma 20 puntos.

# Finalizado los 5 turnos, se muestra en consola el puntaje del usuario y un mensaje asociado al puntaje específico obtenido

import time
import random
from loading_animation import loading_animation
from countdown import countdown

# Carga de variables
total_turnos = 5
turno_actual = 1
listado_números = list(range(0,101))
puntaje = 0

# Primer etapa: Inicio y registro de usuario

print("------- Adivina el número binario -------\n")

jugador = input("Ingrese el nombre del jugador: ").strip()

while jugador.strip() == "":
	jugador = input("No entendí, por favor ingrese el nombre del jugador: ").strip()

# Segunda etapa: Ciclo de juego (5 turnos)

print(f"Hola {jugador}! ¿Estás preparado para ejercitar tu cerebro?")
time.sleep(2)

print("Voy a pensar un número del 1 al 100 EN BINARIO! Y tenés que adivinarlo!")
time.sleep(3)

while turno_actual <= total_turnos:

	print(f"\nAdivinanza #{turno_actual}: Preparado, listo... YA!")
	loading_animation(3, "Lo estoy pensando... ")

	# Se guarda el número que sale cada vez para que no repita en futuros turnos
	indice = random.randint(0,100)

	acierto_decimal = listado_números[indice]
	# Se convierte en número binario y se ignoran los dos primeros numeros (signo).
	acierto_binario = int(bin(listado_números[indice])[2:]) 

	print(f"---	 {acierto_binario}	   ---\n")

	countdown(10)
	
	print("\n")

	try:
		respuesta = int(input("¿Sabés qué número es?: ").strip()) 

		if respuesta == acierto_decimal:
			print(f"Exacto! {acierto_binario} equivale a {respuesta} en decimal")
			puntaje += 20
		else:
			print(f"Ups! El número {acierto_binario} en decimal es el {acierto_decimal}\n")

		# Sacar el numero que salió para no repetirlo
		listado_números.remove(acierto_decimal)
		
		# Avanzar el bucle
		turno_actual += 1
	except Exception as e:
		print("La respuesta indicada no es un número válido. Adivinanza anulada (No sumas puntos)")

print(f"\nSe acabó el juego!")
print(f"\nTu puntaje final es el siguiente: {puntaje}")

if puntaje == 100:
	print("El puntaje más alto posible! Felicitaciones!")
elif puntaje == 80:
	print("Muy bien! Casi sacás todas!")
elif puntaje == 60:
	print("Nada mal! Un poco más de práctica y adivinás todas!")
elif puntaje == 40:
	print("Se puede mejorar, a no aflojar la práctica!")
elif puntaje == 20:
	print("Te agarré distraído. Mejor suerte la próxima")
else:
	print("Cómo te digo esto... hay que estudiar...")

















