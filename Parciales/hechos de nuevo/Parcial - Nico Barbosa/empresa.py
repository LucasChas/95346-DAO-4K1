from vendedor import Vendedor
from contratado import Contratado
from planta import Planta

class Empresa():
    def __init__(self,nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.empleados = []
        self.cargar_empleados()
        
    #1
    def cargar_empleados(self):
        archivo = open(self.nombre_archivo, "rt")
        for linea in archivo:
            campos = linea[:-1].split(",")
            tipo = int(campos[0])
            codigo = int(campos[1])
            nombre = f"{campos[2]} {campos[3]}"
            salario_base = float(campos[4])
            if tipo == 1:
                años_antiguedad = int(campos[5])
                empleado = Planta(tipo,codigo,nombre,salario_base,años_antiguedad)

            elif tipo == 2:
                proyectos_completados = int(campos[5])
                empleado = Contratado(tipo,codigo,nombre,salario_base,proyectos_completados)

            else:
                total_ventas = int(campos[5])
                empleado = Vendedor(tipo,codigo,nombre,salario_base,total_ventas)
            self.empleados.append(empleado)
        archivo.close()

    #2
    def salario_total_por_tipo(self):
        contador = {
            "Planta" : 0,
            "Contratado": 0,
            "Vendedor": 0
        }

        for empleado in self.empleados:
            if empleado.tipo == 1:
                contador["Planta"] += empleado.calcular_salario()
            elif empleado.tipo == 2:
                contador["Contratado"] += empleado.calcular_salario()
            elif empleado.tipo == 3:
                contador["Vendedor"] += empleado.calcular_salario()
        return contador
    
    #3
    def calcular_salario_total(self):
        total = 0

        for empleado in self.empleados:
            total += empleado.calcular_salario()
        return total

    #4
    def empleado_salario_mas_bajo(self):
        nombre = None
        primero = True

        for empleado in self.empleados:
            if primero:
                primero = False
                bajo = empleado.calcular_salario()
                nombre = empleado.nombre
            elif empleado.calcular_salario() < bajo:
                bajo = empleado.calcular_salario()
                nombre = empleado.nombre
        return nombre

    #5
    def empleados_mas_5_años_antiguedad(self):
        cantidad = 0
        for empleado in self.empleados:
            if (empleado.tipo == 1) and (empleado.años_antiguedad > 5):
                cantidad += 1
        return cantidad
    #6
    def empleados_que_reciben_prima(self): 
        cantidad = 0
        for empleado in self.empleados:
            if (empleado.tipo == 2) and (empleado.proyectos_completados > 3):
                cantidad += 1
        return cantidad




