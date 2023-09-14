import pandas as pd
#leemos el arhcivo utilizando la librerira pandas
df = pd.read_csv("datos.csv")
df2 = pd.read_csv("datos.csv")
#df porque es un data frame

#con esto le estoy indicando que me muestre toda la columna de nombre
nombres = df["nombre"]

#como se cargan los encabezados de forma diferente
#df = pd.read_csv("datos.csv",names = ["name","lastname","age"])


cadena = "0123456789"
#print(cadena[0])#nos muestra el valor 0
#print(cadena[1:4])#con esto se puede indicar desde donde hasta donde queres que te lea


#ordenar los dataframe por la edad
df_ordenado = df.sort_values("edad")
#print(df_ordenado)

#ordenar de forma descendente
df_ordenado = df.sort_values("edad", ascending = False)
#print(df_ordenado)

#concatenamos dos datas frames
df_concatenados = pd.concat([df,df2])
#print(df_concatenados)

#accediendo a las primeras 3 filas con head
primer_fila = df.head(3)
print(primer_fila)

#accediendo a las ultimas 3 filas con tail
ultima_fila = df.tail(3)
print(ultima_fila)


#accediendo a la cantidad de filas y columnas que tiene el archivo
filas_columnas = df.shape#nos devuelve una tupla
filas,columnas = filas_columnas
print(f"filas: {filas}")
print(f"Columas: {columnas}")


#obteniendo data estadisticas para el analisis de datos
df_info = df.describe()
print(df_info)#nos da distintos datos de el archivo


#accediendo a la data de un elelemto especifico con loc
elemento_especifico = df.loc[2,"edad"]#fila 2, columna edad
print(elemento_especifico)


#accediendo a la data de un elelemto especifico con iloc
elemento_especifico = df.iloc[2,2]#fila 2, columna 2
print(elemento_especifico)

#accediendo a filas mayores a 30
mayor_que_30 = df.loc[df["edad"]>30,:]
print(mayor_que_30)














