class Persona:
    def __init__(self,nombre,apellido,trabajo):
        self.nombre = nombre
        self.apellido = apellido
        self.trabajo = trabajo

    def hablar(self):
        print(f"Mi nombre es {self.nombre} {self.apellido} y trabajo de {self.trabajo}")

    def trabajoo (self):
        if self.trabajo == "tenista":
            print("que buen trabajo")
