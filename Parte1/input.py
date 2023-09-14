#pedimos un dato al usuario
#la funcion input simpre devuelve es un texto
nombre = input("introduzca su nombre: ")
apellido = input("introduzca su apeliido: ")
nombre_completo = nombre.capitalize() + " " + apellido.capitalize()
print(f"su nombre es: {nombre_completo}")

#por lo tanto si le pedimos un numero hay que pasarlo a entero antes de podes operar el mismo
edad = input("ingrese su edad: ")
#ahora se debe convertir el numero a entero y multiplicarlo por dos
resultado = int(edad) * 2
print(f"Tu edad multiplicada por dos es: {resultado}")
#lo mismo se puede hacer con flotante 
resultado = float(resultado)
print(f"Tu edad multiplicada por dos es: {resultado}")
