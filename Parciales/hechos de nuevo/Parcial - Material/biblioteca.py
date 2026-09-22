from libro import Libro
from ebook import Ebook
from revista import Revista

class Biblioteca():
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.materiales = []
        self.cargar_materiales()
    
    
    def cantidad_materiales(self):
        return self.materiales
    
    #1. Cargar materiales desde el archivo.
    def cargar_materiales(self):
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
                valor_venta = float(campos[5])
                material = Ebook(codigo,titulo,autor,precio_base,valor_venta)
            elif tipo == 3:
                origen = campos[5]
                material = Revista(codigo,titulo,autor,precio_base,origen)
            self.materiales.append(material)
   
    #2. Calcular el promedio entero de los precios base de todos.
    def calcular_promedio_precios_base(self):
        total = 0
        cantidad = 0

        for material in self.materiales:
            total += material.precio_base
            cantidad+=1
        if total == 0:
            return 0
        else: 
            return total // cantidad
    
    #3. Obtener el material con mayor costo de mantenimiento.
    def obtener_material_mayor_costo_mantenimiento(self):
        primero = True
        material = None
        for mat in self.materiales:
            if primero:
                mayor = mat.calcular_costo_mantenimiento()
                material = mat
                primero = False
            else:
                if mat.calcular_costo_mantenimiento() > mayor: 
                    mayor = mat.calcular_costo_mantenimiento()
                    material = mat
        return material    
    
    #4. Calcular la suma de costo de mantenimiento de todos los préstamos.
    def calcular_suma_costo_mantenimiento(self):
        total = 0
        for material in self.materiales:
            total += material.calcular_costo_mantenimiento()
        
        return total
        
    #5. Contar cuántos libros físicos se prestaron por más de 30 días.
    def contar_libros_mas_30_dias(self):
        cantidad = 0
        for material in self.materiales:
            if material.tipo == 1:
                if material.dias_prestados > 30:
                    cantidad += 1
        return cantidad

    #6. Contar cuántas revistas son importadas.
    def contar_revistas_importadas(self):
        cantidad = 0
        org = "importada"
        for material in self.materiales:
            if material.tipo == 3:
                if material.origen == org:
                    cantidad += 1
        return cantidad
    
    #7. Calcular en un diccionario la cantidad de materiales de cada tipo, las claves del diccionario deben ser "Libro", "Ebook" y "Revista".
    def cantidad_por_tipo(self):
        contador = {
            "Libro" : 0,
            "Ebook": 0,
            "Revista":0
        }

        for material in self.materiales:
            if material.tipo == 1:
                contador["Libro"] += 1
            elif material.tipo == 2:
                contador["Ebook"] += 1
            else: 
                contador["Revista"] += 1
        return contador


    
    