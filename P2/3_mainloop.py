from tkinter import *

ventana=Tk()

ventana.title("MAINLOOP")
ventana.geometry("800x600")
ventana.resizable(False,False)

marco=Frame(ventana,width=600,height=400,bg="#7F1392",border=2,relief=RAISED)
marco.pack(padx=50,pady=50)


#LAS 2 FORMAS DE IGUAL MANERA FUNCIONAN
"""
marco=Frame(ventana)
marco.config(
    bg="#652FA2",
    bd=10,
    width=400,
    height=200
    relief=RAISED
)
marco.pack(
    side=BOTTOM,
    anchor=SW
)"""


ventana.mainloop()