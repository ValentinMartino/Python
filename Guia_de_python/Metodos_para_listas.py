#creando una lista con list
lista = list(["hola","valu",22])
lista1 = [23,45,2,8,4,35,True]

print(lista)

#funcion len
#nos devuelve la cantidad de elementos que tiene la lista
resultado = len(lista)
print(resultado)


#------------------------------------------------------------------------------------------------------------------------------------
#agregando  elemento a la lista
lista.append("electronica")
#lo que hace es a la  lista original agregar un valor al final
print(lista)

#------------------------------------------------------------------------------------------------------------------------------------
#agregando un elemento a la lista con un indice especifico
lista.insert(2,"hincha de boca")#en la posicion 2 agrega eso
print(lista)

#-----------------------------------------------------------------------------------------------------------------------------------
#agregando varios elementos a la lista
lista.extend([False,2023])#basicamente se unen listas
print(lista)

#-------------------------------------------------------------------------------------------------------------------------------------
#eliminando un elemento de la lista
lista.pop(0)#se le pasa el lugar donde se encuentra el elemento
print(lista)
#si ponemos -1 se elimina el ultimo, si ponemos -2 el anteultimo y asi

#-------------------------------------------------------------------------------------------------------------------------------------
#eliminando un elemento por su valor
lista.remove("hincha de boca")
print(lista)
#si le pedimos que elimine algo que no esta, salta error
#-------------------------------------------------------------------------------------------------------------------------------------
#eliminando todos los elementos de la lista
#lista.clear()
#print(lista)

#-------------------------------------------------------------------------------------------------------------------------------------
#ordena todos los elementos de la lista, si es que son numeros
lista1.sort()
print(lista1)
lista1.sort(reverse = True)
print(lista1)

#-------------------------------------------------------------------------------------------------------------------------------------
#inverte la cadena, sin ordenar la misma
lista1.reverse()
print(lista1)

#------------------------------------------------------------------------------------------------------------------------------------
#encontrar un elemento en la lista
resultado = lista1.index(2)
print(resultado)

