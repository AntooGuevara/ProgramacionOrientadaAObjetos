import mysql.connector

class Controller:

    @staticmethod
    def conexion():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",   # tu contraseña si tienes
            database="bd_coches"
        )

    # ======================================================
    #                    AUTOS
    # ======================================================

    @staticmethod
    def insertar_auto(datos):
        conn = Controller.conexion()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO autos (marca, color, modelo, velocidad, caballaje, plazas)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            datos["Marca"],
            datos["Color"],
            datos["Modelo"],
            datos["Velocidad"],
            datos["Potencia"],     # Potencia = caballaje
            datos["Nro Plazas"]
        ))

        conn.commit()
        cur.close()
        conn.close()


    @staticmethod
    def consultar_autos():
        conn = Controller.conexion()
        cur = conn.cursor()

        cur.execute("SELECT * FROM autos")
        filas = cur.fetchall()

        conn.close()

        texto = ""
        for f in filas:
            texto += str(f) + "\n"
        return texto


    @staticmethod
    def eliminar_auto(id):
        conn = Controller.conexion()
        cur = conn.cursor()

        cur.execute("DELETE FROM autos WHERE id_carro=%s", (id,))

        conn.commit()
        cur.close()
        conn.close()


    @staticmethod
    def actualizar_auto(id, datos):
        conn = Controller.conexion()
        cur = conn.cursor()

        cur.execute("""
            UPDATE autos SET
            marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s
            WHERE id_carro=%s
        """, (
            datos["Marca"],
            datos["Color"],
            datos["Modelo"],
            datos["Velocidad"],
            datos["Potencia"],
            datos["Nro Plazas"],
            id
        ))

        conn.commit()
        cur.close()
        conn.close()


    # ======================================================
    #                    CAMIONETAS
    # ======================================================

    @staticmethod
    def insertar_camioneta(datos):
        conn = Controller.conexion()
        cur = conn.cursor()

        # Convertir "Si/No" a 1/0
        cerrada = 1 if datos["Cerrada"].lower() == "si" else 0

        cur.execute("""
            INSERT INTO camionetas (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            datos["Marca"],
            datos["Color"],
            datos["Modelo"],
            datos["Velocidad"],
            datos["Potencia"],
            datos["Nro Plazas"],
            datos["Traccion"],
            cerrada
        ))

        conn.commit()
        cur.close()
        conn.close()


    @staticmethod
    def consultar_camionetas():
        conn = Controller.conexion()
        cur = conn.cursor()

        cur.execute("SELECT * FROM camionetas")
        filas = cur.fetchall()

        conn.close()

        texto = ""
        for f in filas:
            texto += str(f) + "\n"
        return texto


    @staticmethod
    def eliminar_camioneta(id):
        conn = Controller.conexion()
        cur = conn.cursor()

        cur.execute("DELETE FROM camionetas WHERE id_camionetas=%s", (id,))

        conn.commit()
        cur.close()
        conn.close()


    @staticmethod
    def actualizar_camioneta(id, datos):
        conn = Controller.conexion()
        cur = conn.cursor()

        cerrada = 1 if datos["Cerrada"].lower() == "si" else 0

        cur.execute("""
            UPDATE camionetas SET
            marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, traccion=%s, cerrada=%s
            WHERE id_camionetas=%s
        """, (
            datos["Marca"],
            datos["Color"],
            datos["Modelo"],
            datos["Velocidad"],
            datos["Potencia"],
            datos["Nro Plazas"],
            datos["Traccion"],
            cerrada,
            id
        ))

        conn.commit()
        cur.close()
        conn.close()


    # ======================================================
    #                      CAMIONES
    # ======================================================

    @staticmethod
    def insertar_camion(datos):
        conn = Controller.conexion()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO camiones (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            datos["Marca"],
            datos["Color"],
            datos["Modelo"],
            datos["Velocidad"],
            datos["Potencia"],
            2,      # plazas por defecto
            2,      # eje por defecto
            1000    # capacidad carga defecto
        ))

        conn.commit()
        cur.close()
        conn.close()


    @staticmethod
    def consultar_camiones():
        conn = Controller.conexion()
        cur = conn.cursor()

        cur.execute("SELECT * FROM camiones")
        filas = cur.fetchall()

        conn.close()

        texto = ""
        for f in filas:
            texto += str(f) + "\n"
        return texto


    @staticmethod
    def eliminar_camion(id):
        conn = Controller.conexion()
        cur = conn.cursor()

        cur.execute("DELETE FROM camiones WHERE id_camion=%s", (id,))

        conn.commit()
        cur.close()
        conn.close()


    @staticmethod
    def actualizar_camion(id, datos):
        conn = Controller.conexion()
        cur = conn.cursor()

        cur.execute("""
            UPDATE camiones SET
            marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s
            WHERE id_camion=%s
        """, (
            datos["Marca"],
            datos["Color"],
            datos["Modelo"],
            datos["Velocidad"],
            datos["Potencia"],
            id
        ))

        conn.commit()
        cur.close()
        conn.close()
