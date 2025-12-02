from tkinter import *
from tkinter import messagebox


class View:
    @staticmethod
    def borrar(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def titulo(ventana, text):
        Label(ventana, text=text, justify="center").pack(pady=15)

    @staticmethod
    def boton(ventana, text, cmd):
        Button(ventana, text=text, command=cmd).pack(pady=10)

    @staticmethod
    def menu_inicial(ventana, titulo, opciones, volver=None):
        """
        opciones = [(texto_boton, funcion), ...]
        """
        View.borrar(ventana)
        View.titulo(ventana, titulo)

        for texto, funcion in opciones:
            View.boton(ventana, texto, funcion)

        if volver:
            View.boton(ventana, "Regresar", volver)

    def __init__(self, ventana):
        ventana.title("..: Coches System :..")
        ventana.geometry("800x700")
        ventana.resizable(False, False)
        View.menu_principal(ventana)

    @staticmethod
    def menu_principal(ventana):
        View.menu_inicial(
            ventana,
            "..:: Menú Principal ::..",
            [
                ("1.- Autos",  lambda: View.menu_autos(ventana)),
                ("2.- Camionetas", lambda: View.menu_camionetas(ventana, "Camionetas")),
                ("3.- Camiones", lambda: View.menu_camiones(ventana, "Camiones")),
                ("4.- Salir", ventana.quit)
            ]
        )

    @staticmethod
    def menu_autos(ventana):
        View.menu_inicial(
            ventana,
            "..:: Menú Autos ::..",
            [
                ("1.- Insertar", lambda: View.auto_registro(ventana)),
                ("2.- Consultar", lambda: View.auto_consultar(ventana)),
                ("3.- Actualizar", lambda: View.auto_id(ventana, "cambiar")),
                ("4.- Eliminar", lambda: View.auto_id(ventana, "eliminar")),
            ],
            lambda: View.menu_principal(ventana)
        )

    @staticmethod
    def menu_camionetas(ventana, tipo):
        View.menu_inicial(
            ventana,
            f"..:: Menú {tipo} ::..",
            [
                ("1.- Insertar", lambda: View.insertar_camioneta(ventana)),
                ("2.- Consultar", lambda: View.auto_consultar(ventana)),
                ("3.- Actualizar", lambda: View.auto_id(ventana, "cambiar")),
                ("4.- Eliminar", lambda: View.auto_id(ventana, "eliminar")),
            ],
            lambda: View.menu_principal(ventana)
        )

    @staticmethod
    def menu_camiones(ventana, tipo):
        View.menu_inicial(
            ventana,
            f"..:: Menú {tipo} ::..",
            [
                ("1.- Insertar", lambda: View.insertar_camiones(ventana)),
                ("2.- Consultar", lambda: View.auto_consultar(ventana)),
                ("3.- Actualizar", lambda: View.auto_id(ventana, "cambiar")),
                ("4.- Eliminar", lambda: View.auto_id(ventana, "eliminar")),
            ],
            lambda: View.menu_principal(ventana)
        )

    @staticmethod
    def auto_registro(ventana):
        View.borrar(ventana)
        View.titulo(ventana, "...: Registro de Autos :...")

        campos = ["Marca", "Color", "Modelo", "Velocidad", "Potencia", "Nro Plazas"]
        entradas = {}

        for c in campos:
            Label(ventana, text=f"{c}: ").pack()
            e = Entry(ventana)
            e.pack()
            entradas[c] = e

        def guardar():
            messagebox.showinfo("Guardar", "Registro correcto")
            View.menu_autos(ventana)

        View.boton(ventana, "Guardar", guardar)
        View.boton(ventana, "Volver", lambda: View.menu_autos(ventana))

        list(entradas.values())[0].focus()

    @staticmethod
    def insertar_camiones(ventana):
        View.borrar(ventana)
        View.titulo(ventana, "...: Registro de Camiones :...")

        campos = ["Marca", "Color", "Modelo", "Velocidad", "Potencia", "Nro Plazas", "#Ejes","Capacidad de Carga"]
        entradas = {}

        for c in campos:
            Label(ventana, text=f"{c}: ").pack()
            e = Entry(ventana)
            e.pack()
            entradas[c] = e

        def guardar():
            messagebox.showinfo("Guardar", "Registro correcto")
            View.menu_autos(ventana)

        View.boton(ventana, "Guardar", guardar)
        View.boton(ventana, "Volver", lambda: View.menu_autos(ventana))

        list(entradas.values())[0].focus()

    @staticmethod
    def insertar_camioneta(ventana):
        View.borrar(ventana)
        View.titulo(ventana, "...: Registro de Camionetas :...")
        campos=["Marca","Color","Modelo","Velocidad","Potencia","Caballaje","Nro Plazas","Tracción","Cerrada"]
        entradas={}
        for c in campos:
            Label(ventana,text=f"{c}: ").pack()
            e=Entry(ventana)
            e.pack()
            entradas[c]=e

            def guardar():
                messagebox.showinfo("Guardar", "Registro correcto")
                View.menu_autos(ventana)

        View.boton(ventana, "Guardar", guardar)
        View.boton(ventana, "Volver", lambda: View.menu_autos(ventana))

        list(entradas.values())[0].focus()
            
    @staticmethod
    def auto_consultar(ventana):
        View.borrar(ventana)
        View.titulo(ventana, "...: Consulta de Autos :...")

        txt = Text(ventana, height=20, width=80)
        txt.pack(pady=10)

        datos = "No hay datos registrados (de momento)"
        txt.insert(END, datos)
        txt.config(state=DISABLED)

        View.boton(ventana, "Volver", lambda: View.menu_autos(ventana))

    @staticmethod
    def auto_id(ventana, tipo):
        View.borrar(ventana)
        View.titulo(ventana, "...: Ingresa ID del Auto :...")

        var = IntVar()
        txt = Entry(ventana, textvariable=var, justify="center", width=8)
        txt.pack(pady=10)
        txt.focus()

        if tipo == "cambiar":
            View.boton(ventana, "Buscar", lambda: View.cambiar_auto(ventana, var.get()))
        else:
            View.boton(ventana, "Buscar", lambda: View.eliminar_auto(ventana, var.get()))

        View.boton(ventana, "Volver", lambda: View.menu_autos(ventana))

    @staticmethod
    def cambiar_auto(ventana, id):
        View.borrar(ventana)
        View.titulo(ventana, f"...: Modificación Auto {id} :...")

        campos = ["Marca", "Color", "Modelo", "Velocidad", "Potencia", "Nro Plazas"]
        entradas = {}

        for c in campos:
            Label(ventana, text=f"Nuevo {c}: ").pack()
            e = Entry(ventana)
            e.pack()
            entradas[c] = e

        def guardar():
            messagebox.showinfo("Guardar", f"Auto {id} modificado correctamente")
            View.menu_autos(ventana)

        View.boton(ventana, "Guardar", guardar)
        View.boton(ventana, "Volver", lambda: View.menu_autos(ventana))

        list(entradas.values())[0].focus()

    @staticmethod
    def eliminar_auto(ventana, id):
        View.borrar(ventana)
        View.titulo(ventana, f"...: Eliminar Auto {id} :...")

        def borrar():
            messagebox.showinfo("Eliminar", f"Auto {id} eliminado correctamente")
            View.menu_autos(ventana)

        View.boton(ventana, "Eliminar", borrar)
        View.boton(ventana, "Volver", lambda: View.menu_autos(ventana))
