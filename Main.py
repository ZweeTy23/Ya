#Importaciones
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Ellipse, Line, Triangle
from kivy.clock import Clock
from kivy.uix.image import Image
from matplotlib import *
from matplotlib_venn import venn2 
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
import random
from kivy.core.window import Window
from kivy.uix.slider import Slider
import matplotlib.pyplot as plt
from kivy.vector import Vector
from kivy.config import Config
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.video import Video
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import ReferenceListProperty, ObjectProperty
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import BooleanProperty
from kivy.graphics.context_instructions import PushMatrix, PopMatrix, Color
from kivy.properties import ListProperty

#Inicio de codigo
class MainScreen(Screen): #definimos la pantalla principal
    def go_to_topics(self): #funcion para ir a la pantalla de temas
        name = self.ids.name_input.text #obtenemos el texto del campo de texto
        if name: #si el campo de texto no esta vacio
            self.manager.current = 'topics' #cambiamos a la pantalla de temas
            self.manager.get_screen('topics').update_title(name) #actualizamos el titulo de la pantalla de temas

class TopicsScreen(Screen): #definimos la pantalla de temas
    def update_title(self, name): #funcion para actualizar el titulo de la pantalla
        self.ids.title_label.text = f'Temas para {name}' #actualizamos el titulo de la pantalla 

    def show_topic(self, instance): #funcion para mostrar un tema
        print(f'Se seleccionó el tema: {instance.text}')  

    def exit_app(self): #funcion para salir de la aplicacion
        App.get_running_app().stop() #cerramos la aplicacion


    
class FuncionesScreen(Screen): #definimos la pantalla de funciones
    def on_enter(self): #funcion para cuando se entra a la pantalla

        # Definir el texto que deseas mostrar en el Label

        texto = (

            "Funciones\n\n"

            "Una función es un tipo especial de relación. Para que una relación sea una función, "

            "cada elemento del dominio debe estar relacionado con exactamente un elemento del codominio.\n\n"

            "Definición formal:\n\n"

            "Una función f de un conjunto A (dominio) a un conjunto B (codominio) es una regla que "

            "asigna a cada elemento x de A exactamente un elemento y de B. Esto se denota como:\n"

            "f: A → B  o  y = f(x).\n\n"

            "Características de una función:\n\n"

            "    Dominio: Conjunto de todos los valores de entrada válidos (x).\n"

            "    Codominio: Conjunto donde están los valores de salida posibles (y).\n"

            "    Rango: Subconjunto del codominio que contiene los valores de salida realmente alcanzados por la función.\n\n"

            "Ejemplo:\n\n"

            "    La función f(x) = x² toma x del conjunto de números reales y produce y = x² como salida.\n"

            "        Si x = 2, entonces f(2) = 4."

                    )
        self.ids.funciones1_label.text = texto #asignamos el texto a la etiqueta
        texto_2 = ( 
            '''
            Una relación es cualquier correspondencia entre los elementos de dos conjuntos. En otras palabras, se define como un conjunto de pares ordenados (x,y)(x,y), donde xx pertenece al primer conjunto (llamado dominio) y yy al segundo conjunto (llamado codominio).
Características de una relación:

    Dominio: El conjunto de todos los valores de entrada (xx) posibles.
    Codominio: El conjunto de valores de salida (yy) posibles.
    Rango: El conjunto de valores de salida realmente obtenidos de la relación.

Ejemplo:

Si A={1,2,3}A={1,2,3} y B={a,b,c}B={a,b,c}, una relación entre AA y BB puede ser:
R={(1,a),(2,b),(3,c)}.
R={(1,a),(2,b),(3,c)}.

Esto significa que 11 está relacionado con aa, 22 con bb, y 33 con cc.
                  '''
                  )
        self.ids.funciones2_label.text = texto_2 #asignamos el texto a la etiqueta
        

    #Poner otro texto
    
class GrafosScreen(Screen): #Creamos una clase para la pantalla de Grafos
    def on_enter(self): #Función que se ejecuta cuando se entra a la pantalla

        texto_0 = (


            "Los grafos se pueden clasificar de varias maneras según sus características:\n"

            "Por la dirección de las aristas:\n"

            "    - Grafo dirigido (dígrafo): Las aristas tienen una dirección, representada por flechas. "

            "Ejemplo: redes sociales donde A sigue a B, pero B no necesariamente sigue a A.\n"

            "    - Grafo no dirigido: Las aristas no tienen dirección. Ejemplo: redes de carreteras bidireccionales.\n\n"

            "Por el peso de las aristas:\n"

            "    - Grafo ponderado: Cada arista tiene un peso o costo asociado. Ejemplo: mapas de rutas con distancias o tiempos.\n"

            "    - Grafo no ponderado: Las aristas no tienen peso.\n\n"

            "Por la conexión entre los nodos:\n"

            "    - Grafo conexo: Existe al menos un camino entre cualquier par de nodos.\n"

            "    - Grafo no conexo: No todos los nodos están conectados.\n"

            "    - Grafo completo: Todos los nodos están conectados entre sí.\n\n"

            "Por la naturaleza de los ciclos:\n"

            "    - Grafo acíclico: No tiene ciclos (es decir, caminos que comienzan y terminan en el mismo nodo).\n"

            "    - Grafo cíclico: Contiene al menos un ciclo.\n\n"

            "Por otras propiedades:\n"

            "    - Multigrafo: Permite múltiples aristas entre dos nodos.\n"

            "    - Pseudografo: Permite la existencia de bucles (aristas que conectan un nodo consigo mismo).\n"

            "    - Árbol: Un grafo conexo y acíclico.\n"

            "    - Grafo bipartito: Los nodos pueden dividirse en dos subconjuntos disjuntos, y las aristas solo conectan nodos de diferentes subconjuntos."

        )

        self.ids.grafos_info0_label.text = texto_0 #asignamos el texto a la etiqueta

        texto_2 = (

            '''
Vértice o Nodo \n

    Es un punto en el grafo.
    Representa un elemento o entidad del sistema que se está modelando.
    Por ejemplo:
        En un grafo que representa una red social, los vértices son las personas.
        En un grafo de ciudades conectadas por carreteras, los vértices son las ciudades.\n\n

Arista\n

    Es una conexión entre dos vértices.
    Representa una relación o vínculo entre los elementos que conectan.
    Puede ser de dos tipos:
        No dirigida: La relación no tiene dirección específica (por ejemplo, amistad en una red social).
        Dirigida: La relación tiene una dirección específica (por ejemplo, una transferencia de dinero de una cuenta a otra).
        '''
        )
        self.ids.grafos_info1_label.text= texto_2 #asignamos el texto a la etiqueta


        texto_3 = (
            '''
En teoría de grafos, el grado (degree) de un vértice es una medida importante que describe cuántas aristas están conectadas a dicho vértice. Hay varias definiciones y variantes del grado dependiendo del tipo de grafo. Aquí te explico los conceptos principales:
1. Grado de un vértice en un grafo no dirigido

    El grado de un vértice, denotado como *deg(v)*, es el número de aristas que están conectadas a vv.
    En términos simples, es el número de vecinos del vértice *v*.

Ejemplo:
Si un vértice tiene conexiones con tres vértices (digamos u,w,x), entonces *deg=3*.

2. Grado de un vértice en un grafo dirigido

En grafos dirigidos, hay dos tipos de grado asociados con un vértice:
    Grado de entrada (in-degree): Es el número de aristas que llegan al vértice.
       
    Grado de salida (out-degree): Es el número de aristas que salen del vértice.
        

3. Propiedades importantes del grado

    En un grafo no dirigido, la suma de los grados de todos los vértices es igual al doble del número de aristas. \n
    (Esto se conoce como el teorema del apretón de manos.)

    En un grafo dirigido, la suma de los grados de entrada es igual a la suma de los grados de salida, y ambos son iguales al número total de aristas.
    '''
        )
        self.ids.grafos_info2_label.text = texto_3 #asignamos el texto a la etiqueta

        texto_4 = (
            '''
1. Según la dirección de las aristas

    Grafo no dirigido:
        Las aristas no tienen dirección.
        Si existe una arista entre uu y vv, se puede recorrer en ambas direcciones.
        Ejemplo: Redes sociales de amistad.

    Grafo dirigido (o dígrafo):
        Las aristas tienen una dirección específica.
        Si existe una arista de uu a vv, no necesariamente existe de vv a uu.
        Ejemplo: Redes sociales de seguimiento (como Twitter).

2. Según la relación entre los vértices

    Grafo simple:
        No tiene aristas múltiples (entre dos vértices hay como máximo una arista) ni bucles (aristas que conectan un vértice consigo mismo).

    Multigrafo:
        Puede tener múltiples aristas entre un par de vértices.

    Pseudografo:
        Puede tener aristas múltiples y bucles.

3. Según el peso de las aristas

    Grafo no ponderado:
        Las aristas no tienen un valor o peso asociado.

    Grafo ponderado:
        Cada arista tiene un peso o costo asociado.
        Ejemplo: Redes de transporte, donde el peso puede representar la distancia o el tiempo.

4. Según la conectividad

    Grafo conexo:
        En un grafo no dirigido, todos los vértices están conectados directa o indirectamente por un camino.

    Grafo no conexo:
        Existe al menos un vértice que no está conectado con otro.

    Grafo fuertemente conexo:
        En un grafo dirigido, hay un camino dirigido entre cualquier par de vértices.

    Grafo débilmente conexo:
        En un grafo dirigido, se convierte en conexo si se ignoran las direcciones de las aristas.

5. Según las propiedades de los vértices y aristas

    Grafo completo:
        Cada par de vértices está conectado por una arista.
        Notación: KnKn​ (donde nn es el número de vértices).

    Grafo bipartito:
        Los vértices se dividen en dos conjuntos UU y VV, y todas las aristas conectan vértices de UU con vértices de VV.
        Ejemplo: Relaciones entre trabajadores y tareas.

    Grafo bipartito completo:
        Cada vértice de UU está conectado con cada vértice de VV.

    Grafo regular:
        Todos los vértices tienen el mismo grado.

    Grafo planar:
        Se puede dibujar en el plano sin que las aristas se crucen.

    Grafo arborescente:
        Es un árbol (conjunto conexo y sin ciclos).

6. Según la existencia de ciclos

    Grafo acíclico:
        No contiene ciclos.
        Ejemplo: Árboles, DAG (Directed Acyclic Graph).

    Grafo cíclico:
        Contiene al menos un ciclo.

    DAG (Directed Acyclic Graph):
        Es un grafo dirigido sin ciclos.
        Ejemplo: Dependencias en proyectos.

7. Otros grafos específicos

    Grafo de caminos:
        Forma una única cadena de vértices.

    Grafo de ciclos:
        Los vértices están organizados en un ciclo cerrado.

    Grafo de estrellas:
        Un vértice central conectado a todos los demás.

    Hipergrafo:
        Generalización donde una arista puede conectar más de dos vértices.

    Grafo dirigido aleatorio:
        Grafo donde las aristas se generan de forma probabilística.

'''
        )
        self.ids.grafos_info3_label.text = texto_4 #asignamos el texto a la etiqueta

class ArbolesScreen(Screen): #creamos una nueva pantalla
    def on_enter(self): #funcion para cuando se entra a la pantalla

        textouniwi = (
            '''
Un grafo de árbol es un tipo especial de grafo que tiene propiedades únicas relacionadas con su estructura y conectividad. Aquí tienes una descripción detallada:
Definición de Árbol

Un árbol es un grafo conexo y acíclico. Es decir:

    Está conectado: Siempre existe un camino entre cualquier par de vértices.
    No contiene ciclos: No puedes empezar en un vértice y regresar al mismo sin repetir aristas.

Propiedades de los Árboles

    Relación entre vértices y aristas:
        Si un árbol tiene nn vértices, entonces tiene exactamente n−1n−1 aristas.
        ∣E∣=∣V∣−1
        ∣E∣=∣V∣−1

    Unicidad del camino:
        En un árbol, existe exactamente un único camino simple entre cualquier par de vértices.

    Conectividad mínima:
        Si eliminas cualquier arista de un árbol, este deja de ser conexo.

    Aumentar una arista crea un ciclo:
        Si agregas una arista a un árbol, se forma un ciclo.

    Grado de los vértices hoja:
        Un vértice hoja tiene grado 1. Estas son las hojas del árbol.

Clasificación de los Árboles

    Árbol raíz:
        Un árbol dirigido con un vértice especial llamado raíz.
        Todas las aristas están dirigidas hacia abajo desde la raíz.
        Términos clave:
            Raíz: Vértice inicial.
            Hojas: Vértices sin hijos.
            Padre: Vértice que apunta hacia otro.
            Hijos: Vértices a los que apunta un padre.
            Nivel: Distancia desde la raíz.
            Altura: Longitud máxima del camino desde la raíz a una hoja.

    Árbol binario:
        Cada vértice tiene como máximo dos hijos (hijo izquierdo y derecho).

    Árbol binario de búsqueda (BST):
        Árbol binario donde, para cada nodo:
            Los valores de los nodos en el subárbol izquierdo son menores.
            Los valores en el subárbol derecho son mayores.

    Árbol AVL:
        Árbol binario de búsqueda equilibrado, donde la diferencia de altura entre los subárboles izquierdo y derecho de cualquier nodo es como máximo 1.

    Árbol B:
        Árbol autoequilibrado usado en bases de datos y sistemas de archivos. Permite múltiples claves por nodo.

Aplicaciones de los Árboles

    Ciencias de la computación:
        Representar jerarquías (sistemas de archivos, árboles de decisión).
        Árboles binarios de búsqueda (estructuras de datos eficientes para búsquedas, inserciones y eliminaciones).

    Redes y telecomunicaciones:
        Diseñar redes mínimas, como en el problema de generación de árboles de expansión mínimos.

    Inteligencia artificial:
        Árboles de decisión y árboles de juego para modelar decisiones y estrategias.

    Bases de datos:
        Estructuras de índices como árboles B o árboles AVL.

Algoritmos Relacionados con Árboles

    Recorridos:
        Preorden (raíz, izquierda, derecha).
        Inorden (izquierda, raíz, derecha).
        Postorden (izquierda, derecha, raíz).
        Por niveles (BFS).

    Construcción:
        Usar un grafo conexo para encontrar un árbol generador.

    Búsqueda:
        DFS y BFS adaptados a árboles.

    Equilibrado:
        Algoritmos para mantener árboles binarios equilibrados (como en árboles AVL).

Representación de Árboles

    Lista de adyacencia:
        Útil para árboles grandes y dispersos.

    Matriz de adyacencia:
        Eficiente para árboles pequeños, pero consume más espacio.

    Estructuras especializadas:
        Uso de estructuras como punteros o nodos enlazados.
        
            '''
        )
        self.ids.arbol_info1_label.text = textouniwi #asignamos el texto a la etiqueta

        textodosiwi=(
            '''
Árbol Binario

Un árbol binario es un tipo especial de árbol en el que cada nodo puede tener como máximo dos hijos. Los hijos suelen denominarse:

    Hijo izquierdo
    Hijo derecho

Características de un Árbol Binario

    Número máximo de nodos por nivel:
        En el nivel ii, puede haber como máximo 2i2i nodos.

    Número total máximo de nodos:
        En un árbol binario completo de altura hh, el número máximo de nodos es:
        2^(h+1)−1
        2^(h+1)−1

    Altura del árbol:
        La altura es el número máximo de niveles desde la raíz hasta la hoja más lejana.

    Balanceo:
        Los árboles binarios pueden estar equilibrados (los subárboles izquierdo y derecho tienen alturas similares) o desequilibrados (un subárbol es mucho más profundo que el otro).

Tipos de Árboles Binarios

    Árbol Binario Completo:
        Todos los niveles están completamente llenos excepto, posiblemente, el último, que está lleno de izquierda a derecha.

    Árbol Binario Perfecto:
        Todos los niveles están completamente llenos, incluido el último.

    Árbol Binario Degenerado:
        Cada nodo tiene como máximo un hijo. Se asemeja a una lista enlazada.

    Árbol Binario Equilibrado:
        La diferencia de altura entre los subárboles izquierdo y derecho de cada nodo es como máximo 1.

    Árbol Binario de Búsqueda (BST):
        Un árbol binario en el que:
            Los valores en el subárbol izquierdo son menores que la raíz.
            Los valores en el subárbol derecho son mayores que la raíz.

Árbol No Binario

Un árbol no binario (también llamado árbol general) es un árbol en el que cada nodo puede tener un número arbitrario de hijos (no está limitado a dos).
Características de un Árbol No Binario

    Número de hijos:
        Un nodo puede tener cero o más hijos sin restricciones.

    Estructura flexible:
        Es adecuado para representar estructuras como jerarquías o gráficos en los que cada nodo puede tener múltiples relaciones.

    Conversión a Árbol Binario:
        Un árbol no binario puede representarse como un árbol binario usando el método hijo izquierdo-hermano derecho:
            El primer hijo se convierte en el hijo izquierdo.
            Los hermanos del nodo se convierten en el hijo derecho del nodo anterior.

Ejemplos de Árboles No Binarios

    Árbol N-ario:
        Un árbol donde cada nodo tiene como máximo NN hijos.
        Ejemplo: Árbol ternario (máximo tres hijos por nodo).

    Árbol de decisiones:
        Cada nodo puede tener múltiples opciones o hijos que representan posibles resultados.

    Árbol de directorios:
        En un sistema de archivos, una carpeta puede contener múltiples subcarpetas y archivos.

            '''
        )
        self.ids.arbol_info2_label.text = textodosiwi   #asignamos el texto a la etiqueta
class AlgoritmosScreen(Screen): #creamos una clase para la pantalla de algoritmos
    def on_enter(self): #función que se ejecuta cuando se entra a la pantalla
        textouno=(
            '''
Un algoritmo es un conjunto de pasos o instrucciones bien definidas, organizadas y finitas que se siguen para resolver un problema o realizar una tarea específica. Es un concepto fundamental en matemáticas, ciencias de la computación y otras disciplinas, y sirve como base para el diseño de programas y sistemas.
Características principales de un algoritmo

    Finitud:
        Debe terminar después de un número finito de pasos.

    Claridad:
        Cada paso debe ser preciso, claro y no ambiguo.

    Entrada:
        Puede aceptar cero o más datos de entrada para procesar.

    Salida:
        Debe producir al menos un resultado o salida.

    Eficiencia:
        Debe realizarse en un tiempo razonable y con un uso óptimo de recursos.

    Determinismo:
        Dado un mismo conjunto de entradas, el algoritmo siempre debe producir el mismo resultado.



            '''
        )
        self.ids.algo_info1_label.text = textouno #asignamos el texto a la etiqueta

        textodos=(
            '''
    Algoritmos de búsqueda:
        Ejemplo: Búsqueda lineal, búsqueda binaria.

    Algoritmos de ordenación:
        Ejemplo: Ordenación por burbuja, ordenación rápida (QuickSort), MergeSort.

    Algoritmos de grafos:
        Ejemplo: DFS, BFS, Dijkstra, Kruskal.

    Algoritmos recursivos:
        Utilizan la técnica de dividir el problema en subproblemas más pequeños.
        Ejemplo: Factorial, Fibonacci.

    Algoritmos probabilísticos:
        Utilizan elementos aleatorios para obtener una solución aproximada.
        Ejemplo: Monte Carlo.

    Algoritmos voraces (Greedy):
        Tomar decisiones óptimas locales para encontrar una solución global.
        Ejemplo: Problema del cambio mínimo, Prim.

    Algoritmos dinámicos:
        Dividen el problema en subproblemas solapados y almacenan sus soluciones.
        Ejemplo: Mochila, cadena de matrices.
            
            '''
        )
        self.ids.algo_info2_label.text = textodos #asignamos el texto a la etiqueta


        textotres=(
            '''
Tipos de Algoritmos de Búsqueda

Los algoritmos de búsqueda se pueden clasificar en función del tipo de estructura de datos sobre la que trabajan y la estrategia que utilizan:
1. Búsqueda en estructuras lineales

    Operan sobre arreglos, listas o secuencias.

    Búsqueda Lineal:
        Recorre los elementos uno por uno hasta encontrar el deseado o llegar al final de la lista.
        Complejidad: O(n).
        Ventaja: Simple, no requiere que los datos estén ordenados.
        Desventaja: Poco eficiente para listas grandes.

    Búsqueda Binaria:
        Requiere que los datos estén ordenados.
        Divide la colección en mitades sucesivas para reducir el rango de búsqueda.
        Complejidad: O(log⁡n).
        Ventaja: Muy eficiente para grandes conjuntos de datos ordenados.
        Desventaja: Requiere datos previamente ordenados.

2. Búsqueda en estructuras jerárquicas

    Diseñados para trabajar con árboles y grafos.

    Búsqueda en profundidad (DFS):
        Explora los caminos de un grafo o árbol lo más profundo posible antes de retroceder.
        Complejidad: O(V+E), donde V son los vértices y EE las aristas.

    Búsqueda en amplitud (BFS):
        Explora todos los nodos de un nivel antes de pasar al siguiente.
        Complejidad: O(V+E).
        '''
        )
        self.ids.algo_info3_label.text = textotres #asignamos el texto a la etiqueta



class BolitaScreen(Screen): #Clase para la pantalla de la bolita
    class CanvasExample5(Widget): #Clase para el widget del canvas
        ball_color = ListProperty([1, 0, 0, 1])  # Initial color (red)


        def __init__(self, **kwargs): #Constructor de la clase
            super().__init__(**kwargs) #Llamada al constructor de la clase padre
            self.ball_size = dp(50) #Tamaño de la bolita
            self.vx = dp(3) #Velocidad horizontal
            self.vy = dp(4) #Velocidad vertical
            with self.canvas: #Canvas para dibujar la bolita

                self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size)) #Dibuja la bolita
                self.color = Color(*self.ball_color)  # Set initial color
                self.canvas.before.add(self.color)  # Add color to canvas

            Clock.schedule_interval(self.update, 1/60) #Actualiza la posición de la bolita cada 1/60 segundos

        def on_size(self, *args): #Método para cambiar el tamaño de la bolita
            self.ball.pos = (self.center_x - (self.ball_size / 2), self.center_y - (self.ball_size / 2)) #Posiciona la bolita en el centro

        def update(self, dt): #Método para actualizar la posición de la bolita
            x, y = self.ball.pos #Obtiene la posición de la bolita
            x += self.vx #Actualiza la posición horizontal
            y += self.vy #Actualiza la posición vertical

            if y + self.ball_size > self.height or y < 0: #Si la bolita llega al borde de la pantalla
                self.vy = -self.vy #Reversa la velocidad vertical
                self.change_color()  # Change color on vertical bounce


            if x + self.ball_size > self.width or x < 0: #Si la bolita llega al borde de la pantalla
                self.vx = -self.vx #Reversa la velocidad horizontal
                self.change_color()  # Change color on horizontal bounce


            self.ball.pos = (x, y) #Actualiza la posición de la bolita


        def change_color(self): #Método para cambiar el color de la bolita
            # Generate a random color
            self.ball_color = [random.random() for _ in range(3)] + [1]  # RGB + Alpha
            self.color.rgba = self.ball_color  # Update the color in the canvas

class ConjuntosScreen(Screen): #Clase para la pantalla de los conjuntos
    def on_enter(self): #Método para ejecutar cuando se entra a la pantalla
 
        # Definir el texto que deseas mostrar en el Label

        texto = (

            "Diagramas de Venn\n\n"

            "Un diagrama de Venn es una representación gráfica utilizada para mostrar las relaciones entre conjuntos. "

            "Consiste en círculos (u otras figuras geométricas) que se superponen dentro de un rectángulo que representa "

            "el universo de todos los elementos posibles.\n\n"

            "Características principales de los diagramas de Venn:\n\n"

            "    Elementos visuales:\n"

            "        Círculos o regiones: Cada conjunto está representado por un círculo.\n"

            "        Regiones de intersección: Áreas donde los círculos se superponen, que representan elementos comunes.\n"

            "        Región externa: Espacio fuera de los círculos, que corresponde a elementos que no están en los conjuntos.\n\n"

            "    Representaciones comunes:\n"

            "        Dos conjuntos (A y B):\n"

            "            Unión (A∪B): Toda el área cubierta por los círculos de A y B.\n"

            "            Intersección (A∩B): La región donde los círculos se superponen.\n"

            "            Diferencia (A−B): La parte del círculo de A que no se solapa con B.\n"

            "        Tres conjuntos (A, B y C):\n"

            "            Las áreas pueden representar combinaciones más complejas, como A∩B∩C o A∪B−C."

        )

        # Asignar el texto al Label usando su ID

        self.ids.info_label.text = texto #Asignar el texto al Label

    resultado = StringProperty("") #Variable para almacenar el resultado

    def calcular_union(self): #Método para calcular la unión de dos conjuntos
        universo = self.obtener_conjunto(self.ids.input_universo.text) #Obtener el conjunto del universo
        conjunto_a = self.obtener_conjunto(self.ids.input_a.text) #Obtener el conjunto A
        conjunto_b = self.obtener_conjunto(self.ids.input_b.text) #Obtener el conjunto B

        if not conjunto_a.issubset(universo) or not conjunto_b.issubset(universo): #Verificar si los conjuntos están dentro del universo
            self.ids.resultado.text = "Error: Los elementos de A o B no están en el universo." #Mostrar error
            return #Salir del método

        union = conjunto_a.union(conjunto_b) #Calcular la unión de A y B
        self.ids.resultado.text = f"Unión: {', '.join(union)}" #Mostrar el resultado

    def calcular_interseccion(self):    #Método para calcular la intersección de dos conjuntos
        universo = self.obtener_conjunto(self.ids.input_universo.text) #Obtener el conjunto del universo
        conjunto_a = self.obtener_conjunto(self.ids.input_a.text) #Obtener el conjunto A
        conjunto_b = self.obtener_conjunto(self.ids.input_b.text) #Obtener el conjunto B

        if not conjunto_a.issubset(universo) or not conjunto_b.issubset(universo): #Verificar si los conjuntos están dentro del universo
            self.ids.resultado.text = "Error: Los elementos de A o B no están en el universo." #Mostrar error
            return #Salir del método

        interseccion = conjunto_a.intersection(conjunto_b) #Calcular la intersección de A y B
        self.ids.resultado.text = f"Intersección: {', '.join(interseccion)}" #Mostrar el resultado

    def calcular_complemento_general(self): #Método para calcular el complemento general de un conjunto
        universo = self.obtener_conjunto(self.ids.input_universo.text) #Obtener el conjunto del universo
        conjunto_a = self.obtener_conjunto(self.ids.input_a.text) #Obtener el conjunto A
        conjunto_b = self.obtener_conjunto(self.ids.input_b.text) #Obtener el conjunto B

        complemento_general = universo.difference(conjunto_a.union(conjunto_b)) #Calcular el complemento general de A y B
        self.ids.resultado.text = f"Complemento General: {', '.join(complemento_general)}" #Mostrar el resultado

    def calcular_complemento_individual(self, conjunto): #Método para calcular el complemento individual de un conjunto
        universo = self.obtener_conjunto(self.ids.input_universo.text) #Obtener el conjunto del universo
        conjunto_a = self.obtener_conjunto(self.ids.input_a.text) #Obtener el conjunto A
        conjunto_b = self.obtener_conjunto(self.ids.input_b.text) #Obtener el conjunto B

        if conjunto == 'A': #Verificar si el conjunto es A
           complemento = universo.difference(conjunto_a) #Calcular el complemento de A
        elif conjunto == 'B': #Verificar si el conjunto es B
           complemento = universo.difference(conjunto_b) #Calcular el complemento de B
        else: #Verificar
            self.ids.resultado.text = "Error: Selecciona un conjunto válido." #Mostrar error
            return #Salir del método

        self.ids.resultado.text = f"Complemento: {', '.join(complemento)}" #Mostrar el resultado

    def calcular_diferencia_simetrica(self): #Método para calcular la diferencia simétrica de dos conjuntos
        universo = self.obtener_conjunto(self.ids.input_universo.text) #Obtener el conjunto del universo
        conjunto_a = self.obtener_conjunto(self.ids.input_a.text) #Obtener el conjunto A
        conjunto_b = self.obtener_conjunto(self.ids.input_b.text) #Obtener el conjunto B

        if not conjunto_a.issubset(universo) or not conjunto_b.issubset(universo): #Verificar si los conjuntos está dentro del universo
            self.ids.resultado.text = "Error: Los elementos de A o B no están en el universo." #Mostrar error
            return #Salir del método

    def obtener_conjunto(self, texto): #Método para obtener un conjunto a partir de un texto
        elementos = map(str.strip, texto.split(',')) #Obtener los elementos del conjunto
        return set(elementos) #Devolver el conjunto


    def mostrar_resultado(self, resultado): #Método para mostrar el resultado en el Label
        self.ids.resultado.text = resultado #Mostrar el resultado

    def generar_venn(self, conjunto_a, conjunto_b, resultado, operacion): #Método para generar el diagrama de Venn
        plt.figure() #Crear una figura
        venn2([conjunto_a, conjunto_b], ('Conjunto A', 'Conjunto B')) #Crear el diagrama de Venn
        plt.title(f'Diagrama de Venn - {operacion}') #Establecer el título del diagrama de Venn
        plt.savefig('venn_diagram.png') #Guardar el diagrama de Venn como imagen
        plt.close() #Cerrar la figura
        self.ids.venn_image.source = 'venn_diagram.png' #Mostrar la imagen en el Label
        self.ids.venn_image.reload() #Recargar la imagen



class PapuApp(App): #Clase para la aplicación
    def build(self): #Método para construir la aplicación
        sm = ScreenManager() #Crear el manager de pantallas
        sm.add_widget(MainScreen(name='main')) #Agregar la pantalla principal
        sm.add_widget(TopicsScreen(name='topics')) #Agregar la pantalla de temas
        sm.add_widget(BolitaScreen(name='Bolita')) #Agregar la pantalla de bolita
        return sm #Devolver el manager de pantallas
    
if __name__ == '__main__': #Verificar si se ejecuta el archivo directamente
    PapuApp().run() #Ejecutar la aplicación