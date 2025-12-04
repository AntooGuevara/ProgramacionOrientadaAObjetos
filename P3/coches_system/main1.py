from tkinter import *
from view.view_1 import View  # importar la clase, no el módulo

if __name__ == "__main__":
    ventana = Tk()
    View(ventana)   # ✔️ ahora sí
    ventana.mainloop()
