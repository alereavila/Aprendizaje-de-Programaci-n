#DECLARAR LA LISTA
mi_lista=["maria","marta",8,"alejandro","lupita"]

#agarras del cero hasta el elemento 3
print(mi_lista[0:3])#no llega al elemento 3
print(mi_lista[:3] )#lo mismo que arriba

#AGREGAR ELEMENTO AL FINAL DE LA LISTA
print(mi_lista[:])
mi_lista.append("sandy")#para agregar elementos a la lista 
#IMPRIME TODA LA LISTA
print(mi_lista[:])
#AGREGAR UN ELEMENTO EN UN INDICE DETERMINADO
mi_lista.insert(2,"Ramon silva")#pide el indice donde deseas agregar el elemnto 
print(mi_lista[:])
#AGREGAR UNA LISTA 
mi_lista.extend(["eduardo",2,"felipe","alejandra"])
print(mi_lista[:])

#SABER EL INDICE DE UN ELEMENTO EN ESPECIFICO
#regresa el primer indice que encuentre 
print(mi_lista.index("eduardo"))

#comprobar si se encuentra REGRESA UN FALSE O UN TRUE
print("pepita" in mi_lista)

#ELIMINAR ALGUN ELEMENTO
mi_lista.remove(2)
print(mi_lista[:])

#ELIMINAR EL ULTIMO ELEMNTO DE UNA LISTA
mi_lista.pop()
print(mi_lista[:])

#agregar una lista a otra lista 
mi_lista2=["salamanca","huitzii","araña"]

mi_lista3=mi_lista+mi_lista2
print(mi_lista3[:])

#REPETIDOR CON EL OPERADOR *
REPETICION=mi_lista2*4
print(REPETICION)