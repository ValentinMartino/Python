def frase(nombre,apellido,adjetivo):
	return f"hola {nombre} {apellido}, soy muy {adjetivo}"
	
resultado = frase(apellido = "martino", adjetivo = "facha", nombre = "valentin")#se puede pasar los argumentos desordenados siempre y cuando se aclare que argumento se le esta pasando, son parametros de palabra clave
print(resultado)

