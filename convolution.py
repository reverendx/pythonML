#Equipo 3
#Lider/Supervisor: Emilio Gallegos A01066813
#Participante: Josemaria 


#Se importa las bibliotecas que se usarán
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
