from empleado import Empleado
from empleado_contrato import Contrato
from empleado_planta import Planta
from empleado_vendedor import Vendedor


class Empresa():
    def __init__(self):
        self.empleados = []
        self.cargar_archivo()
    #1)Cargar los empleados desde el archivo llamado empleados.csv.
    def cargar_archivo(self):
        archivo = open ("./empleados.csv", "rt")
        for linea in archivo: 
            campos = linea[:-1].split(",")
            tipo = int(campos[0])
            codigo = int(campos[1])
            nombre = campos[2] + " " + campos[3]
            salario_base = float(campos[4])

            if tipo == 1:
                antiguedad = int(campos[5])
                empleado = Planta(tipo,codigo,nombre,salario_base,antiguedad)
            elif tipo == 2: 
                cantidad_proyectos = int(campos[5])
                empleado = Contrato(tipo,codigo,nombre,salario_base,cantidad_proyectos)
            else:
                ventas = float(campos[5])
                empleado = Vendedor(tipo,codigo,nombre,salario_base,ventas) 
            self.empleados.append(empleado)
    #2) Calcular el salario total de cada empleado, teniendo en cuenta las bonificaciones o comisiones según su tipo.
    def salario_total_por_empleado(self):
        for emp in self.empleados:
            print(f"El salario total del empleado: {emp.nombre}, es de: ${round(emp.calcular_salario(),2)}")
    #3) Calcular el total a pagar en salarios sumando los salarios de todos los empleados.
    def total_a_pagar(self):
        acum = 0
        for emp in self.empleados:
            acum += emp.calcular_salario()
        return print(f"El total a pagar por los salrios es de: ${acum}")

    #4) Obtener el nombre del empleado con el salario más bajo.
    def emp_salario_mas_bajo(self):
        primero = True
        nombre = None
        for emp in self.empleados:
            if primero:
                menor = emp.calcular_salario()
                primero = False
                nombre = emp.nombre
            else:
                if emp.calcular_salario() < menor:
                    menor = emp.calcular_salario()
                    nombre = emp.nombre
        return print(f"El nombre del empleado con el salario más bajo es {nombre} siendo de: ${menor}")
    #5) Contar cuántos empleados de planta cumplen con la bonificación por antigüedad (más de 5 años).
    def empleados_antiguedad_cumplida(self):
        cont = 0
        for emp in self.empleados:
            if emp.tipo == 1:
                if emp.años_antiguedad > 5:
                    cont += 1
        return print(f"La cantidad de empleados con mas de 5 años de antigüedad y que reciben bonificación es de: {cont}")

    #6) Determinar cuántos empleados por contrato recibieron una prima por proyectos completados (más de 3).
    def cuantas_primas(self):
        cantidad = 0
        for emp in self.empleados:
            if emp.tipo == 2:
                if emp.proyectos_completados > 3:
                    cantidad += 1
        return print(f"La cantidad de empleados que reciben prima es de: {cantidad}")

def main():
        empresa = Empresa()
        print("-"*100)
        print("Salario total de cada empleado: ")
        empresa.salario_total_por_empleado()
        print("-"*100)
        empresa.total_a_pagar()
        print("-"*100)
        empresa.emp_salario_mas_bajo()
        print("-"*100)
        empresa.empleados_antiguedad_cumplida()
        print("-"*100)
        empresa.cuantas_primas()
        print("-"*100)
   
main()

     




