from coches import *

#Solicitar los datos que posteriormente serán los atributos del objeto

"""num_coches=int(input("¿Cuantos coches tienes?"))

for i in range (0,num_coches):  
    print(f"\n\tDATOS DEL AUTOMOVIL #{i+1}")
    marca=input("Ingresa la marca ").upper()
    color=input("Ingresa el color ").upper()
    modelo=input("Ingresa el modelo ").upper()
    velocidad=int(input("Ingresa la velocidad "))
    potencia=int(input("Ingresa la potencia "))
    plazas=int(input("Ingresa el # de plazas "))

    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)

    print(f"\n\tDatos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")
"""

"""coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,0)
coche1.num_serie="B01456789"
coche4=Coches("","","",0,0,0)
coche4.marca="Volvo"

print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")

print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")"""

coche=Coches("VW","Blanco","2020",220,180,4)
print(coche._color,coche.acelerar())

camion=camiones("VW","Blanco aperlado","2020",220,180,4,2,2500)
print(camiones.acelerar())

camioneta=camionetas("VW","Blanco asdadqw","2020",220,180,4,"delantera",True)
print(camionetas.setColor,camionetas.acelerar)

