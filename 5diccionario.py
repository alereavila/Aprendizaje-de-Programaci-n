#DICCIONARIO
#{clave:significado ,}

midiccionario={"Alemania":"Berlin", "Francia":"Paris","españa":"Madrid",23:"jordan","mosqueteros":3}
print(midiccionario["Alemania"])

#Imprimir todo el diccionario
print(midiccionario)


#Agregar al diccionario y ASIGNAR otro valor
midiccionario["Italia"]="Roma"

#Imprimir todo el diccionario
print(midiccionario)


#Eliminar un elemento
del midiccionario["Francia"]
print(midiccionario)

#de una tupla haces un diccionario
mitupla=("cesar","areli","alejandro","ricardo")
midiccionario2={mitupla[0]:26,mitupla[1]:24,mitupla[2]:29,mitupla[3]:28}
print(midiccionario2)

#dentro de un diccionario que haya una tupla
mitupla2=("sonics","utha","finics","chicago")
midiccionario3={23:"jordan","nombre":"Michael","Equipo":mitupla2}
print(midiccionario3)
#otra forma de meter una tupla en un diccionario 
midiccionario4={100:"bofo","nombre":"Adolfo","Equipo":("tecos","morelia","pachuca","chivas")}
print(midiccionario4)

#DENTRO de un diccionario otro diccionario
midiccionario_salarios={"mexico":80,"estados unidos":100,"alemania":112}
midiccionario5={23:"jordan","nombre":"Michael","Equipo":midiccionario_salarios}
print(midiccionario5)
midiccionario6={100:"bofo","nombre":"Adolfo","Equipo":{"tecos":22,"morelia":11,"pachuca":9,"chivas":100}}
print(midiccionario6)

#metodos
print(midiccionario_salarios.keys())#claves

print(midiccionario_salarios.values())#valores

print(len(midiccionario_salarios))#la cantidad de claves con valor que existen en el diccionario

print(midiccionario_salarios)#completo