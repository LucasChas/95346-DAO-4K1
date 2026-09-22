from preventivo import Preventivo
from correctivo import Correctivo

class Maquina():
    def __init__(self, nombre_archivo):
        self.mantenimientos = []
        self.nombre_archivo = nombre_archivo
        self.cargar_mantenimientos()

    def cargar_mantenimientos(self):
        archivo = open(self.nombre_archivo, "rt")
        for linea in archivo:
            campos = linea[:-1].split(",")
            tipo = int(campos[0])
            fecha = campos[1]
            operario = campos[2]
            importe_repuestos = float(campos[3])
            if tipo == 1:
                resultado_mant = int(campos[4])
                importe_insumos = float(campos[5])
                mantenimiento = Preventivo(tipo,fecha,operario,importe_repuestos,resultado_mant,importe_insumos)
            elif tipo == 2:
                cantidad_horas_parada = int(campos[4])
                importe_cobro_tecnico = float(campos[5])
                mantenimiento = Correctivo(tipo,fecha,operario,importe_repuestos,cantidad_horas_parada,importe_cobro_tecnico)
            self.mantenimientos.append(mantenimiento)
        archivo.close()

    def suma_gastos(self):
        total = 0
        for mantenimiento in self.mantenimientos:
            total += mantenimiento.gasto_manteminiento()
        return total

    def cantidad_mant_caros(self):
        cantidad = 0
        for mantenimineto in self.mantenimientos:
            if mantenimineto.gasto_manteminiento() > 10000:
                cantidad += 1
        return cantidad

    def rotura_mas_larga(self):
        primero = True
        fecha = None
        nombre = None
        for mantenimiento in self.mantenimientos:
            if mantenimiento.tipo == 2:
                if primero:
                    mayor = mantenimiento.cantidad_horas_parada
                    nombre = mantenimiento.operario
                    fecha = mantenimiento.fecha
                else:
                    if mantenimiento.   cantidad_horas_parada > mayor:
                        nombre = mantenimiento.operario
                        fecha = mantenimiento.fecha
                        mayor = mantenimiento.cantidad_horas_parada
        
        return f"| Nombre: {nombre} | Fecha: {fecha} |"

        
