#para iterar conjuntos es lo mismo que en listas y tuplas
#vamos a copiar el codigo anterior y va a funcionar igual

animales = {"perro","pez","gatos","jirafas","leones"}
numeros = {10,60,70,5,8}
for animal in animales:
	print(f"Ahora la variables animal es: {animal}")


for numero in numeros:
	print(f"el numero multiplicado por 2 es: {numero*2}")
	
	
#como recorrer dos listas al mismo tiempo
#para esto la lista deben tener la misma cantidad de miembros y se debe usar la funcion zip
for numero,animal in zip(animales,numeros):
	print(f"recorriendo lista 1: {animal}")
	print(f"recorriendo lista 2: {numero}")

#utilizando la funcion range
#al pasarle dos parametros, los numeros fan desde el valor que pusimos primero hasta el valor del segundo menos 1
#al pasarle un solo dato, los valores van de 0 hasta el valor ese menos 1
for num in range(5,10):
	print(num)
	

#forma correcta de recorrer una lista con su indice
#ya que nos crea una tupla, donde el primer termino es el indice y el segundo es el valor
for num in enumerate(numeros):
	indice = num[0]
	valor = num[1]
	print(f"el indice es {indice} y el valor es {valor}")
	
	
#usando for/else
for numero in numeros:
	print(f"el numero multiplicado por 2 es: {numero*2}")
else:
	print("el blucle se termino")#es por si no se encuentran valores en el bucle
