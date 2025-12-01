from tkinter import messagebox
from model.nota import Nota

class FuncionesController:
    @staticmethod
    def calcular(operacion, n1, n2):
        try:
            n1 = float(n1)
            n2 = float(n2)
            
            if operacion == "suma":
                resultado = n1 + n2
                signo = "+"
                tipo_ope = "Suma"
            elif operacion == "resta":
                resultado = n1 - n2
                signo = "-"
                tipo_ope = "Resta"
            elif operacion == "multiplicacion":
                resultado = n1 * n2
                signo = "x"
                tipo_ope = "Multiplicación"
            elif operacion == "division":
                if n2 == 0:
                    messagebox.showerror("Error", "No se puede dividir por cero")
                    return
                resultado = n1 / n2
                signo = "/"
                tipo_ope = "División"
            else:
                return

            mensaje = f"{n1} {signo} {n2} = {resultado:.2f}"
            
            messagebox.showinfo("Resultado", mensaje)
            
            guardar = messagebox.askquestion("Guardar", "¿Deseas guardar esta operación en la base de datos?")
            if guardar == "yes":
                if Nota.insertar(n1, n2, signo, resultado):
                    messagebox.showinfo("Éxito", "Operación guardada correctamente")
                else:
                    messagebox.showerror("Error", "No se pudo guardar la operación")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa números válidos")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")