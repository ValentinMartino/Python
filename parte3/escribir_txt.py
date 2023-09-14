with open("nota.txt","w",encoding = "UTF-8") as archivo:#le damos permiso de escritura
	#archivo.write("Estoy escribiendo en el archivo")
	archivo.writelines("hola capo como estas\n") #tambien se pueden escribir lineas
	#writelines no borra los datos anteriorres, si no que los va acumulando
	archivo.writelines("todo bien pa\n")
	
