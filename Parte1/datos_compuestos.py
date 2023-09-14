#lista
lista = ["Valentin Martino", "Electronica", True, 1.80]
#imprimimos toda la lista
print(lista)
#imprimimos el dato que nosotros querramos
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

#la lista se puede modificar
lista[3] = 1.81
print(f"El dato modificado es:  {lista[3]}")

#--------------------------------------------------------------------------------------------------------------------------------------

#tupla
#es igual que la lista, pero esta no se puede modoficar
tupla = ("Valentin Martino", "Electronica", True, 1.80)
#imprimimos toda la tupla
print(tupla)
#imprimimos el dato que nosotros querramos
print(lista[0])#se muestra con []
print(lista[1])
print(lista[2])
print(lista[3])


#--------------------------------------------------------------------------------------------------------------------------------------
#conjunto
#son muy similares a las listas
#se puede redefinir por completo, peronose puede modificar elememnto por elemento
conjunto = {"Valentin Martino", "Electronica", True, 1.80,"Electronica"}
#no almacena datos duplicados 
print (conjunto)


#--------------------------------------------------------------------------------------------------------------------------------------
#diccionario
#essimilar a una estructura en C

diccionario = {
	'nombre': "valentin martino",
	'carrera' : "Electronica",
	'Altura' : 1.80

}

print(diccionario["nombre"],diccionario["carrera"],diccionario["Altura"])








