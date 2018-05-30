

for i in [1,4,3]:#Bucle determinado
	print("Hola")

#en "i" se almacenan los elementos de la lista
for i in ["hola","adios","buenas tardes","buenas noches"]:
	print(i)

#otros tipos de print
for j in [1,2,4,5,7,9,0]:
	print("alo",end=",")
print()

##se recorre un String
for k in "alereavila@hotmail.com":
	print(k,end="\/")

print()
for k in "alereavila@hotmail.com":
	if k=="@":
		print("el email es correcto",end=" ...")

print()
mi_email=input("Introduce tu direccion de email:	")
print()
checar=False
for k in mi_email:
	if k=="@" and k==".":
		checar=True

if checar:
	print("el email es correcto",end=" ...")
else:
	print("el email no es correcto",end=" ...")

#TIPO RANGO 
print()
for e in range(5):
	print(e,end=" ")