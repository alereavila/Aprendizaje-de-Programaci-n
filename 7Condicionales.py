print("verificacion de edad")

edad_usuario=int(input("Introduce tu edad, por favor  --->"))

if edad_usuario<18:
	print("No puede pasar")
elif edad_usuario>100:
	print("debes de estar muerto")
else :
	print("Puedes pasar")


print("Verificación de calificaciones")

nota_alumno=int(input("Introduce tu calificación, por favor --->"))

if nota_alumno<5:
	print("Insuficiente")

elif nota_alumno<6:
	print("Suficiente")

elif nota_alumno<7:
	print("Bien")

elif nota_alumno<9:
	print("Notable")

else:
	print("Sobresaliente")
