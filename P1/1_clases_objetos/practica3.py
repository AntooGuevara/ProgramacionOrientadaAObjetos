import os
os.system("cls")


class Alumno:
    def __init__(self, nombre, edad, matricula):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula

    def inscribirse(self):
        print(f"{self.nombre} se ha inscrito con la matrícula {self.matricula}.")

    def estudiar(self):
        print(f"{self.nombre} está estudiando.\n")


class Profesor:
    def __init__(self, nombre, experiencia, num_profesor):
        self.nombre = nombre
        self.experiencia = experiencia
        self.num_profesor = num_profesor

    def impartir(self, curso):
        print(f"El profesor {self.nombre} imparte el curso {curso.nombre}.")

    def evaluar(self, alumno):
        print(f"El profesor {self.nombre} evalúa al alumno {alumno.nombre}.\n")



class Curso:
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos

    def asignar(self, profesor):
        print(f"El curso {self.nombre} ha sido asignado al profesor {profesor.nombre}.")

#############

alumno1 = Alumno("Juan Pérez", 19, "546728199")
alumno2 = Alumno("Angel Madrid", 20, "487563892")

profesor1 = Profesor("Abner Vidaña", "10 años", "6189348234")
profesor2 = Profesor("Jared Nuñez", "20 años", "6678943876")

curso1 = Curso("Programación", 101, 6)
curso2 = Curso("Dibujo", 104, 5)


# Ejemplos de uso
alumno1.inscribirse()
alumno1.estudiar()
alumno2.inscribirse()
alumno2.estudiar()

profesor1.impartir(curso1)
profesor1.evaluar(alumno1)
profesor2.impartir(curso2)
profesor2.evaluar(alumno2)

curso1.asignar(profesor1)
curso2.asignar(profesor2)

