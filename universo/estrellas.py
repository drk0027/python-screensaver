import tkinter as tk
import random

CANTIDAD_ESTRELLAS = 2
VELOCIDAD_RADIO=SPEED_GEARS = [i/10.0 for i in range(-10,-2)]+[i/10.0 for i in range(2,10)]
RADIO=25
COLOR_ESTRELLA = "yellow"



class componentes:
    def __init__(self, padre):
       self.padre = padre
       self.comenzar_movimiento()
       self.crear_circulo_pequeño()
    
    def comenzar_movimiento(self):
        self.x1 = self.padre.winfo_width()/2
        self.y1 = self.padre.winfo_height()/2
        self.velocity_x = random.choice(VELOCIDAD_RADIO)
        self.velocity_y = random.choice(VELOCIDAD_RADIO)
        return

    def crear_circulo_pequeño(self):
        x1=self.x1
        y1=self.y1
        x2,y2=x1+RADIO, y1+RADIO
        self.estrella = self.padre.create_oval(x1,y1,x2,y2, fill=COLOR_ESTRELLA)
        return

    def parar_movimiento(self):
        self.padre.coords(self.estrella, self.x1,self.y1,self.x1+RADIO,self.y1+RADIO)
        self.comenzar_movimiento()
        return

    def actualizar(self):
        self.padre.move(self.estrella, self.velocity_x, self.velocity_y)
        x,y = self.padre.coords(self.estrella)[:2]
        if x<0 or x>1500:
            self.parar_movimiento()
        elif y<0 or y>1000:
            self.parar_movimiento()
        return