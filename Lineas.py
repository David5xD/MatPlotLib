import matplotlib.pyplot as plt

# Importamos la librería.

plt.figure(figsize=(6, 4))

# Modificamos las propiedades de la figura, en este caso el tamaño de la figura

#Colombia
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y = [45220, 45660, 46080, 46500, 46970, 47520, 48180, 48910, 49660, 50340]

#Argentina
x2 = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y2 = [40790, 41260, 41730, 42200, 42670, 43130, 43590, 44040, 44490, 44940]

#Venezuela
x3 = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y3 = [28440, 28890, 29360, 29780, 30040, 30080, 29850, 29400, 28890, 28520]

#Perú
x4 = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y4 = [29030, 29260, 29510, 29770, 30090, 30470, 30930, 31440, 31990, 32510]

# Colocamos los puntos, en este caso (x,y) son (3,2), (7,9) y (12,11)

#Colombia
plt.plot(x, y, marker='o', linestyle='-', color='gold', label='Colombia')

#Argentina
plt.plot(x2, y2, marker='s', linestyle=':', color='royalblue', label='Argentina')

#Venezuela
plt.plot(x3, y3, marker='*', linestyle='--', color='maroon', label = 'Venezuela')

#Peru
plt.plot(x4, y4, marker='^', linestyle='-.', color='red', label = 'Perú')

# Grafica los puntos propocionados en una línea con eje x y y.

# Marker cambia el estilo de los puntos.
# Ej: 'o' = circulo, 's' = cuadrado, '*' = estrella, etc.

# Linestyle cambia el estilo de la líneas
# Ej: '-' = solida, ':' = puntos, '--' = barras, etc.

# Color cambia el color de la línea.
# Ej: 'b' = azul, 'g' = verde, 'r' = rojo, etc.

# Label añade un título a cada línea, esencial para hacer leyendas.

plt.xlabel('Años (Década del 2010)')
plt.ylabel('Población (en Miles)')

# Añade un título al eje x y al eje y.

plt.title('Población de Países en la Década de 2010')

# Añade un título a la gráfica en general.

plt.legend(loc='lower right')

# Añade una leyenda, además se especifica que se encuentra en la parte inferior derecha.

plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])
plt.yticks([20000, 30000, 40000, 50000])

# Modifica los valores mostrados en el eje x y y dentro de la gráfica.

plt.savefig('poblacion.png')

# Guarda la figura como poblacion en el formato png.

plt.show()

# Muestra la figura.