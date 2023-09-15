#primero debemos abrir el archivo
archivo = open("nota.txt",encoding = "UTF-8")# lo de utf8 es para leerlo de esa forma


#despues debemos leer el archivo completo
#texto = archivo.read()
#print(texto)

#leer linea por linea
#lineas = archivo.readlines()
#print(lineas)

#leeruna sola linea
linea = archivo.readline()#dentro del parentesis podemos poner la cantidad de caracteres que queremos que lea de la primer linea
print(linea)

#cerrar el archivo
archivo.close()



