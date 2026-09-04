# import time


# nombre = input("Ingrese su nombre: ") 

# edad = int(input("Ingrese su edad: "))
# print("Validando datos...")
# time.sleep(2)
# if not nombre: print("No ingresó su nombre") 
# if not edad: print("Debe ingresar una edad diferente a 0") 
# print("Su edad es " + ("impar" if edad % 2 else "par"))

frutas = ["manzana", "banana", "naranja"]
 # Por cada fruta de la lista de frutas: for fruta in frutas: print(fruta)
for fruta in frutas: 
    print(fruta)


numero = int(input("Ingrese un número: "))
suma_digitos = 0
while numero > 0: # Obtiene el último dígito del número 
    digito = numero % 10
    # Agrega el dígito a la suma total 
    suma_digitos += digito
    # Elimina el último dígito del número 
    numero //= 10
print("La suma de los dígitos es:", suma_digitos)


texto = input("Ingrese un texto: ") 
for letra in texto: 
    if letra == "A": 
        print("Contiene la letra A") 
        break
else: print("No contiene la letra A")


def sumar(*numeros): 
    total = 0 
    for num in numeros: 
        total += num 
    return total 
resultado = sumar(1, 2, 3, 4, 5)
print("Resultado: ", resultado)
nombre = "Lucas"
Apellido = "Chas"
print(f"Hola {Apellido:^20}, {nombre}, como estás?")