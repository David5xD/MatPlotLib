import matplotlib.pyplot as plt

# Basada en la última encuesta INVAMER.

candidatos = ['Petro', 'Fico', 'Rodolfo', 'Fajardo', 'Betancourt', 'Pérez', 'Rodriguez', 'Gómez']

porcentaje = [43.6, 26.7, 13.9, 6.5, 0.5, 0.5, 1.5, 1.1]

# En este caso, como lo que queremos es un gráfico circular, no necesitamos de poner valores númericos
# en el eje y. por tanto, colocamos el nombre que queramos en el eje y, en este caso "candidatos" y "porcentajes"
# como eje x.

colors = ("purple", "blue", "gold", "lime", "green", "red", "darkblue", "royalblue")

# Añade patrón de colores

explode = (0.1, 0.1, 0.1, 0.1, 0.5, 0.4, 0.3, 0.2)

# Expande la distancia de la parte del gráfico del centro a los exteriores.

total = sum(porcentaje)

# Total nos ayudará a introducir los valores dentro de cada gráfico más adelante, ahora solo realiza la suma
# de todos los valores del porcentaje.

plt.title('Preferencia de Candidatos Presidenciales (Invamer)')

plt.pie(porcentaje, explode = explode, labels = candidatos, autopct = lambda p: '{:.0f}%'.format(p * total/100), colors = colors, shadow = True)

# Pedimos que cree un gráfico círcular usando como "candidatos" los títulos de cada parte de la gráfica,
# así como "porcentajes" sus respectivos valores, además de proporcionar personalizaciones como lo es
# colors, explode o shadows.

# Además usamos autopct para poner porcentajes dentro de cada uno de las partes de la gráfica, usando
# lambda calculamos el porcentaje como el total / 100 y que solo refleje valores enteros.

plt.savefig('encuesta.png')

plt.show()