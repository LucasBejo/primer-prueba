class Animal:
    def __init__(self,especie,nombre,edad):
        self.especie = especie
        self.nombre = nombre
        self.edad = edad

    def ruido(self):
        pass

    def describir(self):
        print(f"Soy un animal del tipo: {type(self).__name__}")    

class Perro(Animal):
    def ruido(self):
        print("Guau")
class Ave(Animal):
    def ruido(self):
        print("br br")
    def volar(self,volar):
        print(f"El ave volo {volar} km")    
thor = Perro("Dios","Thor","10")    
thor.describir()
print(thor.especie)
thor.ruido()

hawk = Ave("hawk","hawk","13")
print(hawk.nombre)
hawk.ruido()
hawk.volar(70)
hawk.describir()