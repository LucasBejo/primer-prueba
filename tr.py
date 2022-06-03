class Persona:

    especie = "mamifero"
    
    brazos = 2
   
    def __init__(self,nombre,apellido,edad,celu,peso,altura):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.celu = celu
        self.peso = peso
        self.altura = altura

    def kim (self,km):
        print(f"hoy corri {km} km")

    def masa_corporal(self,peso,altura):
        n = float(peso / altura **2)
        print(f"la masa corporal es: {n}")       

yo = Persona("Lucas","Bejo",20,"1131217015",70,178)
print(f"\n Nombre: {yo.nombre} \n Apellido: {yo.apellido}")
print(f"especie: {yo.especie}")
print(f"brazos{yo.brazos}")
print(yo.celu)
yo.kim(10)
yo.masa_corporal(yo.peso,yo.altura)