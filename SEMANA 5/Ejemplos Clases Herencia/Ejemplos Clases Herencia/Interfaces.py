class MiInterfaz:
    def metodo_abstracto(self):
        pass

class MiClaseConcreta(MiInterfaz):
    def metodo_abstracto(self):
        return "Implementación del método abstracto"
    
pruebaclase=MiClaseConcreta()
print(pruebaclase.metodo_abstracto())