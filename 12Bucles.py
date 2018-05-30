#Escoger asignatura
print("ASIGNATURAS OPTATIVAS")

print("Informatica gráfica-Pruebas de software-Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()#ponerlo todo en minúsculas

if asignatura in ("Informatica gráfica","Pruebas de software","Usabilidad y accesibilidad"):
	print("Asignatura elegida" + asignatura)

else:
	print("La asignatura escogida no esta contemplada")

