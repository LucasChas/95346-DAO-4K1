from abc import ABC, abstractmethod

class Cuenta(ABC):
    def __init__(self,numero,nombre,saldo):
        self.numero = numero
        self.nombre = nombre 
        self.saldo = saldo

    def depositar (self,monto):
        self.saldo += monto

    @abstractmethod
    def extraer (self,monto):
        ...

    def __str__(self):
        return f"#{self.numero} - {self.nombre} - Saldo: {self.saldo:.2f}"

class CajaAhorro (Cuenta):
    def __init__ (self,numero,nombre,saldo):
        super().__init__(numero,nombre,saldo) 

    def extraer(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto 
        else:
            print("Saldo insuficiente")

class CuentaCorriente (Cuenta):
    def __init__ (self,numero,nombre,saldo,acuerdo):
        super().__init__(numero,nombre,saldo) 
        self.acuerdo = acuerdo 

    def extraer(self, monto):
        if (self.saldo+self.acuerdo) >= monto:
            self.saldo -= monto 
        else:
            print ("Saldo(+acuerdo) insuficiente")

cuentas = []
cuentas.append (CajaAhorro(8828282,"Martin",0))
cuentas.append (CuentaCorriente(8828282,"Martin 2",0,100000))

for c in cuentas:
    c.depositar(20000)

for c in cuentas:
    print(c)

for c in cuentas:
    c.extraer(280000)
    print(c)




