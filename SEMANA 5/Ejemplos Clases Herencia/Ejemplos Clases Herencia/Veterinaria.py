class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Cliente:
    def __init__(self, numero_cliente, nombre, antiguedad, mascota):
        self.numero_cliente = numero_cliente
        self.nombre = nombre
        self.antiguedad = antiguedad
        self.mascota = mascota

# Crear una lista para almacenar los datos de los clientes
clientes = []

# Solicitar al usuario la cantidad de clientes a ingresar
cantidad_clientes = int(input("Ingrese la cantidad de clientes a registrar: "))

# Pedir datos de los clientes y sus mascotas y crear instancias
for i in range(cantidad_clientes):
    print(f"Ingresando datos del cliente {i + 1}:")
    numero_cliente = int(input("Número de cliente: "))
    nombre_cliente = input("Nombre del cliente: ")
    antiguedad = int(input("Antigüedad (años): "))

    print(f"Ingresando datos de la mascota de {nombre_cliente}:")
    nombre_mascota = input("Nombre de la mascota: ")
    edad_mascota = int(input("Edad de la mascota: "))

    mascota = Mascota(nombre_mascota, edad_mascota)
    cliente = Cliente(numero_cliente, nombre_cliente, antiguedad, mascota)
    clientes.append(cliente)

# Informe 1: Cantidad de clientes
cantidad_total_clientes = len(clientes)
print(f"\nCantidad total de clientes: {cantidad_total_clientes}")

# Informe 2: Promedio de edad de las mascotas
suma_edades_mascotas = sum(cliente.mascota.edad for cliente in clientes)
promedio_edad_mascotas = suma_edades_mascotas / cantidad_total_clientes
print(f"Promedio de edad de las mascotas: {promedio_edad_mascotas:.2f} años")

# Informe 3: Clientes con antigüedad mayor o igual a 5 años
clientes_antiguedad_5_anios = [cliente for cliente in clientes if cliente.antiguedad >= 5]
cantidad_clientes_antiguedad_5_anios = len(clientes_antiguedad_5_anios)
print(f"Cantidad de clientes con antigüedad mayor o igual a 5 años: {cantidad_clientes_antiguedad_5_anios}")

# Informe 4: Clientes con mascotas mayores de 5 años
clientes_mascotas_mayor_5_anios = [cliente for cliente in clientes if cliente.mascota.edad > 5]
print("\nClientes cuyas mascotas tienen más de 5 años:")
for cliente in clientes_mascotas_mayor_5_anios:
    print(f"Nombre del cliente: {cliente.nombre}")
    print(f"Antigüedad del cliente: {cliente.antiguedad} años")
    print(f"Nombre de la mascota: {cliente.mascota.nombre}")
    print(f"Edad de la mascota: {cliente.mascota.edad} años")
    print("-" * 20)
