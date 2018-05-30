#TUPLAS 
#NO SE PUEDEN MODIFICAR LAS TUPLAS
mitupla=("Alejandro",5528632681,"masculino",1988)
print(mitupla)
print(mitupla[1])

#se convierte la tupla en lista con el metodo "list(nombre de la tupla)"
milista=list(mitupla)
print(milista)
print(milista [0:2])

#convertir una lista en una tupla con el metodo "tupla(nombre de la lista)"
milista2=["erik",5528905366,"masculino",1991,1991,1991]
print(milista2)
mitupla2=tuple(milista2)
print(mitupla2)

#Buscar elemento en la tupla
print("femenino" in mitupla2)

#cuantos elemntoss de encuentran en la Tupla con el metodo count()
print(mitupla2.count("masculino"))

#averiguar la longitud de la tupla
print(len(mitupla2))

#Tupla unitaria de la siguiente manera 
mitupla3=("ANGLOSAJON",)
print(mitupla3)

#desempaquetado de tupla
mitupla4=("JUAN",13,1,1996)
nombre,dia,mes,anio=mitupla4#asigno toda la tupla a las variables
#comprobar como desempaqueto la tupla en las dif variables
print(nombre)
print(mes)
print(anio)
print(dia)
