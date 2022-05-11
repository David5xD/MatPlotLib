import matplotlib.pyplot as plt

# Basada en el rating del día 10 de Abril del 2022.

# plt.style.use('ggplot')

# plt.xkcd()

# Cambia el estilo de la gráfica. __doc__

plt.figure(figsize=(12, 8))

width = 0.25

# Cambia el ancho de las barras

programas = ['Noticias Caracol', 'Los Informantes', 'Séptimo Día', 'Masterchef Celebrity', 'The Susos Show', 'Factor X', 'Noticias RCN']

rating = [8.4, 7.9, 7.9, 6.9, 5.6, 4.0, 3.2]

# En este caso, como lo que queremos es un gráfico de barras, no necesitamos de poner valores númericos en el eje y. por tanto, colocamos el nombre que queramos en el eje y, en este caso "programas" y "rating" como eje x.

colors = ("orange", "orange", "orange", "cornflowerblue", "orange", "red", "cornflowerblue", "cornflowerblue")

plt.xlabel('Programas', fontname='Courier New', fontsize="8")
plt.ylabel('Rating en Puntos', fontname='Arial', fontsize="8")

# Modificamos el tamaño de la letra y su estilo, como por ejemplo, 'fontname' cambia el estilo, mientras que 'fontsize' cambia su tamaño

plt.title('Rating en Colombia del día 10 de Abril del 2022')

plt.bar(programas, rating, width, color = colors)

plt.grid(False)

# Muestra una cuadricula dentro del gráfico

plt.savefig('rating.png')

plt.show()