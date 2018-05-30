def evaluacion(nota):
	valoracion="aprobado"
	if nota<=5:
		valoracion="no aprobado"
	return valoracion

print("programa de evaluación")
#todo lo que se introduce es texto
nota_alumno=int(input("Introduce la calificación"))#lo transformo en entero 
print(evaluacion(nota_alumno))