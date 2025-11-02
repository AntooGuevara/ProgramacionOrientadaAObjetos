"""
Tkinter trabaja a traves de interfaces, es una biblioteca de Python que permite crear aplicaciones en python para escritorio
"""

#from  tkinter import*

import tkinter as tk 

ventana=tk.Tk()

ventana.title() 
ventana.title("Mi primer app grafica en Tkinter con Pyhton")
ventana.geometry("800x600")
ventana.resizable(False,False) #Metodo para redimensionar el tamaño de la pantalla
ventana.mainloop() #Metodo que permite tener la ventana abierta e interactuar con ella
