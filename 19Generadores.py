#* antes no sabemos cuantos elementos recibira pero los recibira en forma 
#de tupla

def devuelveCiudades(*ciudades):

	for elemento in ciudades:
		for subelemento in elemento:#los dos primeros elementos del elemnto
			yield subelemento
		

ciudades_devueltas=devuelveCiudades("madrid","mexico","bogota","buenos aires")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

#para acceder a los elemntos dentro de la tupla 
def devuelveCiudades(*ciudades):

	for elemento2 in ciudades:
		yield from elemento2
		

ciudades_devueltas2=devuelveCiudades("madrid","mexico","bogota","buenos aires")
print(next(ciudades_devueltas2))
print(next(ciudades_devueltas2))