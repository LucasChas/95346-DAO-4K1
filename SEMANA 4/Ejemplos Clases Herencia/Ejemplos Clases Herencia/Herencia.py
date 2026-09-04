# Clase base (superclase)
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass

# Clase derivada (subclase)
class Perro(Animal):
    def hacer_sonido(self):
        return "Woof!"

# Clase derivada (subclase)
class Gato(Animal):
    def hacer_sonido(self):
        return "Meow!"

# Crear instancias de las subclases
mi_perro = Perro("Rex", 3)
mi_gato = Gato("Whiskers", 2)

# Acceder a los atributos de la superclase
print(f"{mi_perro.nombre} tiene {mi_perro.edad} años.")
print(f"{mi_gato.nombre} tiene {mi_gato.edad} años.")

# Llamar a los métodos de las subclases
print(f"{mi_perro.nombre} hace: {mi_perro.hacer_sonido()}")
print(f"{mi_gato.nombre} hace: {mi_gato.hacer_sonido()}")
