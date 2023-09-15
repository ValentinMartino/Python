diccionario = {
	"nombre" : "valentin",
	"apellido" : "martino",
	"seguidores" : 1000
	
}

#lo recorremos con un for para obtener los datos y las claves
for datos in diccionario.items():
	print(f"key: {datos[0]}")#esto nos muestra la clave
	print(f"valor: {datos[1]}")#esto nos muestra el valor

#lo recorremos con un for para obtener las claves
for key in diccionario:
	print(key)#esto solo nos da la key
