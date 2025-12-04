from tkinter import messagebox

class Controlador:

#AUTOS
    @staticmethod
    def insertar_auto(datos):
        messagebox.showinfo("Guardar", "Auto registrado correctamente")

    @staticmethod
    def consultar_autos():
        return "No hay autos registrados (de momento)"

    @staticmethod
    def actualizar_auto(id, datos):
        messagebox.showinfo("Actualizar", f"Auto {id} actualizado correctamente")

    @staticmethod
    def eliminar_auto(id):
        messagebox.showinfo("Eliminar", f"Auto {id} eliminado correctamente")

#CAMIONETAS
    @staticmethod
    def insertar_camioneta(datos):
        messagebox.showinfo("Guardar", "Camioneta registrada correctamente")

    @staticmethod
    def consultar_camionetas():
        return "No hay camionetas registradas (de momento)"

    @staticmethod
    def actualizar_camioneta(id, datos):
        messagebox.showinfo("Actualizar", f"Camioneta {id} actualizada correctamente")

    @staticmethod
    def eliminar_camioneta(id):
        messagebox.showinfo("Eliminar", f"Camioneta {id} eliminada correctamente")

#CAMIONES
    @staticmethod
    def insertar_camion(datos):
        messagebox.showinfo("Guardar", "Camión registrado correctamente")

    @staticmethod
    def consultar_camiones():
        return "No hay camiones registrados (de momento)"

    @staticmethod
    def actualizar_camion(id, datos):
        messagebox.showinfo("Actualizar", f"Camión {id} actualizado correctamente")

    @staticmethod
    def eliminar_camion(id):
        messagebox.showinfo("Eliminar", f"Camión {id} eliminado correctamente")
