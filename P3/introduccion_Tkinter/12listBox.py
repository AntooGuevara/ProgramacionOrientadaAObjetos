from tkinter import *

ventana=Tk()

ventana.title("List Box")
ventana.geometry("500x500")

def mostrarValor():
    resultado.config(text=f"Valor seleccionado: {lista.get(ACTIVE)}")

lista=Listbox(ventana, width=50, height=5, selectmode=SINGLE)
lista.pack()
opciones = ["Azul", "Rojo", "Negro", "Amarillo"]
for i in opciones:
    lista.insert(END, i)


boton= Button(ventana, text="Mostrar seleccion", command=mostrarValor)
boton.pack()

resultado = Label(ventana, text="")
resultado.pack()

ventana.mainloop()