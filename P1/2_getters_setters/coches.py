import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
  """  marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0"""

    #Crear los métodos setters y getters, estos son importantes y necesarios en todas las clases para que el programador interactué con los valores de los atributos a traves de estos métodos... digamos que es la manera más adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a través de un objeto.
    #En teoria se debería de crear un método Getters y Setters por cada atributo que contenga la clase.
    #Los métodos get siempre regresan valor, es decir, el valor de la propiedad a través del return.
    #Por otro lado, el método set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion.
    
  def getMarca(self):
      return self.marca    
  def setMarca(self,marca):
      self.marca=marca
      
  #####################
  #2da forma
  @property
  def marca(self):
    return self.marca
  
  @marca.setter
  def marca (self,marca):
    self.marca=marca
  #####################   
   
  def getColor(self):
      return self.color
  def setColor(self,color):
    self.color=color
    
  def setModelo(self):
      return self.modelo
  def getModelo(self,modelo):
      self.modelo=modelo 
      
  def getVelocidad(self):
      return self.velocidad
  def setVelocidad(self,velocidad):
    self.velocidad=velocidad
    
  def setCaballaje(self):
      return self.caballaje
  def getCaballaje(self,caballaje):
    self.caballaje=caballaje
    
  def getPlazas(self):
      return self.plazas
  def setPlazas(self,plazas):
    self.plazas=plazas
        
    
    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      pass

    def frenar(self):
      pass  

#Fin definir clase

#Crear un objetos o instanciar la clase
coche1=Coches()
coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)

coche2=Coches()
coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(5)


"""coche1=Coches()
coche1.marca="VW"
coche1.color="Blanco"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5"""

print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca} \n color: {coche1.getColor} \n Modelo: {coche1.getModelo} \n velocidad: {coche1.getVelocidad} \n caballaje: {coche1.getCaballaje} \n plazas: {coche1.getPlazas} ")

"""coche2=Coches()

coche2.setMarca="Nissan"
coche2.setColor="Azul"
coche2.setModelo="2020"
coche2.setVelocidad=180
coche2.setCaballaje=150
coche2.setPlazas=6"""

print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca} \n color: {coche2.getColor} \n Modelo: {coche2.getModelo} \n velocidad: {coche2.getVelocidad} \n caballaje: {coche2.getCaballaje} \n plazas: {coche2.getPlazas} ")

coche3=Coches()

coche3.marca="Honda"
print(coche3.marca)