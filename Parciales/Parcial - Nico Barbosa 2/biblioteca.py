from ebook import Ebook
from libro import Libro
from revista import Revista
class Biblioteca():
    def __init__(self,nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.lista_libros = []
        self.cargar_archivo()

    def cantidad_materiales(self):
        return self.lista_libros

    #1. Cargar materiales desde el archivo.
    def cargar_archivo(self):
        archivo = open(self.nombre_archivo, "rt")
        for linea in archivo:
            campos = linea[:-1].split(",")
            tipo = int(campos[0])
            codigo = campos[1]
            titulo = campos[2]
            autor = campos[3]
            precio_base = float(campos[4])
            if tipo == 1:
                dias_prestados = int(campos[5])
                material = Libro(codigo,titulo,autor,precio_base,dias_prestados)
            elif tipo == 2:
                venta = float(campos[5])
                material = Ebook(codigo,titulo,autor,precio_base,venta)
            else:
                importado = campos[5]
                material = Revista(codigo,titulo,autor,precio_base,importado)
            self.lista_libros.append(material)
    #2. Calcular el promedio entero de los precios base de todos.
    def calcular_promedio_precios_base(self):
        suma = 0
        cantidad = 0
        for material in self.lista_libros:
            suma += material.precio_base
            cantidad +=1
        return suma//cantidad

    #3. Obtener el material con mayor costo de mantenimiento. 
    def obtener_material_mayor_costo_mantenimiento(self):
        primero = True
        objeto = None
        for material in self.lista_libros:
            if primero:
                mayor = material.calcular_precio_mantenimiento()
                primero = False
                objeto = material
            else:
                if material.calcular_precio_mantenimiento() > mayor:
                    mayor = material.calcular_precio_mantenimiento()
                    objeto = material
        return objeto

    #4. Calcular la suma de costo de mantenimiento de todos los préstamos.

    def calcular_suma_costo_mantenimiento(self):
        suma = 0
        for material in self.lista_libros:
            suma += material.calcular_precio_mantenimiento()
        return suma

    #5. Contar cuántos libros físicos se prestaron por más de 30 días.
    def contar_libros_mas_30_dias(self):
        cantidad = 0
        for material in self.lista_libros:
            if material.tipo == 1:
                if material.dias_prestados > 30:
                    cantidad += 1
        return cantidad

    #6. Contar cuántas revistas son importadas.
    def contar_revistas_importadas(self):
        cantidad = 0
        for material in self.lista_libros:
            if material.tipo == 3:
                if material.importacion == "importada":
                    cantidad += 1
        return cantidad

    #7. Calcular en un diccionario la cantidad de materiales de cada tipo, las claves del diccionario deben ser "Libro", "Ebook" y "Revista".
    def cantidad_por_tipo(self):
        conteo = {
            "Libro" : 0,
            "Ebook" : 0,
            "Revista": 0 
        }

        for material in self.lista_libros:
            if material.tipo == 1:
                conteo["Libro"] += 1
            elif material.tipo == 2:
                conteo["Ebook"] += 1
            else:
                conteo["Revista"] += 1
        return conteo


        
