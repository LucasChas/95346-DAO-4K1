from abc import ABC, abstractmethod

# Clase abstracta Cliente
class Cliente(ABC):
    def __init__(self, nombre, monto_compra):
        self.nombre = nombre
        self.monto_compra = monto_compra

    @abstractmethod
    def calcular_descuento(self):
        pass

# Subclase ClienteRegular
class ClienteRegular(Cliente):
    def calcular_descuento(self):
        if self.monto_compra > 100:
            return self.monto_compra * 0.05  # Descuento del 5%
        else:
            return 0

# Subclase ClientePremium
class ClientePremium(Cliente):
    def calcular_descuento(self):
        return self.monto_compra * 0.10  # Descuento del 10%

# Función para calcular el monto total después del descuento
def calcular_total_con_descuento(cliente):
    descuento = cliente.calcular_descuento()
    total = cliente.monto_compra - descuento
    return total

# Crear instancias de clientes
cliente1 = ClienteRegular("Cliente Regular 1", 120)
cliente2 = ClientePremium("Cliente Premium 1", 150)

# Calcular el monto total con descuento para cada cliente
total_cliente1 = calcular_total_con_descuento(cliente1)
total_cliente2 = calcular_total_con_descuento(cliente2)

# Mostrar resultados
print(f"{cliente1.nombre}: Monto a pagar después del descuento: ${total_cliente1}")
print(f"{cliente2.nombre}: Monto a pagar después del descuento: ${total_cliente2}")
