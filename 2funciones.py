def suma():
	num1=5
	num2=7
	print(num1+num2)

suma()

def sumarecibe(num3,num4):#pasa valores por referencia
	print(num3+num4)

sumarecibe(8,9)
sumarecibe(88,105)

def sumarecibeydevuelve(num5,num6):#pasa valores por referencia
	return num5+num6

print(sumarecibeydevuelve(8,17.6))#pasa valores por referencia
