from tkinter import *
from tkinter import messagebox
from controller.funciones import FuncionesController
from model.nota import Nota

class vista:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Calculadora Básica")
        ventana.geometry("600x500")
        ventana.resizable(False, False)

        ventana.vista = self

        self.interfaz_principal()

    # -------------------------------------------------------
    # BORRAR PANTALLA
    # -------------------------------------------------------
    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    # -------------------------------------------------------
    # MENÚ PRINCIPAL
    # -------------------------------------------------------
    @staticmethod
    def menuPrincipal(ventana):
        menuBar = Menu(ventana)
        ventana.config(menu=menuBar)

        operacionesMenu = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Operaciones", menu=operacionesMenu)

        operacionesMenu.add_command(label="Agregar", command=lambda: ventana.vista.interfaz_principal())
        operacionesMenu.add_command(label="Consultar", command=ventana.vista.consultar)
        operacionesMenu.add_command(label="Borrar", command=ventana.vista.eliminar)
        operacionesMenu.add_command(label="Cambiar", command=ventana.vista.cambiar)
        operacionesMenu.add_separator()
        operacionesMenu.add_command(label="Salir", command=ventana.quit)

    # -------------------------------------------------------
    # PANTALLA PRINCIPAL (AGREGAR)
    # -------------------------------------------------------
    def interfaz_principal(self):
        vista.borrarPantalla(self.ventana)
        vista.menuPrincipal(self.ventana)

        self.n1 = StringVar()
        self.n2 = StringVar()

        Label(self.ventana, text="Número 1:", font=("Arial", 12)).pack(pady=5)
        Entry(self.ventana, textvariable=self.n1, font=("Arial", 12), width=20).pack(pady=5)

        Label(self.ventana, text="Número 2:", font=("Arial", 12)).pack(pady=5)
        Entry(self.ventana, textvariable=self.n2, font=("Arial", 12), width=20).pack(pady=5)

        frame_botones = Frame(self.ventana)
        frame_botones.pack(pady=30)

        Button(frame_botones, text="Suma", width=12, command=self.suma).pack(side=LEFT, padx=5)
        Button(frame_botones, text="Resta", width=12, command=self.resta).pack(side=LEFT, padx=5)
        Button(frame_botones, text="Multiplicación", width=12, command=self.multiplicacion).pack(side=LEFT, padx=5)
        Button(frame_botones, text="División", width=12, command=self.division).pack(side=LEFT, padx=5)

        Button(self.ventana, text="Salir", width=10,
               command=self.ventana.quit).pack(pady=20)

    # -------------------------------------------------------
    # OPERACIONES
    # -------------------------------------------------------
    def suma(self):
        FuncionesController.calcular("suma", self.n1.get(), self.n2.get())

    def resta(self):
        FuncionesController.calcular("resta", self.n1.get(), self.n2.get())

    def multiplicacion(self):
        FuncionesController.calcular("multiplicacion", self.n1.get(), self.n2.get())

    def division(self):
        FuncionesController.calcular("division", self.n1.get(), self.n2.get())

    # -------------------------------------------------------
    # CONSULTAR
    # -------------------------------------------------------
    def consultar(self):
        vista.borrarPantalla(self.ventana)
        vista.menuPrincipal(self.ventana)

        Label(self.ventana, text="Calculadora Básica",
              font=("Arial", 16, "bold")).pack(pady=10)

        Label(self.ventana, text="::. Listado de las Operaciones .::",
              font=("Arial", 12)).pack(pady=10)

        operaciones = Nota.consultarTodo()

        if not operaciones:
            Label(self.ventana, text="No hay operaciones registradas.",
                  font=("Arial", 12)).pack(pady=10)
        else:
            for op in operaciones:
                texto = f"ID: {op[0]} | Fecha: {op[1]}\nOperación: {op[2]}"
                Label(self.ventana, text=texto, font=("Arial", 11),
                      justify="center").pack(pady=8)

        Button(self.ventana, text="Volver", width=12,
               command=self.interfaz_principal).pack(pady=20)

    # -------------------------------------------------------
    # ELIMINAR
    # -------------------------------------------------------
    def eliminar(self):
        vista.borrarPantalla(self.ventana)
        vista.menuPrincipal(self.ventana)

        Label(self.ventana, text="Borrar una operación",
              font=("Arial", 14, "bold")).pack(pady=10)

        Label(self.ventana, text="ID de la operación:", font=("Arial", 12)).pack(pady=5)

        id_var = StringVar()
        Entry(self.ventana, textvariable=id_var, font=("Arial", 12), width=10).pack(pady=5)

        def procesar_eliminacion():
            try:
                id_op = int(id_var.get())
                eliminado = Nota.eliminar(id_op)
                if eliminado:
                    messagebox.showinfo("Éxito", "Operación eliminada correctamente.")
                else:
                    messagebox.showerror("Error", "No existe una operación con ese ID.")
            except:
                messagebox.showerror("Error", "Ingrese un ID válido.")

        Button(self.ventana, text="Eliminar", width=12,
               command=procesar_eliminacion).pack(pady=10)

        Button(self.ventana, text="Volver", width=12,
               command=self.interfaz_principal).pack(pady=10)

    # -------------------------------------------------------
    # CAMBIAR OPERACIÓN
    # -------------------------------------------------------
    def cambiar(self):
        vista.borrarPantalla(self.ventana)
        vista.menuPrincipal(self.ventana)

        Label(self.ventana, text="Calculadora Básica",
              font=("Arial", 16, "bold")).pack(pady=10)

        Label(self.ventana, text="::. Cambiar una Operación .::",
              font=("Arial", 12)).pack(pady=10)

        # Variables
        id_var = StringVar()
        n1_var = StringVar()
        n2_var = StringVar()
        signo_var = StringVar()
        res_var = StringVar()

        Label(self.ventana, text="ID de la Operación:", font=("Arial", 12)).pack()
        Entry(self.ventana, textvariable=id_var, width=10).pack(pady=5)

        Label(self.ventana, text="Nuevo Número 1:", font=("Arial", 12)).pack()
        Entry(self.ventana, textvariable=n1_var, width=20).pack(pady=5)

        Label(self.ventana, text="Nuevo Número 2:", font=("Arial", 12)).pack()
        Entry(self.ventana, textvariable=n2_var, width=20).pack(pady=5)

        Label(self.ventana, text="Nuevo Signo:", font=("Arial", 12)).pack()
        Entry(self.ventana, textvariable=signo_var, width=20).pack(pady=5)

        Label(self.ventana, text="Nuevo Resultado:", font=("Arial", 12)).pack()
        Entry(self.ventana, textvariable=res_var, width=20).pack(pady=5)

        def guardar_cambio():
            try:
                id_op = int(id_var.get())
                n1 = float(n1_var.get())
                n2 = float(n2_var.get())
                signo = signo_var.get()
                resultado = float(res_var.get())

                actualizado = Nota.actualizar(id_op, n1, n2, signo, resultado)

                if actualizado:
                    messagebox.showinfo("Éxito", "Operación actualizada correctamente.")
                else:
                    messagebox.showerror("Error", "No existe una operación con ese ID.")

            except Exception as e:
                messagebox.showerror("Error", f"Datos inválidos: {e}")

        Button(self.ventana, text="Guardar", width=15,
               command=guardar_cambio).pack(pady=10)

        Button(self.ventana, text="Volver", width=15,
               command=self.interfaz_principal).pack(pady=10)
