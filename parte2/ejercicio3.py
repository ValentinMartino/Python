#hay que pedir el nomber y la edad de los alumnos que vinieron hoy a clase
#supongamos que le pedimos al usuario la cantidad de alumnos que asistieron ese dia a clase

def obtenemos_compañeros(num_alumnos):
	#creamos una lista donde se van a ingresar los distintos alumnos
	compañeros = []
	for i in range(int(num_alumnos)):
		nombre = input("ingrese el nombre del alumno: ")
		edad = int(input("ingrese la edad del alumno: "))
		compañero = (nombre,edad)#creamos una tupla con el nombre y la edad de los alumnos
		compañeros.append(compañero)#guardamos la tupla en la lista
	return compañeros

#-------------------------------------------------------------------------------------------------------------------------------------
def obtener_edad(compañero):
    return compañero[1]

#-------------------------------------------------------------------------------------------------------------------------------------

num_alumnos = input("ingrese la cantidad de alumnos que asistieron hoy: ")

compañeros = obtenemos_compañeros(num_alumnos)
compañeros.sort(key = obtener_edad)#en esta linea le estamos indicando al rpgrama que ordene de menor a mayor los datos que se encuentran por edad, ya que short funciona solo con numeros
#tambien se puede usar la siguiente linea de codigo donde se tiene la funcion lambda compañeros.sort(key = lambda x:x[1])
#a la funcion sort se la pasa un key, ya que le debemos indicar que elemento de la tupla queremos usar para ordenar la lista, por eso a la funcion obtener edad se le pasa compañero que es la tupla

nombre_menor = compañeros[0][0]
edad_menor = compañeros[0][1]
nombre_mayor = compañeros[int(num_alumnos)-1][0]
edad_mayor = compañeros[int(num_alumnos)-1][1]

print(f"El profesor sera {nombre_mayor}, ya que tiene {edad_mayor} años")
print(f"El ayudante sera {nombre_menor}, ya que tiene {edad_menor} años")
