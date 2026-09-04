from abc import ABC, abstractmethod

class MiInterfaz(ABC):  # Importa ABC aquí
    @abstractmethod
    def metodo_abstracto(self):
        pass

class MiClaseConcreta(MiInterfaz):
    def metodo_abstracto(self):
        return "Implementación del método abstracto 2"

claseprueba = MiClaseConcreta()
print(claseprueba.metodo_abstracto())