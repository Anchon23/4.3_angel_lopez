import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/angel/Downloads/adult(1).csv", sep=';')

df['sex'] = df['sex'].map({1: 'mujer', 0: 'hombre'})

# Contar el número de mujeres y hombres para cada categoría de ingresos
counts = df.groupby(['sex', 'income']).size().unstack()

# Crear el gráfico de barras
counts.plot(kind='bar')

# Personalizar el gráfico
plt.xlabel('sex')
plt.title('Numero de mujeres y hombres con altas ganancias y bajas')
plt.legend(title='income', labels=['<50K', '>50K'])

# Mostrar el gráfico
plt.show()