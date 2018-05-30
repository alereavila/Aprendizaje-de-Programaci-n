valido=False
email=input("Introduce tu email")
for e in range (len(email)):
	if email[e]=="@":
		valido=True

if valido:
	print("Email es correcto ")

else:
	print("Email incorrecto")	