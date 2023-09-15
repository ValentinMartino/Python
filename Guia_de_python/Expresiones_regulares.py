import re

texto = '''Hola mi rey, como estas?, te banco mucho
Esta es la 234. linea pa
y esta aca esta la tercer linea campeon'''

resultado = re.search("Hola",texto)#nos busca el objeto hola en el texto

resultado = re.findall("esta",texto)#nos busca todos los esta que hay en el tetxo

resultado = re.findall("esta",texto,flags = re.IGNORECASE)#al igual que el anterior pero nos ignora las mayusculas


#\d ->busca numeros numericos del 1 al 9
resultado = re.findall(r"\d",texto)

#\D ->busca TODO MENOS caracteres numericos del 1 al 9
resultado = re.findall(r"\D",texto)

#\w ->busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w",texto)


#\W ->busca Todo menos caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\W",texto)

#\s->busca espacios en blanco
resultado = re.findall(r"\s",texto)

#\S->busca Todo menos espacios en blanco
resultado = re.findall(r"\S",texto)

#.->busca Todo menos saltos de linea
resultado = re.findall(r".",texto)

#\n ->busca saltos de linea
resultado = re.findall(r"\n",texto)

#buscando un numero, segudio por un punto, seguido por un espacio en blanco
resultado = re.findall(r"\d\.\s",texto)

#buscando el principio de una linea mas un hola
resultado = re.findall(r"^Hola",texto)

#buscando el principio de una linea mas un hola
resultado = re.findall(r"campeon$",texto)

#\d ->busca numeros numericos del 1 al 9 que esten en una cadena juntos
resultado = re.findall(r"\d{3}",texto)

print(resultado)
