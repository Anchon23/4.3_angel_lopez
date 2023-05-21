import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/angel/Downloads/adult(1).csv", sep=';')

df['sex'] = df['sex'].map({1: 'mujer', 0: 'hombre'})

# Contar el número de mujeres y hombres para cada categoría de ingresos
pivot_table = df.pivot_table(index='education.num', columns=['income', 'sex'], aggfunc='size', fill_value=0)

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

pivot_table[(-1, 'mujer')].plot(kind='bar', ax=axes[0], color='red', label='<50k')
pivot_table[(1, 'mujer')].plot(kind='bar', ax=axes[0], color='blue', label='>50k')
axes[0].set_xlabel('education.num')
axes[0].set_ylabel('Número de mujeres')
axes[0].set_title('Mujeres')
axes[0].legend()

pivot_table[(-1, 'hombre')].plot(kind='bar', ax=axes[1], color='red', label='<50k')
pivot_table[(1, 'hombre')].plot(kind='bar', ax=axes[1], color='blue', label='>50k')
axes[1].set_xlabel('education.num')
axes[1].set_ylabel('Número de hombres')
axes[1].set_title('Hombres')
axes[1].legend()

plt.tight_layout()
plt.show()