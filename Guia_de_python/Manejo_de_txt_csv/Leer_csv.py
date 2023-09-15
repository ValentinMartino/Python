import csv

#este tipo de archivo a diferencia de los .txt es para analisis de datos mas que todo, como planillas de excel
#los datos se van a presentar en forma de lista y se recorren con un for
with open("datos.csv") as archivo:
	reader = csv.reader(archivo)
	for row in reader:
		print(row)
	
#se suele utilizar pandas en vez de cvs para leer este tipo de arhcivos

