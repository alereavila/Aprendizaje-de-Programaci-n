#puede caer el programa con un 8/0
#se debe hacer una captura o control de excepción
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
#cuando corres el programa te describe el error
	try:
		
		return num1/num2
	
	except ZeroDivisionError:
		print("no se puede dividir entre 0")
		return "Operacion eroonea"
while True:
	try:
		op1=(float(input("Introduce el primer número: ")))
		op2=(float(input("Introduce el segundo número: ")))		
		break;


	except ValueError:
		print("Los valores introducidos no son correctos")

	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")