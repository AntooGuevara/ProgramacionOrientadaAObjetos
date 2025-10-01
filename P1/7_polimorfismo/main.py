from coches import *
import os
os.system("cls")
#Solicitar los datos que posteriormente serán los atributos del objeto

def autos():
    print(f"\n\tDATOS DEL VEHICULO")
    marca=input("Ingresa la marca ").upper()
    color=input("Ingresa el color ").upper()
    modelo=input("Ingresa el modelo ").upper()
    velocidad=int(input("Ingresa la velocidad "))
    potencia=int(input("Ingresa la potencia "))
    plazas=int(input("Ingresa el # de plazas "))

    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)

    print(f"\n\tDatos del Vehiculo: \n Marca:{coche1._marca()} \n color: {coche1._color()} \n Modelo: {coche1._modelo()} \n velocidad: {coche1._velocidad()} \n caballaje: {coche1._caballaje()} \n plazas: {coche1._plazas()} ")

def camionetas():
    print(f"\n\tDATOS DEL VEHICULO")
    marca=input("Ingresa la marca ").upper()
    color=input("Ingresa el color ").upper()
    modelo=input("Ingresa el modelo ").upper()
    velocidad=int(input("Ingresa la velocidad "))
    potencia=int(input("Ingresa la potencia "))
    plazas=int(input("Ingresa el # de plazas "))
    traccion=int(input("Ingresa el tipo de tracción")).upper()
    cerrada=input("Es cerrada (SI/NO)").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False
        

    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)

    print(f"\n\tDatos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")


def camiones():
    print(f"\n\tDATOS DEL VEHICULO")
    marca=input("Ingresa la marca ").upper()
    color=input("Ingresa el color ").upper()
    modelo=input("Ingresa el modelo ").upper()
    velocidad=int(input("Ingresa la velocidad "))
    potencia=int(input("Ingresa la potencia "))
    plazas=int(input("Ingresa el # de plazas "))

    eje=int(input("Ingresa el número de ejes"))
    capacidadCarga=int(input("Ingresa la capacidad de carga"))
        

    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)

    print(f"\n\tDatos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} \n, eje:{coche1.eje()}\n capacidad de carga: {coche1.capacidadCarga()}")

opcion=1
while opcion!="4":
    os.system("cls")
    opcion=input(" ...::Menu principal::... \n\t\t \n\t 1- Autos\n\t 2- Camionetas \n\t 3- Camiones \n\t 4- Salir \n\t ELIGE UNA OPCIÓN ").lower().strip()
    match opcion:
        case "1":
            autos()
        case "2":
            camionetas()
        case "3":
            camiones()
        case "4":
            print("Salió del sistema")
            input("Presione cualquier tecla para continuar")

            
        case _:
            print("Opcion invalida")
            input("Presione cualquier tecla para continuar")

    
    
    
    



coche=Coches("VW","Blanco","2020",220,180,4)
print(coche._color,coche.acelerar())

camion=camiones("VW","Blanco aperlado","2020",220,180,4,2,2500)
print(camiones.acelerar())

camioneta=camionetas("VW","Blanco asdadqw","2020",220,180,4,"delantera",True)
print(camionetas.setColor,camionetas.acelerar)

