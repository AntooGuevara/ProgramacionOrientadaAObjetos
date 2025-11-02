from tkinter import *

##EJERCICIO DONDE TENGAMOS NOMBRE, CONTRASEÑA, Y CUANDO SE LE DE A ACEPTAR DIGA "INICIASTE SESION"

def cambiarTexto():
    mensajeCambiante.config(text="hola crayola")

def regresarTexto():
    mensajeCambiante.config(text="Texto original")

ventana=Tk()

ventana.geometry("800x600")
ventana.title("USO DE BOTONES")
frame_principal=Frame(ventana)
frame_principal.config(
    bg="#871010",
    width=800,
    height=50,
    border=2,
    relief=GROOVE
)
frame_principal.pack(pady=10)
frame_principal.pack_propagate(False)
lbl_titulo=Label(frame_principal,text="USO DE BOTONES") #LABEL Y LBL ES LO MISMO
lbl_titulo.config(
    bg="#871010",
    width=20
)
lbl_titulo.pack(pady=10)

mensajeCambiante=Label(ventana,text="Texto original")
mensajeCambiante.pack()

boton_cambiar=Button(ventana,text="Cambiar texto",command=cambiarTexto)
boton_cambiar.pack()

boton_regresar=Button(ventana,text="Regresar texto",command=regresarTexto)
boton_regresar.pack()


ventana.mainloop()



