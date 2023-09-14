#forma no optima de sumar valores
def suma(a,b):
	return a+b

#otra forma de hacerlo de forma no optima
def suma1(lista):
	numero_sumado = 0
	for numero in lista:
		numero_sumado = numero_sumado + numero
	return numero_sumado

def suma2(nombre,*numeros):#te convierte todos los parametros en uno, pero se debe agregar siempre al final de los parametros
	return f"{nombre}, la suma de tus numeros es {sum(numeros)}"



resultado = suma(3,5)
print(resultado)
resultado = suma1([1,3,5,6,7,8])
print(resultado)
resultado = suma2("Valentin",1,3,5,6,7,8)
print(resultado)
