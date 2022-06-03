class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def get_nombre(self):
        return self.nombre

    def set_nombre(self,nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Nombre: {self.nombre} \n Apellido: {self.apellido}"    

yo = Persona("Luas","Bejo")
yo.set_nombre("Lucas")
print(yo)
                