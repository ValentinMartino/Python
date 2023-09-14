#grafico de barras
import pandas as pd
import matplotlib.pyplot as plt #usamos esta librerira
import seaborn as sns#esta libreria es para graficos estadisticos
#abrimos el archivo .csv
df = pd.read_csv("cofla_ingresos.csv")
#generando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)
#creando un punto en el momento de mas pedos

#mostramos ademas los ingreosos totales
total_ingresos = df["ingresos"].sum()#nos suma todos los valores que hay en esa columna
print(f"El total de ingresos es: {total_ingresos}")

#mostrando el grafico
plt.show()
