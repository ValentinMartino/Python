import pandas as pd
#cambiar el tipo de dato de un columna

df = pd.read_csv("datos.csv")
df["edad"] = df["edad"].astype(str)#cambiamos los datos de numero a str

#cambiar un elemento
df["nombre"].replace("valentin","valu",inplace = True)#me reemplaza valentin por valu
#print(df["nombre"])

#eliminamos las filas con datos faltantes
print(df)
df = df.dropna()
print(df)

#eliminamos las filas repetidas
df = df.drop_duplicates()
print(df)


#creando un archivo con el dataframe nuevo
df.to_csv("datos_limpios.csv")
