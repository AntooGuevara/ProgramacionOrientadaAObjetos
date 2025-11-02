from tkinter import *

ventana=Tk()

ventana.title("USO DE FRAME/MARCO")
ventana.geometry("800x600")

#marcos o frames


marco=Frame(ventana, width=300,height=200,bg="blue",borderwidth=2,relief=SOLID)
marco.pack_propagate(False)
marco.pack(pady="150")

marco2=Frame(marco,width=200,height=100,bg="red",border=2,relief=SOLID).pack(padx=50,pady=50)


ventana.mainloop()