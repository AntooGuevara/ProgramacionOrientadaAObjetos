#que no haya método construcror, que todos los atributos sean publicos, que los métodos de acelerar y frenar no hagan nada.
"""""
import os
os.system(cls)

class Coches:

    marca = ""
    color = ""
    modelo = ""
    velocidad = 0
    caballaje = 0
    plazas = 0


    def acelerar(self):
        pass #el pass sirve para que no haga nada lol (básicamente se salta el código)

    def frenar(self):
        pass



coche1 = Coches()
coche1.marca = "VW"
coche1.color = "Blanco"
coche1.modelo = "2022"
coche1.velocidad = 220
coche1.caballaje = 150
coche1.plazas = 5

coche2 = Coches()
coche2.marca = "Nissan"
coche2.color = "Azul"
coche2.modelo = "2020"
coche2.velocidad = 180
coche2.caballaje = 150
coche2.plazas = 6

# Mostrar los datos de los coches
print(f"Coche 1: {coche1.marca}, {coche1.color}, {coche1.modelo}, {coche1.velocidad} , {coche1.caballaje} , {coche1.plazas}")
print(f"Coche 2: {coche2.marca}, {coche2.color}, {coche2.modelo}, {coche2.velocidad} , {coche2.caballaje} , {coche2.plazas}")

"""

import os
os.system("clear")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      pass

    def frenar(self):
      pass  

#Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches()
coche1.marca="VW"
coche1.color="Blanco"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5

print(f"Datos del Vehiculo: \n Marca:{coche1.marca} \n color: {coche1.color} \n Modelo: {coche1.modelo} \n velocidad: {coche1.velocidad} \n caballaje: {coche1.caballaje} \n plazas: {coche1.plazas} ")

coche2=Coches()

coche2.marca="Nissan"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=150
coche2.plazas=6

print(f"\nDatos del Vehiculo: \n Marca:{coche2.marca} \n color: {coche2.color} \n Modelo: {coche2.modelo} \n velocidad: {coche2.velocidad} \n caballaje: {coche2.caballaje} \n plazas: {coche2.plazas} ")