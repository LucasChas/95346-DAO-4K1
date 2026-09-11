# Producto de una tienda
# Crear una clase Producto que permita almacenar código, descripción, precio y stock. Implementar el constructor y 
# __str__(). Agregar un método hay_stock() que indique si existen unidades disponibles y un método valor_stock() que
# calcule el valor total de las unidades almacenadas. Crear dos productos y mostrar sus datos.


class Producto():
    def __init__(self, codigo, descripcion, precio, stock):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"El codigo es: {self.codigo} | Descripcion: {self.descripcion} | Precio: ${self.precio} | Stock: {self.stock}"

    def hay_stock(self):
        if self.stock > 0:
            return f"El producto: {self.descripcion}, tiene unidades disponibles ({self.stock})"
        else:
            return f"El producto: {self.descripcion}, no tiene unidades disponibles"

    def valor_stock(self):
        return self.stock*self.precio


def main():
    n = 0
    array_productos = []
    valor_total_unidades_almacenadas = 0
    while n < 2:
        n += 1

        codigo = int(input("Ingrese un codigo de producto: "))
        descripcion = input("Ingrese la descripción del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese la cantidad de unidades del producto: "))
        print("-"*50)
        Producto_n = Producto(codigo,descripcion,precio,stock)
        array_productos.append(Producto_n)

    print("Los productos registrados son:")
    
    for i in array_productos:
        print(i)
        print("-"*80)

    print("Metricas del sistema:")
    for i in array_productos:
        print(i.hay_stock())
        print(f"El valor del stock es: ${i.valor_stock()}")
        valor_total_unidades_almacenadas += i.valor_stock()

    print(f"El valor total de las unidades almacenadas es de: {valor_total_unidades_almacenadas}")
    

main()