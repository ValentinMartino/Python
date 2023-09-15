#se tiene dos listas
#una con nombres y la otra con apellidos
#hay que escribir de forma optima estas dos listas en un archivo

nombres = ["valentin","milagros","rosana"]
apellidos = ["martino","diaz","baima"]

with open("datos.txt","w",encoding = "UTF-8") as archivo:
	for nom,ape in zip(nombres,apellidos) :
		archivo.write(f"{nom.capitalize()} {ape.capitalize()} \n")
			
