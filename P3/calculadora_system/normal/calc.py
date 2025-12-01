"""
Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las operaciones
3.- Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox


def calcular(operacion, n1, n2):
        if operacion == "suma":
            resultado = n1 + n2
            mensaje = f"{n1} + {n2} = {resultado}"
        elif operacion == "resta":
            resultado = n1 - n2
            mensaje = f"{n1} - {n2} = {resultado}"
        elif operacion == "multiplicacion":
            resultado = n1 * n2
            mensaje = f"{n1} x {n2} = {resultado}"
        elif operacion == "division":
            resultado = n1 / n2
            mensaje = f"{n1} / {n2} = {resultado}"


        return messagebox.showinfo("Resultado", mensaje)


########
def mensaje(n1,n2,operacion,signo,tipo_ope):
     messagebox.showinfo(title=tipo_ope,icon="info",message=f"{n1} {signo} {n2} = {operacion}")


ventana = Tk()
ventana.geometry("600x400")
ventana.title("Calculadora")
ventana.resizable(False, False)
n1 = IntVar()
n2 = IntVar()
Label(ventana, text="Número 1:").pack()
valor1 = Entry(ventana, textvariable=n1)
valor1.pack()
Label(ventana, text="Número 2:").pack()
valor2 = Entry(ventana, textvariable=n2)
valor2.pack()


Button(ventana, text="Suma", command=lambda: calcular("suma", n1.get(), n2.get())).pack()
Button(ventana, text="Resta", command=lambda: calcular("resta", n1.get(), n2.get())).pack()
Button(ventana, text="Multiplicación", command=lambda: calcular("multiplicacion", n1.get(), n2.get())).pack()
Button(ventana, text="División", command=lambda: calcular("division", n1.get(), n2.get())).pack()
Button(ventana, text="Salir", command=ventana.quit).pack()


ventana.mainloop()

