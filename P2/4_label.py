from tkinter import *

ventana=Tk()
ventana.geometry("800x600")
ventana.title("LABEL")

#ETIQUETA O LABEL

etiqueta1=Label(ventana,text="Nombre de la persona").pack()

marco1=Frame(ventana,width=200,height=200,bg="#7C1E50")
marco1.pack_propagate(False)
marco1.pack()
marco1=Frame(marco1,width=150,height=150,bg="#189016").pack()

etiqueta2=Label(marco1,text="Soy una etiqueta dentro de un marco").pack()

ventana.mainloop()