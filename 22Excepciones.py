def divide ():
	try :
		op1=(float(input("Introduce el primer número: ")))
		op2=(float(input("Introduce el segundo número: ")))	

		print ("La división es "+str(op1/op2))
	except ValueError:
		print ("el valor introducido es erroneo")	
	except ZeroDivisionError:
		print("no se puede dividir entre 0")

	print("calculo finalizado")

divide()

def divide2 ():
	try :
		op11=(float(input("Introduce el primer número: ")))
		op22=(float(input("Introduce el segundo número: ")))	

		print ("La división es "+str(op11/op22))
	except ValueError:
		print ("Ha ocurrido un error")	
	

	print("calculo finalizado")

divide2()