# 1.6.1 Estación de servicio
# Una estación de servicio que dispone de 10 surtidores y necesita gestionar
# información relacionada con la venta de combustibles en la jornada.
# De cada surtidor se conoce:
# • Número de Surtidor (validar que sea un número entre 1 y 30)
# • Cantidad: representa la cantidad de litros de combustible vendido por
# el surtidor (validar que sea un número positivo)
# • Tipo: representa el tipo de combustible del surtidor. Los valores que pue-
# de asumir son 1 representa “Nafta Super”, 2 representa “Nafta Especial”
# y 3 representa “Gasoil” (validar que se ingresen valores válidos).
# Se pide calcular e imprimir:
# • El total de litros vendidos en la jornada, por tipo de combustible.
# • El número de surtidor que menos combustible vendió.
# • El promedio por surtidor en litros de combustible vendido en la jornada
# (promedio general, es un único resultado).

total_nafta_super = total_nafta_especial = total_gasoil = 0
surtidor_menor = None
menor= None
total=0
for i in range(10):
    numero_surtidor = int(input("Ingresa el numero del surtidor: "))
    while not 0 < numero_surtidor <= 30: 
       numero_surtidor = int(input("Error debe ser un número entre 1 y 30, Ingresa el numero del surtidor: ")) 
    cantidad = int(input("Ingrese la cantidad de litros: "))
    while cantidad < 0:
        cantidad = int(input("Error debe ser un número positivo, Ingresa la cantidad de litros: "))  
    tipo = int(input("Ingrese el tipo de combustible: "))
    while not 1 <= tipo <= 3:
        tipo = int(input("Error debe ser un número entre 1 y 3 , Ingresa el tipo de combustible: ")) 
    if tipo == 1:
        total_nafta_super += cantidad
    elif tipo == 2:
        total_nafta_especial += cantidad   
    else: 
        total_nafta_especial += cantidad


    if not menor or cantidad < menor:
        menor = cantidad
        surtidor_menor = numero_surtidor

total = total_nafta_super + total_nafta_especial + total_gasoil 
promedio = total//10

print("El total de litros vendidos en la jornada, por tipo de combustible")
print("-"*50)
print("Nafta super: ", total_nafta_super, "litros")
print("Nafta Especial: ", total_nafta_especial, "litros")
print("Gasoil: ", total_gasoil, "litros")
print("-"*50)
print(f"Surtidor que menos litros vendió: {surtidor_menor}")
print(f"Promedio de litros por surtidor: {promedio}")