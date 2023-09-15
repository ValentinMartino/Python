
nombre = "valu"
nombre2 = 5

#esto es la concatenacion , la cual permite concatenar variables, sin importar su tipo 
mensaje = f"hola  {nombre} , bienvenido a python"
print(mensaje) #con una cadena
mensaje = f"hola  {nombre2} , bienvenido a python"#para meter valores distintos de chars se pone el f adelante
print(mensaje) #con un entero



#tambien existe la concatenacion de cadenas 
nombre3 = "hola, todo bien " + nombre + ", ¿Como estas?"
print(nombre3)#este tipo de concatenacion solo permite cadenas



#operadores de pertenecia
#estos operadores devuelven un true o false, dependiendo si en la cadena se encuentra lo que le indicamos
print("valu" in mensaje)#False
print("hola" in mensaje)#True
print("hola" not in mensaje)#False

