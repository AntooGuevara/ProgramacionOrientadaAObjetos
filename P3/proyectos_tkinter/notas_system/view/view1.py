from tkinter import *
from tkinter import messagebox
from controller import controlador1

class View:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.title("ids System")
        ventana.geometry("800x600")
        ventana.resizable(0,0)
        self.menu_principal(ventana)
    @staticmethod
    def borrarpantalla(ventana):
            for widget in ventana.winfo_children():
                 widget.destroy()
    @staticmethod
    def menu_principal(ventana):
        View.borrarpantalla(ventana)
        lbl_titulo=Label(ventana,text="..::Menú principal::..",justify="center")
        lbl_titulo.pack()
        btn_registro=Button(ventana,text="1.- Registro",justify="center",command=lambda:View.registros(ventana))
        btn_registro.pack(pady=15)
        btn_login=Button(ventana,text="2.- Login",justify="center",command=lambda:View.login(ventana))
        btn_login.pack(pady=15)
        btn_salir=Button(ventana,text="3.- Salir",justify="center",command=ventana.quit)
        btn_salir.pack(pady=15)
    @staticmethod
    def registros(self, ventana):
     View.borrarpantalla(ventana)

     Label(ventana, text="..::Registro::..", justify="center").pack()

     Label(ventana, text="¿Cuál es tu nombre?", justify="center").pack()
     txt_nombre = Entry(ventana)
     txt_nombre.focus()
     txt_nombre.pack(pady=15)

     Label(ventana, text="¿Cuáles son tus apellidos?", justify="center").pack()
     txt_apellidos = Entry(ventana)
     txt_apellidos.pack(pady=15)

     Label(ventana, text="Ingresa tu Email", justify="center").pack()
     txt_email = Entry(ventana)
     txt_email.pack(pady=15)

     Label(ventana, text="Ingresa tu contraseña", justify="center").pack()
     txt_contrasena = Entry(ventana, show="*")
     txt_contrasena.pack(pady=15)

     btn_registrar = Button(
          ventana,
          text="Registrar",
          justify="center",
          command=lambda: controlador1.controlador.registro(
               txt_nombre.get(),
               txt_apellidos.get(),
               txt_email.get(),
               txt_contrasena.get()
          )
     )
     btn_registrar.pack()

     btn_volver = Button(
          ventana,
          text="Volver",
          justify="center",
          command=lambda: self.menu_principal(ventana)
     )
     btn_volver.pack()
    @staticmethod 
    def login(ventana):
         View.borrarpantalla(ventana)
         lbl_titulo=Label(ventana,text="..::Registo en el sistema::..",justify="center")
         lbl_titulo.pack()
         lbl_email=Label(ventana,text="Ingresa tu Email",justify="center")
         lbl_email.pack()
         txt_email=Entry(ventana)
         txt_email.focus
         txt_email.pack(pady=15)
         lbl_contrasena=Label(ventana,text="Ingresa tu contraseña",justify="center")
         lbl_contrasena.pack()
         txt_contrasena=Entry(ventana)
         txt_contrasena.focus
         txt_contrasena.pack(pady=15)

         btn_login = Button(
          ventana,
          text="Entrar",
          justify="center",
          command=lambda: (
               controlador1.controlador.inicio_sesion(ventana,txt_email.get(), txt_contrasena.get()),
               View.menu_ids(ventana)
          )
          )

         btn_login.pack()
         btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:View.menu_principal(ventana))
         btn_volver.pack()

    @staticmethod 
    def menu_ids(ventana,usuario_id,nombre,apellidos):
         global id_user,nom_user,ape_user
         id_user=usuario_id
         nom_user=nombre
         ape_user=apellidos

         View.borrarpantalla(ventana)
         lbl_titulo=Label(ventana,text=f"Bienvenido, has iniciado sesión",justify="center")
         lbl_titulo.pack()
         btn_crear=Button(ventana,text="Crear",justify="center",command=lambda:View.crear_id(ventana))
         btn_crear.pack()
         btn_mostrar=Button(ventana,text="Mostrar",justify="center",command=lambda:View.descripcion(ventana))
         btn_mostrar.pack()
         btn_cambiar=Button(ventana,text="Cambiar",justify="center",command=lambda:View.modificar(ventana))
         btn_cambiar.pack()
         btn_eliminar=Button(ventana,text="Eliminar",justify="center",command=lambda:View.eliminar(ventana))
         btn_eliminar.pack()
         btn_regresar=Button(ventana,text="Regresar",justify="center",command=lambda:View.login(ventana))
         btn_regresar.pack()
    @staticmethod     
    def crear_id(ventana):
         View.borrarpantalla(ventana)
         lbl_titulo=Label(ventana,text="..::Crear id::..",justify="center")
         lbl_titulo.pack()
         lbl_titulo=Label(ventana,text="Titulo",justify="center")
         lbl_titulo.pack()
         lbl_titulo=Entry(ventana)
         lbl_titulo.focus
         lbl_titulo.pack(pady=15)
         lbl_descripcion=Label(ventana,text="Descripción",justify="center")
         lbl_descripcion.pack()
         lbl_descripcion=Entry(ventana)
         lbl_descripcion.focus
         lbl_descripcion.pack(pady=15)

         btn_guardar=Button(ventana,text="Guardar",justify="center",command=lambda:View.menu_ids(ventana))
         btn_guardar.pack()
         btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:View.menu_ids(ventana))
         btn_volver.pack()
    @staticmethod 
    def descripcion(ventana):
         View.borrarpantalla(ventana)
         txt_descripcion=Text(ventana,text="Tus ids son:",justify="center")
         txt_descripcion.pack()
         filas=""
         registros=[("1","100","Descripcion de la id","2025-11-24")]
         num_id=1
         if len(registros)<0:
            for fila in registros:
                filas=filas+f"id: {num_id} \n ID: {fila[0]} .- Titulo: {fila[2]} \t Fecha de Creación {fila[4]} \n\t Descripción: {fila(3)}"
                num_id+=1
         else:
              messagebox.showinfo(icon="warning",Text="No hay ids para este usuario")
         lbl_resultado=Label(ventana,text=f"{filas}")
         lbl_resultado.pack()
         btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:View.menu_ids(ventana))
         btn_volver.pack()
    @staticmethod 
    def modificar(ventana):
        View.borrarpantalla(ventana)
        lbl_titulo=Label(ventana,text="..::Vamos a modifcar una id::..",justify="center")
        lbl_titulo.pack()
        lbl_id=Label(ventana,text="ID de la id a cambiar",justify="center")
        lbl_id.pack()
        txt_id=Entry(ventana)
        lbl_id.focus
        txt_id.pack(pady=15)
        lbl_titulo=Label(ventana,text="Nuevo titulo",justify="center")
        lbl_titulo.pack()
        txt_titulo=Entry(ventana)
        txt_titulo.focus
        txt_titulo.pack(pady=15)
        lbl_descripcion=Label(ventana,text="Nueva Descripción",justify="center")
        lbl_descripcion.pack()
        txt_descripcion=Entry(ventana)
        txt_descripcion.focus
        txt_descripcion.pack(pady=15)
        btn_registrar=Button(ventana,text="Guardar",justify="center",command=lambda:View.menu_ids(ventana))
        btn_registrar.pack()
        btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:View.menu_ids(ventana))
        btn_volver.pack()
    @StopAsyncIteration 
    def eliminar(ventana):
         View.borrarpantalla(ventana)
         lbl_titulo=Label(ventana,text="..::Eliminar una id::..",justify="center")
         lbl_titulo.pack()
         lbl_id=Label(ventana,text="ID de la id a eliminar",justify="center")
         lbl_id.pack()
         txt_id=Entry(ventana)
         txt_id.focus
         txt_id.pack(pady=15)
         btn_entrar=Button(ventana,text="Eliminar",justify="center",command=lambda:View.menu_ids(ventana))
         btn_entrar.pack()
         btn_volver=Button(ventana,text="Volver",justify="center",command=lambda:View.menu_ids(ventana))
         btn_volver.pack()


    



