# Importar los componentes necesarios
import tkinter as tk
import time
import random

#importar los componentes que contienen las clases que hemos creado
import universo.cielo

#Definir variables globales
COLOR_FONDO="black" #Establecer la variable que define el atributo del color del cielo
NIVEL_TRANSPARENCIA=1
EVENTOS_DE_CIERRE = ['<Any-KeyPress>', '<Any-Button>'] #Se puede crear un arreglo de eventos para inicializarlos todos de una vez


def main():
    raiz=tk.Tk()#Establecer la ventana raiz o inicial

    pantalla=universo.cielo.componentes(raiz,bg=COLOR_FONDO) #crear la ventana, utilizando la clase «cielo» como lienzo donde se dibujaran los componentes
    pantalla.pack(expand="yes",fill="both") #agrega los componentes en el lienzo
    
    raiz.wait_visibility(pantalla) #Se espera a que la ventana sea construida para cargar los componentes
    raiz.wm_attributes('-alpha',NIVEL_TRANSPARENCIA) #Se agrega el atributo de transparencia a la ventana
    raiz.wm_attributes("-topmost", True) #Se agrega el atributo «por encima de todo» a la ventana
    raiz.overrideredirect(1) #Evita redimensionar la ventana
    raiz.state('zoomed') #Inicia la ventana en estado "maximizado"

    #Esta funcion permite terminar el programa al ser disparada por los eventos definidos en la variable EVENTOS_DE_CIERRE
    def salir(event):
        raiz.destroy()
        return
    
    #Permite vincular la ventana a la lista de eventos definidos en la variable «EVENTOS_DE_CIERRE»
    for seq in EVENTOS_DE_CIERRE:
        raiz.bind_all(seq, salir)

    while True:
        raiz.update() #Actualiza la ventana
        raiz.update_idletasks() #Actualiza la ventana si no hay actividad
        pantalla.actualizar_pantalla() #Recarga la ventana mediante la clase cielo

#establecemos la funcion main como arranque al iniciar el script
if __name__ == '__main__':
 main()