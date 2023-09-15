#creando diccionario con dic
diccionario = dict(nombre = "valentin", apellido = "martino")#esto sirve para crear diccionarios vacios
print(diccionario)

#crando un diccionario con fromkeys() con none
diccionario = dict.fromkeys(["nombre","apellido"])
print(diccionario)

#crando un diccionario con fromkeys() con un valor definido que sea none
diccionario = dict.fromkeys(["nombre","apellido"],"No se")
print(diccionario)

