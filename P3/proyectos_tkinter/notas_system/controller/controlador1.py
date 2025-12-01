from tkinter import messagebox
from model import usuario, nota
from view import view1

class controlador:
    @staticmethod
    def registro(nombre, apellidos, email, contrasena):
        resultado = usuario.Usuario.registrar(nombre, apellidos, email, contrasena)

        if resultado:
            messagebox.showinfo(
                title="REGISTRO ÉXITOSO",
                message=f"{nombre} {apellidos} se registró correctamente con el email: {email}",
                icon="info"
            )
        else:
            messagebox.showinfo   (
                title="Usuarios",
                message="...** Por favor intentelo de nuevo, no fue posible insertar el registro **...",
                icon="info"
            )

    @staticmethod   
    def inicio_sesion(ventana,email,contrasena):
        registro=usuario.Usuario.iniciar_sesion(email,contrasena)
        if registro:
            messagebox.showinfo(icon="info",message=f".:: {registro[1]} {registro[2]}, inciaste sesión correctamente::.",title="Usuarios") 
            view1.View.menu_ids(ventana,registro[0],registro[1],registro[2])
        else:
            messagebox.showinfo(icon="info",message=f"** Email y/o contraseña incorrectas, vuelva a intentarlo **",title="Usuarios")
   

    @staticmethod
    def crear_nota(usuario_id,titulo,descripcion):
        respuesta=nota.crear
   