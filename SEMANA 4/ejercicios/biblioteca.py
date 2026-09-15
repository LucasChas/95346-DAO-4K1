# Libro de una biblioteca
# Crear una clase Libro con título, autor, cantidad de páginas y estado de préstamo. Implementar el constructor y 
# __str__(). Agregar los métodos prestar() y devolver(). No debe ser posible prestar un libro que ya se encuentra
# prestado. Crear un libro y realizar algunas operaciones para comprobar su funcionamiento

class Libro():
    def __init__(self,titulo,autor,cant_paginas,estado_prestamo):
        self.titulo = titulo
        self.autor = autor
        self.cant_paginas = cant_paginas
        self.estado_prestamo = estado_prestamo

    def __str__(self):
        return f"| El titulo del libro es: {self.titulo} | \n | El autor del libro es: {self.autor} | \n | La cantidad de paginas del libro es de: {self.cant_paginas} | \n | El estado de prestamo del libro es de: {'Prestado' if self.estado_prestamo else 'Libre'} |"
    def prestar(self):
        if not self.estado_prestamo:
            self.estado_prestamo = True
            return True   # Se pudo prestar con éxito
        else:
            return False  # Ya estaba prestado, no se pudo
    def devolver(self):
        if self.estado_prestamo:
            self.estado_prestamo = False
            return True   # Se devolvió con éxito
        else:
            return False  # No estaba prestado, ya estaba libre

def menu():
    print("-"*100)
    print("Menu del sistema")
    print("Opcion 1 - Crear un Libro")
    print("Opcion 2 - Listar Libros creados")
    print("Opcion 3 - Prestar un libro")
    print("Opcion 4 - Devolver un libro")
    print("Opcion 0 - Cerrar sistema")
    print("-"*100)


def main():
    lista_libro = []
    while True:
        menu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1: 
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el nombre del autor del libro: ")
            cant_paginas = int(input("Ingrese la cantidad de paginas del libro: "))
            estado_prestamo = input("Ingrese el estado de prestamo del libro: (S = Prestado) (N = Libre)").strip().upper()
            while estado_prestamo not in ["S","N"]:
                print("Ingreso un valor incorrecto...")
                estado_prestamo = input("Ingrese el estado de prestamo del libro: (S = Prestado) (N = Libre)").strip().upper()
            estado = (estado_prestamo == "S")

            libro = Libro(titulo,autor,cant_paginas,estado)
            lista_libro.append(libro)
            print("-"*100)
            print("Libro creado exitosamente...")
        elif opcion == 2:
            print("Los libros registrdos son: ")
            for i, libro in enumerate(lista_libro):
                print("Libro: ", i + 1, "\n", libro)
                print("="*100)
        elif opcion == 3:
            # 1. Chequear si hay libros registrados
            if len(lista_libro) == 0:
                print("\nNo hay libros registrados en el sistema.")
            else:
                print("\n--- Libros disponibles en el sistema ---")
                for i, libro in enumerate(lista_libro):
                    estado_texto = "Prestado" if libro.estado_prestamo else "Libre"
                    print(f"{i + 1}. {libro.titulo} (Autor: {libro.autor}) - Estado: {estado_texto}")
                
                # 2. Pedir qué libro prestar
                indice = int(input("\nIngrese el número del libro que desea prestar: ")) - 1
                
                # 3. Validar que el índice exista en la lista
                if 0 <= indice < len(lista_libro):
                    libro_seleccionado = lista_libro[indice]
                    
                    # 4. Intentar prestar
                    if libro_seleccionado.prestar():
                        print(f"\n¡Éxito! El libro '{libro_seleccionado.titulo}' fue prestado.")
                    else:
                        print(f"\nNo se pudo realizar el préstamo: '{libro_seleccionado.titulo}' ya se encuentra prestado.")
                else:
                    print("\nNúmero de libro inválido.")  
        elif opcion == 4:
            # 1. Chequear si hay libros cargados
            if len(lista_libro) == 0:
                print("\nNo hay libros registrados en el sistema.")
            else:
                print("\n--- Libros en el sistema ---")
                for i, libro in enumerate(lista_libro):
                    estado_texto = "Prestado" if libro.estado_prestamo else "Libre"
                    print(f"{i + 1}. {libro.titulo} (Autor: {libro.autor}) - Estado: {estado_texto}")
                
                # 2. Pedir qué libro devolver
                indice = int(input("\nIngrese el número del libro que desea devolver: ")) - 1
                
                # 3. Validar el rango del índice
                if 0 <= indice < len(lista_libro):
                    libro_seleccionado = lista_libro[indice]
                    
                    # 4. Intentar devolver
                    if libro_seleccionado.devolver():
                        print(f"\n¡Éxito! El libro '{libro_seleccionado.titulo}' ha sido devuelto y ahora está Libre.")
                    else:
                        print(f"\nOperación inválida: El libro '{libro_seleccionado.titulo}' ya se encuentra libre en la biblioteca.")
                else:
                    print("\nNúmero de libro inválido.")
        elif opcion == 0:  
            print("Gracias por usar el sistema de biblioteca de ChasDays...")
            break
        else: 
            print("Ingreso una opcion incorrecta, Intente nuevamente...")


main()