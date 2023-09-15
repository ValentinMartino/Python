#creando un conjunto con set
#hay que enteneder lo de subconjuntos y superconjuntos

conjunto = set(["dato 1","dato 2"])

print(conjunto)

conjunto1 = set(["dato 1",("dato_lista1","dato_lista2")])# una tupla dentro de un conjunto

print(conjunto1)

conjunto2 = frozenset(["dato 1","dato 2"])
conjunto3 = {conjunto2, "dato 3"}
print(conjunto3)

#teoria de conjuntos
conjunto1 = {1,3,7}
conjunto2 = {1,3,5,7}


#verificando si es un subconjunto
resultado = conjunto1.issubset(conjunto2)#este metodo nos devuelve True o False dependiendo si conjunto1 es un subconjunto de conjunto2
print(resultado)

#otra forma de hacerlo
resultado = conjunto1 <= conjunto2
print(resultado)


#verificamos si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
print(resultado)

#otra forma de hacerlo
resultado = conjunto2 > conjunto1
print(resultado)


#verificamos si hay algun elemento en comun
#si un elemento es comun entre los dos conjuntos, devuelve False
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)


