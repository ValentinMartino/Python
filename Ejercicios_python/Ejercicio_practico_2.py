#El usuario ingresa la frase
frase = input("Ingrese la frase que desee: ")
#Creamos una lista con la cadena que le pasamos 
frase_lista = frase.split(" ")
#Obtenemos la cantidad de palabras que hay en la frase
cantidad_de_palabras = len(frase_lista)
print(f"La frase contiene: {cantidad_de_palabras} palabras")
#calculamos el tiempo que se tarda en promedio en decir la frase
tiempo_prom = cantidad_de_palabras * 0.5
print(f"El tiempo que se tarda es de: {tiempo_prom} segundos")

#si la persona tarda mas de 60 segundos en decir la frase
if tiempo_prom > 60:
	print("Para flaco tampoco te pedi un testamento")

#calculamos el tiempo para una persona que habla un 30% mas rapido
tiempo_dalto = tiempo_prom * 0.7
print(f"El tiempo que se tarda dalto es de: {tiempo_dalto} segundos")

