#gerara pares
def generaParesfun(limite):
	
	num=1
	
	milista=[]

	while num<limite:
		milista.append(num*2)

		num=num+1

	return milista

print( generaParesfun(20))	


#utilizando generadores
def generaParesgen(limite2):
	num2=1

	while num2<limite2:

		yield num2*2

		num2=num2+1

devuelvepares=generaParesgen(20)

for i in devuelvepares:
	print(i)
