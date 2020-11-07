# -*- coding: utf-8 -*-
"""Los alumnos de Boltzman

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KTCr2iZsKySVXdCmwQQvW5zfm_vDgyiP
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Commented out IPython magic to ensure Python compatibility.
# %load_ext Cython

# Commented out IPython magic to ensure Python compatibility.
# %%cython
# import numpy as np
# class Particula:#En esta clase definimos los métodos fundamentales que debe seguir cada partícula
#  
#     def __init__(self, (float,float) velocidad , int masa , (float,float) posicion ,float radio): 
#       """comenzamos definiendo el método que debe 
#        inicializar la clase, en este definimos los atributos básicos de la clase partícula
#        las entradas masa y radio son de tipo entero y las entradas de posición son tuplas"""  
#       self.radio=radio #Estas variables son de tipo entero  ##¿Por qué la masa y el radio son enteros? Att: Nicolás
#       self.masa=masa 
#     
#       self.posicion=np.array(posicion) #Estas variables son arrays de numpy, y las trataremos como vecotores
#       self.velocidad=np.array(velocidad)
#       self.velocidad_mag=np.linalg.norm(self.velocidad)#Este atributo no es otra cosa que la magnitud del vector velocidad
#     
#       """Creamos dos listas con copias de los vectores posición y velocidad y velocidad_mag, posteriormente las usaremos
#       para actualizar la información a medida que vaya avanzando la simulación"""
#       
#       self.velocidad_n=[np.copy(self.velocidad)]
#       self.posicion_n=[np.copy(self.posicion)]
#       self.velocidad_mag_n=[np.copy(self.velocidad_mag)]
#     
#  ##########################################################################
#     def paso_dt(self,int dt):
#       """Este método lo que hace es avanzar en el tiempo, cambia la posición de la partícula y agrega a las listas
#       una actualización tanto de la posición de la partícula como la velocidad de la misma"""
#      
#       self.posicion=self.posicion + self.velocidad*dt
#       self.velocidad_n.append(np.copy(self.velcidad))
#       self.posicion_n.append(np.copy(self.posicion))
#       self.velocidad_mag_n.append(np.copy(self.velocidad_mag))
# ###############################################################################################
#     def ver_colision(self,otra_p):
#       """Este método verifica si se dio luegar a una colisión entre dos partículas, las entradas
#      son dos partículas, se definen sus radios y posiciones y se plantea una condición que indica 
#      si las partículas chocaron"""
#       cdef int r1=self.radio
#       cdef int r2=otra_p.radio
#       p1=self.posicion
#       p2=otra_p.posicion
#       cdef float sep=np.linalg.norm(p1-p2)#Norma del vector separación de ambas partículas
#       if sep-(r1+r2)<=0:#Si la separación es menor o igual a la suma de sus radios, entonces las partículas están en contacto y por lo tanto chocaron
#         return True
#       else:
#         return False



import numpy as np
a = np.array([1,2,3,4])
a.append(5)
print(a)

fig, axes=plt.subplots()
x_datos=[]
y_datos=[]
graficar,=plt.plot([],[])

def lim():
  axes.set_xlim(0,2*np.pi)
  axes.set_ylim(-1,1)
  return graficar,

def funcion(x):
  x_datos.append(x)
  y_datos.append(np.cos(3*x))
  graficar.set_data(x_datos,y_datos)
  return graficar,

ani=FuncAnimation(fig,funcion,frames=np.linspace(0,4*np.pi,500),init_func=lim,blit=True)
from IPython.display import HTML
HTML(ani.to_jshtml())