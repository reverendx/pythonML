#Equipo 3
#Lider/Supervisor: Emilio Gallegos A01066813
#Participante: Josemaria Robledo Lara A01612376


#Se importan las bibliotecas que se usarán
import os
from scipy import signal, misc
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray
from skimage import io 

#Se crea matriz de 4x4 y un kernel de 2x2
Matriz = np.array([[1,1,1,1], [1,1,1,1], [0,0,0,0], [0,0,0,0]])
Kernel = np.array([[1,1], [-1,-1]])
Matriz

#Se llama la función de convulción y se pasa la matriz de entrada
temp = signal.convolve2d(Matriz, Kernel, mode='same')
#Se mantienen las dimensiones de la imagen de entrada
temp

#Función de la convolución para el filtrado de imágenes
def show_convolve2d(imagen, Kernel):

  matplotlib
  plt.ion()

  image_list = []
  for d in range(3):
    temp = signal.convolve2d(imagen[:,:,d], Kernel, boundary='symm', mode='same')
    imagen_list.append(temp)

  imagen_filt = np.stack(imagen_list, axis=2)
  imagen_filt[imagen_filt > 255] = 255
  imagen_filt[imagen_filt < 0] = 0
  imagen_filt = imagen_filt.astype('uint8')
  
#Primero se muestra la imagen filtrada
  plt.subplot(1,2,1)
  io.imshow(imagen_filt)
  plt.axis('off')

#Después la imagen original
  plt.subplot(1,2,2)
  io.imshow(imagen)
  plt.axis('off')
  
  io.show()

#Se carga una imagen del directorio
filename = os.path.join('img/', 'prueba.jpg') 
#Se lee la carpeta que contiene la imagen prueba
imagen = io.imread(filename)
