s_presidente=int(input("Introduce el salario del Presidente"))
#Python es fuertemente tipado asi que no puede imprimir 
#variables de diferente tipo

print(5+s_presidente)

print("El salario dl Presidente es: "+str(s_presidente))

s_director=int(input("Introduce el salario del director"))
print("El salario dl director es: "+str(s_director))

s_jefe=int(input("Introduce el salario del jefe"))
print("El salario dl jefe es: "+str(s_jefe))

s_administrativo=int(input("Introduce el salario del administrativo"))
print("El salario dl administrativo es: "+str(s_administrativo))

if s_administrativo<s_jefe<s_director<s_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo esta fallando")