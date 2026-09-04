class Persona:
    def __init__(self, documento=0, nombre="No", apellido="No", edad=0):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, DNI: {self.documento}, Edad: {self.edad}"

persona = Persona(45087630,"Lucas Martin", "Chas Diaz", 22)
persona2 = Persona()
print(f"Objeto: {persona}")
print(f"Objeto: {persona2}")
