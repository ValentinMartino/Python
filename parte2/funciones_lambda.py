multiplicar_por_dos = lambda x : x*2
#es como asignar una funcion a una variable
#se usan para funciones simples y cortas, donde no se necesita return
#y solo se debe tener una isntruccion, para mas de una isntruccion no se utiliza
print(multiplicar_por_dos(5))

#creando una funcion que diga si es par o no
def es_par(num):
	if (num % 2 == 0):
		return True


#usando filter como funcion
numeros = [1,2,3,4,5,6,7,8,9]

numeros_pares = filter(es_par,numeros)#esto nos va a devolver una lista con los numeros pares que ahaya en esa lista
print(list(numeros_pares))#se necesita poner list si o si para poder crear la lista


#ahora se hace con una funcion lambda
numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
print(list(numeros_pares))
