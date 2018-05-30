import math 


print("Ingrese un numero para obtener su raíz cudrada ")
numero=int(input("Ingrese el número"))
intentos=0

while numero<0:
	print("No se permiten número negativos")

	if intentos>=2:
		print("Has consumido los intentos posibles")
		break;

	numero=int(input("Ingrese el número"))
	intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)
	print(f"La solucion es {solucion}")