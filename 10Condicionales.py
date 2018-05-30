#Dar beca
print("PROGRAMA DE BECAS")
dist_escuela=int(input("Introduce la distancia a la escuela en Km "))

num_hermanos=int(input("Introduce cuantos hermanos tienes sin contarte a ti por supuesto "))

salario_familiar=int(input("Introduce el salario familiar bruto "))

if dist_escuela>40 and num_hermanos>2 or salario_familiar<20000:
	print("tienes derecho a beca")

else:
	print("no tienes derecho a beca ")

