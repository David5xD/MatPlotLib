import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import PillowWriter

# Utilizamos la librería numpy para permitir uso de funciones avanzadas de matemáticas, en este caso
# el coseno.

# También usamos PillowWriter para poder crear un archivo gif que contrendra la animación.

fig = plt.figure()

# Creamos una figura en el gráfico.

l, = plt.plot([], [], 'k-')

# Ahora creamos una linea en el mismo gráfico.

plt.xlabel('EjeX')
plt.ylabel('EjeY')

# Renombramos los ejes.

plt.title('Función del Coseno')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

# Creamos límites en el eje x y y, por tanto, solo se visualizara los valores de -5 a 5 en ambos ejes.

def func(x):
    return np.cos(x)*3

# Usando numpy, podemos definir una función, que en este caso, es el coseno de x multiplicado por 3.

metadata = dict(title='Animacion', artist='DLRO')

# Recogemos metadatos para la animacion, dandole un título y el artista.

writer = PillowWriter(fps=15, metadata=metadata)

# Pedimos que cree la animación usando 15 frames por segundo y almacenando los metadatos.

xlist = []
ylist = []

# Como los valores van variando y se van alargando, definimos la lista de x y y como vacíos por ahora.

with writer.saving(fig, "FuncionCoseno.gif", 100):

    # Guarda el archivo usando la figura y pone el nombre del archivo como "sinWave.gif"
    # El 100 indica los puntos por pulgada.

    for xval in np.linspace(-5,5,100):

        # Por cada valor en x en el espacio entre -5 y 5 usando 100 puntos por pulgada.

        xlist.append(xval)
        ylist.append(func(xval))

        # Decimos que la lista en x recoga los valores en el eje x.
        # Y en la lista en y, que recoga los valores resultantes de la función del eje x.

        l.set_data(xlist,ylist)

        # Establecemos los datos, usando lista en x y lista en y.

        writer.grab_frame()

        # Guarda automaticamente la imagen que se encuentra actualmente en la figura y lo salva en el archivo.
        # Va almacenando cada uno de los frames para crear un gif.