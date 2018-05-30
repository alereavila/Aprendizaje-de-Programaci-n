i=1
while i<=10:
	print(i)
	i=i+1
print("El programa terminó")

edad=int(input("Ingresa tu edad"))
while edad<=0 or edad>100:
	print("Has introducido mal tu edad")
	edad=int(input("Ingresa tu edad"))
print("Puedes pasar")
print("La edad de usted es "+str(edad))