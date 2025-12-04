from tkinter import messagebox
from model.cochesBD import Autos, Camionetas, Camiones


class Controlador:

# ----------------------------------------------------
# AUTOS
# ----------------------------------------------------

    @staticmethod
    def insertar_auto(datos):
        try:
            a = Autos(
                datos["Marca"],
                datos["Color"],
                datos["Modelo"],
                datos["Velocidad"],
                datos["Potencia"],
                datos["Nro Plazas"]
            )
            if a.insertar():
                messagebox.showinfo("Guardar", "Auto registrado correctamente")
            else:
                messagebox.showerror("Error", "No se pudo guardar el auto")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    @staticmethod
    def consultar_autos():
        registros = Autos.consultar()
        if not registros:
            return "No hay autos registrados"
        
        texto = ""
        for fila in registros:
            texto += f"ID: {fila[0]} | Marca: {fila[1]} | Modelo: {fila[3]} | Plazas: {fila[6]}\n"

        return texto


    @staticmethod
    def actualizar_auto(id, datos):
        ok = Autos.actualizar(
            datos["Marca"],
            datos["Color"],
            datos["Modelo"],
            datos["Velocidad"],
            datos["Potencia"],
            datos["Nro Plazas"],
            id
        )

        if ok:
            messagebox.showinfo("Actualizar", f"Auto {id} actualizado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo actualizar el auto")


    @staticmethod
    def eliminar_auto(id):
        ok = Autos.eliminar(id)
        if ok:
            messagebox.showinfo("Eliminar", f"Auto {id} eliminado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo eliminar el auto")



# ----------------------------------------------------
# CAMIONETAS
# ----------------------------------------------------

    @staticmethod
    def insertar_camioneta(datos):
        try:
            ok = Camionetas.insertar(
                datos["Marca"],
                datos["Color"],
                datos["Modelo"],
                datos["Velocidad"],
                datos["Potencia"],
                "4",    # plazas default
                "4x4",  # traccion default
                "No"    # cerrada default
            )
            if ok:
                messagebox.showinfo("Guardar", "Camioneta registrada correctamente")
            else:
                messagebox.showerror("Error", "No se pudo guardar la camioneta")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    @staticmethod
    def consultar_camionetas():
        registros = Camionetas.consultar()
        if not registros:
            return "No hay camionetas registradas"
        
        texto = ""
        for fila in registros:
            texto += f"ID: {fila[0]} | Marca: {fila[1]} | Modelo: {fila[3]}\n"

        return texto


    @staticmethod
    def actualizar_camioneta(id, datos):
        ok = Camionetas.actualizar(
            datos["Marca"],
            datos["Color"],
            datos["Modelo"],
            datos["Velocidad"],
            datos["Potencia"],
            "4",
            "4x4",
            "No",
            id
        )
        if ok:
            messagebox.showinfo("Actualizar", f"Camioneta {id} actualizada correctamente")
        else:
            messagebox.showerror("Error", "No se pudo actualizar la camioneta")


    @staticmethod
    def eliminar_camioneta(id):
        ok = Camionetas.eliminar(id)
        if ok:
            messagebox.showinfo("Eliminar", f"Camioneta {id} eliminada correctamente")
        else:
            messagebox.showerror("Error", "No se pudo eliminar la camioneta")



# ----------------------------------------------------
# CAMIONES
# ----------------------------------------------------

    @staticmethod
    def insertar_camion(datos):
        try:
            ok = Camiones.insertar(
                datos["Marca"],
                datos["Color"],
                datos["Modelo"],
                datos["Velocidad"],
                datos["Potencia"],
                "2",   # plazas default
                "6",   # eje default
                "8000" # capacidad
            )
            if ok:
                messagebox.showinfo("Guardar", "Camión registrado correctamente")
            else:
                messagebox.showerror("Error", "No se pudo guardar el camión")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    @staticmethod
    def consultar_camiones():
        registros = Camiones.consultar()
        if not registros:
            return "No hay camiones registrados"
        
        texto = ""
        for fila in registros:
            texto += f"ID: {fila[0]} | Marca: {fila[1]} | Modelo: {fila[3]}\n"

        return texto


    @staticmethod
    def actualizar_camion(id, datos):
        ok = Camiones.actualizar(
            datos["Marca"],
            datos["Color"],
            datos["Modelo"],
            datos["Velocidad"],
            datos["Potencia"],
            "2",
            "6",
            "8000",
            id
        )
        if ok:
            messagebox.showinfo("Actualizar", f"Camión {id} actualizado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo actualizar el camión")


    @staticmethod
    def eliminar_camion(id):
        ok = Camiones.eliminar(id)
        if ok:
            messagebox.showinfo("Eliminar", f"Camión {id} eliminado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo eliminar el camión")
