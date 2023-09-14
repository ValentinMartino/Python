#se llama a un modulo que se encuentra en la carpeta modulos y con el as se lo denomina modulos
import modulos.modulos_saludar as saludos

#entonces con este ya se puede usar la funcion de otro modulo que se encuentra en otra carpeta
frase = saludos.saludar("valu")
print(frase)


