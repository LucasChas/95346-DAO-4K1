from correctivo import Correctivo
from preventivo import Preventivo

class Maquina():
    def __init__(self,nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.mantenimientos = []
        self.cargar_mantenimiento()

    def cargar_mantenimiento(self):
        archivo = open(self.nombre_archivo,"rt")

        for linea in archivo:
            campos = linea[:-1].split(",")
            tipo = int(campos[0])
            fecha = campos[1]
            operario = campos[2]
            importe_repuesto = float(campos[3])

            if tipo == 1:
                resultado = int(campos[4])
                importe_insumo = float(campos[5])
                mantenimiento = Preventivo(tipo,fecha,operario,importe_repuesto,resultado, importe_insumo)
            elif tipo == 2:
                horas_paradas = int(campos[4])
                importe_tecnico = float(campos[5])
                mantenimiento = Correctivo(tipo,fecha,operario,importe_repuesto,horas_paradas,importe_tecnico)
            self.mantenimientos.append(mantenimiento)

        archivo.close()
        return self.mantenimientos

    def suma_gastos(self):
        total = 0
        for mantenimiento in self.mantenimientos:
            total += mantenimiento.gastos_mantenimiento()
        return total    

    def cant_mant_caros(self):
        cantidad = 0
        tope = 10000
        for mantenimiento in self.mantenimientos:
            if mantenimiento.gastos_mantenimiento() > tope:
                cantidad += 1
        return cantidad

    def rotura_mas_larga(self):
        primero = True
        fecha = None
        operario = None
        for mantenimiento in self.mantenimientos:
            if mantenimiento.tipo_mantenimiento == 2:
                if primero:
                    primero = False
                    mayor = mantenimiento.cantidad_horas_parada
                    fecha = mantenimiento.fecha
                    operario = mantenimiento.operario
                elif mantenimiento.cantidad_horas_parada > mayor : 
                    mayor = mantenimiento.cantidad_horas_parada
                    fecha = mantenimiento.fecha
                    operario = mantenimiento.operario
        return f"Fecha: {fecha} | Operario: {operario}"
