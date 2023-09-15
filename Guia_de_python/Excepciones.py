def sumar_dos():
	while True:
		a = input("Numero 1: ")
		b = input("Numero 2: ")
		try:#intentalo
			#si se cumple y el usuario ingresa dos numeros, sale de while y retorna el resultado
			resultado = int(a) + int(b)
		except:
			#si no ingresa un numero valido, lo vuleve a pedir
			print("Por favor, inserte un numero valido.")
		else:
			break
		finally:
			print("Esto se ejecuta siempre")
	return resultado
	
print(sumar_dos())
