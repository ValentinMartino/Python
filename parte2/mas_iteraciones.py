frutas = ["banana","manzana","ciruela","mandarina","sandia","pera","limon"]
cadena = "hola valu"
numeros = [2,4,6,8]

for fruta in frutas:
	if fruta == "limon":#esto hace que cuando fruta sea igual a limon, lo saltee y sigue iterando
		continue
	print(f"me voy a comer una: {fruta}")
	
#evitamos ahora que cuando llegue a cierto elemento el bucle se detenga y no siga iterando
#hacemos de cuenta que una vez que coma la pera no queremos comer mas
for fruta in frutas:
	print(f"me voy a comer una: {fruta}")
	if fruta == "pera":
		break
	

#recorrer una cadena de texto
for letra in cadena:
	print(letra)
	
	
	
#duplicamos los numeros en una solo linea de for

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)	
