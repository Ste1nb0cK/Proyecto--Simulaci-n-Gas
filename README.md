# SIMULACIÓN DE UN GAS IDEAL CON PYTHON
Obejtivos principales: En este proyecto se busca, haciendo uso del lenguaje de programación Python y sus herramientas, realizar la simulación de un gas ideal confinado en una caja. De manera detallada el objetivo es verificar la ley de los gases ideales (PV=NRT) y verificar que la variable aleatoria definida como la raíz de la suma de los cuadrados de la velocidad de cada partícula del gas, se acopla a la función de distribución de Maxwell Boltzman.

Implementación: Como se dijo anteriormente el proyecto usará como lenguaje único Python y se implementarán recursos propios de este lenguaje como lo son librerías científicas del tipo de numpy o scipy. También se baraja la posibilidad de usar librerías gráficas como lo son Visual Python o Matplotlib, las cuales son de mucha utilidad en proyectos como este.

La columna vertebral del proyecto (en términos de código) serán las clases de Python, en ellas se definirán los métodos pertinentes basados en los principales modelos que se tienen para los gases ideales. En particular, este modelo se basa en considerar cada partícula del gas como un objeto circular con dimensiones definidas como masa y radio, en el caso de la primera, consideraremos que cada una de las partículas tienen exactamente la misma masa. Se considerará también que tanto los choques entre partículas, como los choques con las paredes de la caja son colisiones elásticas.

Finalmente haciendo uso de la información que se pueda extraer y las librerías gráficas nombradas anteriormente se busca realizar una animación de lo que sucede con las partículas dentro de la caja, la cual vendrá acompañada de una gráfica dinámica que comparará en cada instante de tiempo la gráfica de la distribución que sigue la variable aleatoria definida como está en el item de objetivos principales y la distribución real de Maxwel-Boltzman.

# ¿CÓMO FUNCIONA EL CÓDIGO?
# Método init:
Comenzamos creando la clase partícula, la cual, como ya se expuso va a contener todos los métodos que determinarán la evoución del gas. En el método init se definen los atributos 
que va a tener el objeto partícula. Cada partícula va a tener asociada una posición, una velocidad, una masa, un radio y adicional a esto 3 listas que corresponderán a todas las velocidades (vector), posición (vector) y la magnitud de su velocidad (float), para definir un objeto de la clase partícula fuera de la clase misma, podemos ver el siguiente ejemplo:

```
p1=Particula((0,0),(3,4),2,0.5)
```

Esta es una partícula que está en el orígen, su velocidad en la componte horizontal es 3, y en la componente vertical es 4. Tiene masa de 2
y su radio es de 0.5.
# Método paso_dt
Ahora, el siguiente método de la clase es el método paso_dt, lo que hace este método es avanzar el tiempo, aquí se dice que, como es natural en la mecánica, si una partícula está en una posición cualquiera, su posición después de un tiempo dt, no será otra cosa que la posición en la que está sumada a la velocidad que lleva multiplicada por el tiempo dt que ha transcurrido, luego, la nueva posición, la nueva velocidad y su magnitud se añaden a las listas definidas en el método init. Este método lo único que va a recibir será el tamaño del intervalo de tiempo, es decir, dt, el cual es un número flotante. Un ejemplo de cómo funciona esto es el siguiente:
```
p1.paso_dt(0.01)

Definimos el tamaño de dt, que deseamos, si luego queremos saber cuál es su nueva posición, esta será:
p1.posicion=(0.03,0.04)
```

En el archivo hay un ejemplo más complicado que demuestra la funcionalidad del método.

# Métodos de colision
Es necesario revisar si las partículas han chocado con algo a medida que avanza el tiempo. Existen 3 posibles colisiones: muros, esquinas y otras partículas. Para los métodos de colision con muros y esquinas se requiere de las dimensiones Lx (longitud) y Ly (alto) de la caja, retorna verdadero si detecta un choque con la esquina o muro y falso  en caso contrario. Siguiendo con nuestro ejemplo, estos atributos se llaman de esta manera
```
p1.ver_colision_esquina(lx,ly)
p1.ver_colision_muro(lx,ly)
```

También tenemos el método que revisa colisiones con otras partículas, en este caso el método revisa una condición que relaciona la distancia entre la posición de dos partículas, si la distancia es menor o igual a cierta distancia definida en la condición, se tendrá que las partículas chocaron y el método retornará un verdadero, de lo contrario retornará un falso, este método funciona así:
```
p2=Particula((0,0.5),(3,4),2,0.5)
p1.ver_colision_pp(p2)


```
Así se revisa si las partículas colisionaron

# Métodos que resuelven choques
Estos métodos lo que hacen es, actualizar las velocidades de las partículas una vez colisionaron con algo, estos métodos funcionan revisando el valor booleano de los métodos anteriores que solo revisaban si había sucedido un choque, y con base a ese valor se activan o no. Para los choques con los muros se actualizan las velocidades de tal manera que estas nuevas velocidades sean un reflejo de la velocidad con la que chocaron inicialmente, en el caso del choque con una esquina la velocidad se actualiza invirtiendo el vector velocidad completamente, y finalmente para el caso de los choques entre partículas, las velocidades de cada partícula se actualizan siguiendo un modelo de colisiones completamente elásticas en dos dimensiones, el cual se puede encontrar en la bibliografía y el código ilustra bastante bien, para llamar esos métodos, se realiza lo siguiente:

Resolver colision esquina:
```
p1.resolver_colision_esquina

```
No recibe ningún parámetro.

Resolver colision muro:
```
p1.resolver_colision_muro(lx,ly)

```
Recibe las dimensiones de la caja.

resolver colsión con otra partícula:
```
p1.resolver_colision_particula(p2)

```
Recibe como parámetro la partícula con la que se quiere resolver el choque.


