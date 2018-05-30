#continue, pass y else
#continue salta a la siguiente iteración de bucle
#pass devuelve null cuando lee la instrucción, definir clases
#else funciona igual que con el if 

for a in "ALEJANDRO":
	
	if a=="J":
		continue#para saltarse a la proxima iteración
	print(a,end="  ")	
print()
nombre="kjdkal lkjldakj lhjadid lkjdkldsa jda "
contador=0
print(len(nombre))
for e in nombre:
	if e==" ":
		continue

	contador+=1
print(contador)

email=input("Introduce tu email")

for e in email:
	if e=="@":
		arroba = True

		break;
#forma parte del for cuando ya no quede quede que reocrrer 
else:
	arroba=False

print(arroba)