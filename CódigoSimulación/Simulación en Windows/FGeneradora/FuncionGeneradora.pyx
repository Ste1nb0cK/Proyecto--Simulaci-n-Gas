import random
import numpy as np
from ParticleClass import hello as hell
#Prototipo de la función final, recibe las dimensiones de la caja, el rango de velocidades inciales y el número de partículas
#Si algo podemos establecer por defecto que las masas y los radios sean los mismos por defecto o cómo quieran
def funcion_generadora(float lx,float ly,float v1,float v2,float m,float r,int n):
#Por el momento se crea un arreglo vacío de enteros para las posiciones iniciales
  posiciones=np.zeros((n,2))
  
  for i in range(n):
    #Se llena el arreglo con números aleatorios dentro del rango de las dimensiones de la caja
    posiciones[i][0]=np.random.uniform(10,lx-10)
    posiciones[i][1]=np.random.uniform(10,ly-10)
  #Se convierte el arreglo en una lista
  posiciones_lista=list(posiciones)
  #Las velocidades se crean normalmente con velocidades aleatorias dentro del rango establecido, el intervalo (v1,v2)
  velocidades_lista=list(np.random.uniform(v1,v2,(n,2)))
  #Ahora creamos una lista vacía donde irán objetos de la clase partícula
  lista_de_particulas=[]
  #Llenamos la lista con partículas que tendrán posiciones provenientes de posiciones_lista y velocidades_lista, le puse una masa y un radio aleatorio 
  #entre 0 y 5.
  for j in range(n):
    Pn=hell.Particula(tuple(posiciones_lista[j]),tuple(velocidades_lista[j]),m,r)
    lista_de_particulas.append(Pn)
  
  
  #Ahora queremeos hacer que si las partículas se crean superpuestas de alguna manera, eliminamos una y creamos otra nueva
  #luego añadimos la nueva partícula a la lista de partículas

  for i in range(n):
   for p1 in lista_de_particulas:
    for p2 in lista_de_particulas:
        
     if p1.ver_colision_pp(p2):
       p_nueva=hell.Particula(tuple([(random.uniform(0,lx),random.uniform(0,ly)) for x in range(1)][0]),
       tuple([(random.uniform(v1,v2),random.uniform(v1,v2)) for x in range(1)][0]), m,r)
                                                      
       lista_de_particulas.pop(i)
       lista_de_particulas.append(p_nueva)
  #Nos retorna la lista con las partículas creadas, acá le puse que me devolviera solo la primera para demostrar funcionalidad

  return lista_de_particulas
