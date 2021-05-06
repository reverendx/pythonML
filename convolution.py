#Equipo 3
#Lider/Supervisor: Emilio Gallegos A01066813
#Participante: Josemaria Robledo Lara A01612376


#Se importan las bibliotecas necesarias.
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

#Se hace una operacion de convolucion entre la matriz de 4x4 y el kernel de 2x2

#Se llama la función de convolución y se pasa la matriz de entrada.
#Funcion de la libreria de scipy 
temp = signal.convolve2d(Matriz, Kernel, mode='same')   #Gracias al same se mantienen las dimensiones de la imagen de entrada 
temp

#Función de la convolución para el filtrado de imágenes
def show_convolve2d(imagen, Kernel):

  matplotlib
  plt.ion()

  image_list = []
  for d in range(3): #El 3 representa cada canal de la imagen.
    temp = signal.convolve2d(imagen[:,:,d], Kernel, boundary='symm', mode='same') #Imagen del mismo tamaño 
    imagen_list.append(temp)

  imagen_filt = np.stack(imagen_list, axis=2)
  imagen_filt[imagen_filt > 255] = 255
  imagen_filt[imagen_filt < 0] = 0
  imagen_filt = imagen_filt.astype('uint8')
   
  plt.subplot(1,2,1)
  io.imshow(imagen_filt) #Se muestra la imagen filtrada
  plt.axis('off')

  plt.subplot(1,2,2)
  io.imshow(imagen) #Se muestra la imagen original para futuras comparaciones.
  plt.axis('off')
  
  io.show()

#Se carga una imagen de prueba del directorio con dimensiones pequeñas
filename = os.path.join('prueba.jpg') 
#Se lee la carpeta que contiene la imagen prueba
imagen = io.imread(filename)
