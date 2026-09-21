from hiper import Hiper
from mini import Mini
from super import Super

class Empresa():
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.sucursales = []
        self.cargar_sucursales()

    def cargar_sucursales(self):
        archivo = open(self.nombre_archivo, "rt")
        for linea in archivo:
            campos = linea[:-1].split(",")
            tipo = int(campos[0])
            numero = int(campos[1])
            superficie = int(campos[2])
            facturacion = float(campos[3])
            if tipo == 1:
                #hipermercado
                importe_g_alquiler = float(campos[4])
                sucursal = Hiper(tipo,numero,superficie,facturacion,importe_g_alquiler)
            elif tipo == 2: 
                #Supermercado
                es_mayorista = int(campos[4])
                sucursal = Super(tipo,numero,superficie,facturacion,
                es_mayorista )
            elif tipo == 3:
                importe_p_alquiler = float(campos[4])
                sucursal = Mini(tipo,numero,superficie,facturacion,importe_p_alquiler )
            self.sucursales.append(sucursal)
        archivo.close()


    def suma_ganancias(self):
        total = 0
        for sucursal in self.sucursales:
            total += sucursal.resultado_comercial()
        return total

    def cantidad_locales_no_rentables(self):
        cantidad = 0
        for sucursal in self.sucursales:
            if sucursal.tipo == 1:
                    if sucursal.indice_rentabilidad() < 50:
                        cantidad+=1
            elif sucursal.tipo == 2:
                    if sucursal.es_mayorista == 1:
                        if sucursal.indice_rentabilidad() <= 45:
                            cantidad += 1
                    else:
                        if sucursal.indice_rentabilidad() <= 40:
                            cantidad += 1
            elif sucursal.tipo == 3:
                    if sucursal.indice_rentabilidad() < 35:
                        cantidad += 1
        return cantidad

    def local_mas_rentable(self):
        primero = True
        numero = None
        tipo_sucursal = None
        for sucursal in self.sucursales:
            if primero: 
                primero = False
                mayor = sucursal.indice_rentabilidad()
                numero = sucursal.numero
                tipo_sucursal = sucursal.tipo
            else:
                if mayor < sucursal.indice_rentabilidad():
                    mayor = sucursal.indice_rentabilidad()
                    numero = sucursal.numero
                    tipo_sucursal = sucursal.tipo   
        return f"\n | Número: {numero} | Tipo de comercio: { 'Hipermercado' if tipo_sucursal == 1 else ( 'Supermercado' if tipo_sucursal == 2 else 'Minimercado')} | "
 