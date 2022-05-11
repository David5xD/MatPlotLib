import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Utilizamos la librería numpy para permitir uso de funciones avanzadas de matemáticas
# Como matplotlib es un programa basado en gráficas 2D usamos mpl_toolkits para poder graficar en 3D

ax = plt.axes(projection="3d")

# Pedimos que nos muestre una proyección en tres dimensiones.

x_data = np.arange(-5, 5, 0.1)
y_data = np.arange(-5, 5, 0.1)

# Pedimos que nos muestre los datos con un mínimo de -5 a 5 en ejes x y y, y de -0.1 a 0.1 en el eje z.

X, Y = np.meshgrid(x_data, y_data)
Z = np.sin(X) * np.cos(Y)

# Meshgrid retorna matrices coordenados de vectores coordenados, x y y no son alterados, por tanto x=y, sin
# embargo, se modifica Z tal que Z es igual al seno de X * el coseno de Y.

ax.plot_surface(X, Y, Z, cmap="plasma")

# Se almacena en una superficie, usando los ejes x, y y z, y además usando el cmap "plasma" para reflejar
# con diferente color los puntos altos y bajos de la gráfica.

plt.show()
