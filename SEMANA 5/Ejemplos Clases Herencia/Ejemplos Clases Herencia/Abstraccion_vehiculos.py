from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def detener(self):
        pass

    def obtener_informacion(self):
        return f"{self.año} {self.marca} {self.modelo}"

class Coche(Vehiculo):
    def arrancar(self):
        return f"El coche {self.obtener_informacion()} ha arrancado."

    def detener(self):
        return f"El coche {self.obtener_informacion()} se ha detenido."

class Moto(Vehiculo):
    def arrancar(self):
        return f"La moto {self.obtener_informacion()} ha arrancado."

    def detener(self):
        return f"La moto {self.obtener_informacion()} se ha detenido."

# Crear instancias de las clases derivadas
mi_coche = Coche("Toyota", "Corolla", 2022)
mi_moto = Moto("Honda", "CBR 600", 2021)

# Utilizar los métodos de las clases derivadas
print(mi_coche.arrancar())  # Salida: El coche 2022 Toyota Corolla ha arrancado.
print(mi_moto.detener())    # Salida: La moto 2021 Honda CBR 600 se ha detenido.
