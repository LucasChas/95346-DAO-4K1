from auto import Auto
from moto import Moto
from camioneta import Camioneta

class Empresa():
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.vehiculos = []
        self.cargar_archivo()
    #1) 
    def cargar_archivo(self,):
        archivo = open(self.nombre_archivo,"rt")
        for linea in archivo:
            campos = linea[:-1].split(",")
            tipo = int(campos[0])
            matricula = campos[2]
            marca = campos[1]
            modelo = campos[3]
            costo_base = float(campos[4])
            if tipo == 1:
                kilometraje = int(campos[5])
                vehiculo = Auto(tipo,matricula,marca,modelo,costo_base,kilometraje)
            elif tipo == 2:
                capacidad_carga = int(campos[5])
                vehiculo = Camioneta(tipo,matricula,marca,modelo,costo_base,capacidad_carga)
            else:
                cilindrada = int(campos[5])
                vehiculo = Moto(tipo,matricula,marca,modelo,costo_base,cilindrada)
            self.vehiculos.append(vehiculo)
        archivo.close()

    #2) Calcular el costo total de mantenimiento de todos los vehículos

    def calcular_costo_total_matenimiento(self):
        total = 0
        for vehiculo in self.vehiculos:
            total += vehiculo.calcular_costo_mantenimiento()
        return total

    #3) Calcular el costo de mantenimiento de cada vehículo, aplicando los incrementos mencionados.
    #Ya esta resuelto. - se lista.

    #4)Obtener el vehículo con el costo de mantenimiento más alto
    def vehiculo_costo_mas_alto(self):
        primero = True
        vehiculo = None

        for v in self.vehiculos:
            if primero:
                primero = False
                mayor = v.calcular_costo_mantenimiento()
                vehiculo = v
            else:
                if v.calcular_costo_mantenimiento() > mayor:
                    mayor = v.calcular_costo_mantenimiento()
                    vehiculo = v
        return vehiculo

    #5) Contar cuántas camionetas tienen más de 1000 kg de capacidad de carga
    def camionetas_mas_mil_kg(self):
        cantidad = 0
        for vehiculo in self.vehiculos:
            if vehiculo.tipo == 2:
                if vehiculo.capacidad_carga > 1000:
                    cantidad += 1
        return cantidad

    #6) Obtener el total de motos que son de alta cilindrada
    def motos_alta_cilidrada(self):
        cantidad = 0
        for vehiculo in self.vehiculos:
            if vehiculo.tipo == 3:
                if vehiculo.cilindrada > 500:
                    cantidad += 1
        return cantidad

    
        

    