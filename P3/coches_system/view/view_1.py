from tkinter import *
from tkinter import messagebox
from controller.controlador_1 import Controlador

class View:

    @staticmethod
    def borrar(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def titulo(ventana, text):
        Label(ventana, text=text, justify="center", font=("Arial", 14, "bold")).pack(pady=15)

    @staticmethod
    def boton(ventana, text, cmd):
        Button(ventana, text=text, width=20, command=cmd).pack(pady=6)

    @staticmethod
    def formulario_generico(ventana, titulo, campos, guardar_cmd, volver_cmd):

        View.borrar(ventana)
        View.titulo(ventana, titulo)

        entradas = {}

        frame = Frame(ventana)
        frame.pack(pady=10)

        for c in campos:
            Label(frame, text=f"{c}: ").pack()
            e = Entry(frame)
            e.pack()
            entradas[c] = e

        def guardar():
            datos = {c: entradas[c].get() for c in campos}
            guardar_cmd(datos)

        View.boton(ventana, "Guardar", guardar)
        View.boton(ventana, "Volver", volver_cmd)

    @staticmethod
    def pedir_id(ventana, titulo, aceptar_cmd, volver_cmd):

        View.borrar(ventana)
        View.titulo(ventana, titulo)

        var = IntVar()

        Entry(ventana, textvariable=var, justify="center", width=8).pack(pady=10)

        def enviar():
            aceptar_cmd(var.get())

        View.boton(ventana, "Buscar", enviar)
        View.boton(ventana, "Volver", volver_cmd)

#menu principal
    def __init__(self, ventana):
        ventana.title("..: Coches System :..")
        ventana.geometry("800x700")
        ventana.resizable(False, False)
        View.menu_principal(ventana)

    @staticmethod
    def menu_principal(ventana):

        View.borrar(ventana)
        View.titulo(ventana, "..:: Menú Principal ::..")

        View.boton(ventana, "1.- Autos", lambda: View.menu_autos(ventana))
        View.boton(ventana, "2.- Camionetas", lambda: View.menu_camionetas(ventana))
        View.boton(ventana, "3.- Camiones", lambda: View.menu_camiones(ventana))
        View.boton(ventana, "4.- Salir", ventana.quit)

#AUTOS
    @staticmethod
    def menu_autos(ventana):

        View.borrar(ventana)
        View.titulo(ventana, "..:: Menú Autos ::..")

        View.boton(ventana, "1.- Insertar", lambda: View.form_auto(ventana))
        View.boton(ventana, "2.- Consultar", lambda: View.mostrar_autos(ventana))
        View.boton(ventana, "3.- Actualizar", lambda: View.auto_id(ventana, "actualizar"))
        View.boton(ventana, "4.- Eliminar", lambda: View.auto_id(ventana, "eliminar"))

        View.boton(ventana, "Regresar", lambda: View.menu_principal(ventana))

    @staticmethod
    def form_auto(ventana):

        def guardar(datos):
            Controlador.insertar_auto(datos)
            View.menu_autos(ventana)

        campos = ["Marca", "Color", "Modelo", "Velocidad", "Potencia", "Nro Plazas"]

        View.formulario_generico(
            ventana,
            "...: Registro de Autos :...",
            campos,
            guardar,
            lambda: View.menu_autos(ventana)
        )

    @staticmethod
    def mostrar_autos(ventana):

        View.borrar(ventana)
        View.titulo(ventana, "...: Consulta de Autos :...")

        txt = Text(ventana, height=20, width=80)
        txt.pack(pady=10)

        txt.insert(END, Controlador.consultar_autos())
        txt.config(state=DISABLED)

        View.boton(ventana, "Volver", lambda: View.menu_autos(ventana))

    @staticmethod
    def auto_id(ventana, tipo):
        if tipo == "actualizar":
            View.pedir_id(
                ventana,
                "...: Ingresa ID del Auto a Modificar :...",
                lambda id: View.editar_auto(ventana, id),
                lambda: View.menu_autos(ventana),
            )
        else:
            View.pedir_id(
                ventana,
                "...: Ingresa ID del Auto a Eliminar :...",
                lambda id: View.borrar_auto(ventana, id),
                lambda: View.menu_autos(ventana),
            )

    @staticmethod
    def editar_auto(ventana, id):

        def guardar(datos):
            Controlador.actualizar_auto(id, datos)
            View.menu_autos(ventana)

        campos = ["Marca", "Color", "Modelo", "Velocidad", "Potencia", "Nro Plazas"]

        View.formulario_generico(
            ventana,
            f"...: Modificar Auto {id} :...",
            campos,
            guardar,
            lambda: View.menu_autos(ventana)
        )

    @staticmethod
    def borrar_auto(ventana, id):
        Controlador.eliminar_auto(id)
        View.menu_autos(ventana)

#CAMIONETAS
    @staticmethod
    def menu_camionetas(ventana):

        View.borrar(ventana)
        View.titulo(ventana, "..:: Menú Camionetas ::..")

        View.boton(ventana, "1.- Insertar", lambda: View.form_camioneta(ventana))
        View.boton(ventana, "2.- Consultar", lambda: View.mostrar_camionetas(ventana))
        View.boton(ventana, "3.- Actualizar", lambda: View.camioneta_id(ventana, "actualizar"))
        View.boton(ventana, "4.- Eliminar", lambda: View.camioneta_id(ventana, "eliminar"))

        View.boton(ventana, "Regresar", lambda: View.menu_principal(ventana))

    @staticmethod
    def form_camioneta(ventana):

        def guardar(datos):
            Controlador.insertar_camioneta(datos)
            View.menu_camionetas(ventana)

        campos = ["Marca", "Color", "Modelo", "Velocidad", "Potencia"]

        View.formulario_generico(
            ventana,
            "...: Registro de Camionetas :...",
            campos,
            guardar,
            lambda: View.menu_camionetas(ventana)
        )

    @staticmethod
    def mostrar_camionetas(ventana):

        View.borrar(ventana)
        View.titulo(ventana, "...: Consulta de Camionetas :...")

        txt = Text(ventana, height=20, width=80)
        txt.pack(pady=10)

        txt.insert(END, Controlador.consultar_camionetas())
        txt.config(state=DISABLED)

        View.boton(ventana, "Volver", lambda: View.menu_camionetas(ventana))

    @staticmethod
    def camioneta_id(ventana, tipo):
        if tipo == "actualizar":
            View.pedir_id(
                ventana,
                "...: Ingresa ID de la Camioneta a Modificar :...",
                lambda id: View.editar_camioneta(ventana, id),
                lambda: View.menu_camionetas(ventana),
            )
        else:
            View.pedir_id(
                ventana,
                "...: Ingresa ID de la Camioneta a Eliminar :...",
                lambda id: View.borrar_camioneta(ventana, id),
                lambda: View.menu_camionetas(ventana),
            )

    @staticmethod
    def editar_camioneta(ventana, id):

        def guardar(datos):
            Controlador.actualizar_camioneta(id, datos)
            View.menu_camionetas(ventana)

        campos = ["Marca", "Color", "Modelo", "Velocidad", "Potencia"]

        View.formulario_generico(
            ventana,
            f"...: Modificar Camioneta {id} :...",
            campos,
            guardar,
            lambda: View.menu_camionetas(ventana)
        )

    @staticmethod
    def borrar_camioneta(ventana, id):
        Controlador.eliminar_camioneta(id)
        View.menu_camionetas(ventana)

#CAMIONES
    @staticmethod
    def menu_camiones(ventana):

        View.borrar(ventana)
        View.titulo(ventana, "..:: Menú Camiones ::..")

        View.boton(ventana, "1.- Insertar", lambda: View.form_camion(ventana))
        View.boton(ventana, "2.- Consultar", lambda: View.mostrar_camiones(ventana))
        View.boton(ventana, "3.- Actualizar", lambda: View.camion_id(ventana, "actualizar"))
        View.boton(ventana, "4.- Eliminar", lambda: View.camion_id(ventana, "eliminar"))

        View.boton(ventana, "Regresar", lambda: View.menu_principal(ventana))

    @staticmethod
    def form_camion(ventana):

        def guardar(datos):
            Controlador.insertar_camion(datos)
            View.menu_camiones(ventana)

        campos = ["Marca", "Color", "Modelo", "Velocidad", "Potencia"]

        View.formulario_generico(
            ventana,
            "...: Registro de Camiones :...",
            campos,
            guardar,
            lambda: View.menu_camiones(ventana)
        )

    @staticmethod
    def mostrar_camiones(ventana):

        View.borrar(ventana)
        View.titulo(ventana, "...: Consulta de Camiones :...")

        txt = Text(ventana, height=20, width=80)
        txt.pack(pady=10)

        txt.insert(END, Controlador.consultar_camiones())
        txt.config(state=DISABLED)

        View.boton(ventana, "Volver", lambda: View.menu_camiones(ventana))

    @staticmethod
    def camion_id(ventana, tipo):
        if tipo == "actualizar":
            View.pedir_id(
                ventana,
                "...: Ingresa ID del Camión a Modificar :...",
                lambda id: View.editar_camion(ventana, id),
                lambda: View.menu_camiones(ventana),
            )
        else:
            View.pedir_id(
                ventana,
                "...: Ingresa ID del Camión a Eliminar :...",
                lambda id: View.borrar_camion(ventana, id),
                lambda: View.menu_camiones(ventana),
            )

    @staticmethod
    def editar_camion(ventana, id):

        def guardar(datos):
            Controlador.actualizar_camion(id, datos)
            View.menu_camiones(ventana)

        campos = ["Marca", "Color", "Modelo", "Velocidad", "Potencia"]

        View.formulario_generico(
            ventana,
            f"...: Modificar Camión {id} :...",
            campos,
            guardar,
            lambda: View.menu_camiones(ventana)
        )

    @staticmethod
    def borrar_camion(ventana, id):
        Controlador.eliminar_camion(id)
        View.menu_camiones(ventana)
