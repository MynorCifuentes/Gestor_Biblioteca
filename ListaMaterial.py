from Nodo import * 

class listaMaterial:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self,libro):
        nuevoLibro = Nodo(libro)
        if not self.cabeza:
            self.cabeza = nuevoLibro
        else: 
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevoLibro

    def buscar(self, titulo):
        actual = self.cabeza
        while actual:
            if actual.libro.titulo == titulo:
                return actual.libro
            actual = actual.siguiente

        return 'No se encontro el titulo que busca'

    def mostrar_todos(self):
        actual = self.cabeza
        if not actual:
            print("No hay libros registrados.")
        while actual:
            actual.libro.mostrar_info()
            actual = actual.siguiente
