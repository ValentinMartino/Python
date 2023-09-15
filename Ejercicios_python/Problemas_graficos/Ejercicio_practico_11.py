#grafico de bigotes
import pandas as pd
import matplotlib.pyplot as plt #usamos esta librerira
import seaborn as sns#esta libreria es para graficos estadisticos
#abrimos el archivo .csv
df = pd.read_csv("bigotes.csv")
#generando el grafico
sns.boxplot(x="categoria",y="valor",data=df)
#creando un punto en el momento de mas pedos

#mostrando el grafico
plt.show()
