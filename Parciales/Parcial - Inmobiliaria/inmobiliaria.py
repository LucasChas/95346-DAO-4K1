from casa import Casa
from departamento import Departamento


class Inmobiliaria():
    def __init__(self,nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.inmuebles = []
        self.cargar_archivo()

    def cargar_archivo(self):
        archivo = open(self.nombre_archivo, "rt")
        for linea in archivo:
            campos = linea[:-1].split(",")
            tipo = int(campos[0])
            codigo = campos[1]
            nombre_propietario = campos[2]
            alquiler_base = float(campos[3])
            superficie = int(campos[4])
            if tipo == 1:
                cant_hab = int(campos[5])
                tiene_pileta = int(campos[6])
                inmueble = Casa(tipo,codigo,nombre_propietario,alquiler_base,superficie,cant_hab,tiene_pileta)
            elif tipo == 2:
                expensas = float(campos[5])
                piso = int(campos[6])
                inmueble = Departamento(tipo,codigo,nombre_propietario,alquiler_base,superficie,expensas,piso)
            self.inmuebles.append(inmueble)

    #Suma de alquileres
    def suma_alquileres(self):
        total = 0
        for i in self.inmuebles:
            total += i.calcular_costo()
        return total
    #Cantidad de casas premium
    def casas_premium(self):
        cantidad = 0
        for i in self.inmuebles:
            if i.tipo == 1:
                if (i.superficie > 150) and (i.cant_hab > 2) and (i.tiene_pileta == 1):
                    cantidad += 1
        return cantidad

    #Propietario del alquier más bajo
    def propietario_mas_bajo(self):
        primero = True
        nombre = None
        for i in self.inmuebles:
            if primero:
                primero = False
                menor = i.calcular_costo()
                nombre = i.nombre_propietario
            else:
                if i.calcular_costo() < menor:
                    menor = i.calcular_costo()
                    nombre = i.nombre_propietario
        return nombre

    