class Personas:
    def __init__(self, nombre, edad, tel):
        self.nombre = nombre
        self.edad = edad
        self.tel = tel
    
    def info_persona(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Tel: {self.tel}"