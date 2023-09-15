#el metodo funciona de la siguiente  manera  dato.metodo()

cadena1 = "Hola Soy Vala"
cadena2 = "Olor,a,Bola"
cadena3 = "holabro"

#con la funcion dir te devuelve todo lo que se puede hacer con un tipo de dato
resultado  = dir(cadena1)#esto es una funcion
#print(resultado)

#convierte todo a mayusculas
resultado = cadena1.upper()
print(resultado)



#convierte todo a minuscula
resultado = cadena1.lower()
print(resultado)

#convierte la primer letra en mayuscula
resultado = cadena1.capitalize()
print(resultado)

#buscamos una cadena en otra cadena
resultado = cadena1.find("Hola")#devuele la posicion donde se encontro
print(resultado)
resultado = cadena1.find("a")#si no encuentra algo devuelve menoos 1
print(resultado)

#si es numerico devuelve true
resultado = cadena1.isnumeric()
print(resultado)

#si es alfanumerico devuelve true
resultado = cadena1.isalpha()#solo con caracteres de la a la z, sin espacios
print(resultado)
resultado = cadena3.isalpha()
print(resultado)

#nos dice la cantidad de veces que hay concidencias
resultado = cadena1.count("a")
print(resultado)

#contamos cuantos caracteres tiene una cadena
resultado = len(cadena1)#len no es un metodo, si no una funcion
print(resultado)

#verificamos si una cadena comienza con algo
resultado = cadena1.startswith("Hola")
print(resultado)

#verificamos si una cadena termina con algo
resultado = cadena1.endswith("Valu")
print(resultado)

#reemplaza un pedazo de cierta cadena por otro que querramos
resultado = cadena1.replace("la","lu")#reemplaza los la de la cadena por lu
print(resultado)

#separar cadenas con la cadena qu le pasemos
resultado = cadena2.split(",")#crea una lista con la cedana que le pasemos 
print(resultado)
resultado = cadena1.split(" ")#crea una lista con la cedana que le pasemos 
print(resultado)













