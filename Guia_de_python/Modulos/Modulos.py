# se necesita importar el modulo, el cual debe estar en la misma carpeta
import modulos_saludar as m_saludar
#la palabra as, se utiliza para cambiar el nombre de los modulos para nuestra conveniencia
#tambien se puede importar solo la funcion y no todo el modulo
#from modulo_saludar import saludar, saludar_raro
#el as tambien sirve para renombrar otras funciones

#la funcion, ya no se accede mas como fucnion, sino como un metodo
saludo = m_saludar.saludar("valu")#se llama utilizando el nombre_modulo.nombre_funcion()
print(saludo)
saludo = m_saludar.saludar_raro("valu")#se llama utilizando el nombre_modulo.nombre_funcion()
print(saludo)
