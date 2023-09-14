#if y else

edad = 17

if edad >= 18:
	print("podes pasar")#es un lenguaje que debe estar iterado
	print("forma parte del if") 
else:
	print("no podes pasar") 
	print("formaparte del else")
	
	
contraseña_correcta = "valucrack"
contraseña_ingresada = "holavalu"
	
if contraseña_correcta == contraseña_ingresada:
	print("contraseña correcta")
else:
	print("contraseña incorrecta")
	
	
#---------------------------------------------------------------------------------------------------------------------------------------

ingreso_mensual = 900

if ingreso_mensual > 10000:
	print("estas bien economicamente en qualquier parte delmundo")
elif ingreso_mensual > 1000:
	print("estas bien economicamente en latinoamerica")#en python se utiliza elif
elif ingreso_mensual > 500:
	print("estas bien en argentina")
elif ingreso_mensual > 200:
	print("estas bien en venezuela")
else:
	("sos pobre")
	

