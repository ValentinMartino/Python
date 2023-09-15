#grafico de lineas
import pandas as pd
import matplotlib.pyplot as plt #usamos esta librerira
import seaborn as sns#esta libreria es para graficos estadisticos
#abrimos el archivo .csv
df = pd.read_csv("pedos.csv")
#generando el grafico
sns.lineplot(x="fecha",y="pedos",data=df)
#creando un punto en el momento de mas pedos
plt.plot("01-06",9,"o")
#mostrando el grafico
plt.show()
