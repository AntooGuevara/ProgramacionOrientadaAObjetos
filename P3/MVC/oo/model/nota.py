from conexionBD import *

class Nota:
    @staticmethod 
    def insertar(numero1, numero2, signo, resultado):
        try:
          cursor.execute(
            "INSERT INTO operaciones (numero1, numero2, signo, resultado) VALUES (%s, %s, %s, %s)",
             (numero1, numero2, signo, resultado)
          )
          conexion.commit()
          return True
        except Exception as e:
          print(f"Error al insertar: {e}")
          return False

    @staticmethod
    def consultar():
        try:
          cursor.execute("SELECT * FROM operaciones")
          return cursor.fetchall()
        except Exception as e:
          print(f"Error al consultar: {e}")
          return []

    @staticmethod
    def actualizar(numero1, numero2, signo, resultado, id):
       try:
         cursor.execute(
            "UPDATE operaciones SET numero1=%s, numero2=%s, signo=%s, resultado=%s WHERE id=%s",
            (numero1, numero2, signo, resultado, id)
         )
         conexion.commit()
         return True
       except Exception as e:
         print(f"Error al actualizar: {e}")
         return False
    
    @staticmethod
    def eliminar(id):
        try:
          cursor.execute(
            "DELETE FROM operaciones WHERE id=%s", 
            (id,)
          ) 
          conexion.commit() 
          return True  
        except Exception as e:
          print(f"Error al eliminar: {e}")
          return False