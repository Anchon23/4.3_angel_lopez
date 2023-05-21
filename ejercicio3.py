import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/angel/Downloads/adult(1).csv", sep=';')

df['sex'] = df['sex'].map({1: 'mujer', 0: 'hombre'})

pivot_table = df.pivot_table(index='education.num', columns=['income', 'sex'], aggfunc='size', fill_value=0)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

etiqueta = ['<50k', '>50k']

sizes = pivot_table[(-1, 'mujer')]
axes[0, 0].pie(sizes, labels=etiqueta, autopct='%1.1f%%', startangle=90)
axes[0, 0].set_title('Mujeres <50k')

sizes = pivot_table[(1, 'mujer')]
axes[0, 1].pie(sizes, labels=etiqueta, autopct='%1.1f%%', startangle=90)
axes[0, 1].set_title('Mujeres >50k')

sizes = pivot_table[(-1, 'hombre')]
axes[1, 0].pie(sizes, labels=etiqueta, autopct='%1.1f%%', startangle=90)
axes[1, 0].set_title('Hombres <50k')

sizes = pivot_table[(1, 'hombre')]
axes[1, 1].pie(sizes, labels=etiqueta, autopct='%1.1f%%', startangle=90)
axes[1, 1].set_title('Hombres >50k')

plt.tight_layout()
plt.show()