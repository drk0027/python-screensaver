#Importar los componentes necesarios
import tkinter as tk

#Importar los componentes que contienen las clases que hemos creado
import universo.estrellas

#Crear una variable globlal para la cantidad de estrellas en pantalla.
CANTIDAD_ESTRELLAS = 2

# Definir la clase componentes
class componentes(tk.Canvas):
    # Definir la clase inicial, que recibira los parametros desde donde sea inicializada.
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs) # Crear un objeto tkinter con los parametros iniciales
        self.estrellas = [] # Establecer un arreglo de «estrellas» obtenidas de la clase «universo.estrellas.componentes»
        self.crear_estrellas() # Llamar a funcion crear_estrellas() al inicializar la clase

    # Funcion para crear estrellas
    def crear_estrellas(self):
        for i in range(CANTIDAD_ESTRELLAS): # Crea un arreglo de instancias de universo.estrellas.componentes de acuerdo a la cantidad definida en la variable CANTIDAD_ESTRELLAS
            self.estrellas.append(universo.estrellas.componentes(self))
        return

    #Funcion para actualizar la posicion de las estrellas en el cielo
    def actualizar_pantalla(self):
        for i in self.estrellas:
            i.actualizar()
        return

