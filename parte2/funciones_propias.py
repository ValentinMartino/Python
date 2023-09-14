#creando una funcion simple

def saludar():
	print("hola lucas como andas pa")

#creando una funcion que tenga parametros
def saludar1(nombre,sexo):
	if (sexo.lower() == "mujer"):
		adjetivo = "reina"
	elif(sexo.lower() == "hombre"):
		adjetivo = "rey"
	else:
		adjetivo = "none" 
	print(f"Hola {nombre.capitalize()}, como andas {adjetivo}?")


saludar1("valu","Hombre")

#crear una funcion que retorne valores
def crear_contraseña_aleatoria(num):
	chars = "jhfasoiduf"
	num_entero = str(num)#convertimos el numero en una cadena
	num = int(num_entero[0])#tomamos el primer valor de ese numero y lo convertimos a entero otra vez
	c1 = num - 1
	c2 = num -4
	c3 = num
	contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
	return contraseña
	
contraseña = crear_contraseña_aleatoria(98)
print(f"Tu contraseña es: {contraseña}")


#ademas se pueden devolver multiples valores
#por ejemplo podemos devolver una tupla de la siguiente manera
#return (contraseña,num)
#y para recibir
#contraseña,numero = crear_contraseña_aleatoria(98)
