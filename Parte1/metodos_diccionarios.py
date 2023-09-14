diccionario = {
	"nombre" : "valu",
	"apellido": "martino",
	"Subs" : 300
}

#devuelve las claves
claves = diccionario.keys()
print(claves)

#-----------------------------------------------------------------------------------------------------------------------------------
#devuelve lo que esta en cada llave
claves = diccionario.get("nombre")#esto se utiliza porque al no encontrar la llave no salta error
print(claves)

#----------------------------------------------------------------------------------------------------------------------------------
#eliminando todo del diccionario
#diccionario.clear()
#print(diccionario)


#----------------------------------------------------------------------------------------------------------------------------------
#eliminando un elemento del diccionario
diccionario.pop("nombre")
print(diccionario)

#---------------------------------------------------------------------------------------------------------------------------------
#obtenemos el diccionario iterado
resultado = diccionario.items()
print(resultado)
