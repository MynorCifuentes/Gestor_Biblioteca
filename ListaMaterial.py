from Nodo import * 

class listaMaterial:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self,material):
        nuevoMaterial = Nodo(material)
        if not self.cabeza:
            self.cabeza = nuevoMaterial
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevoMaterial

    def buscar(self, titulo):
        actual = self.cabeza
        while actual:
            if actual.material.titulo == titulo:
                return actual.material
            actual = actual.siguiente

        return 'No se encontro el titulo que busca'

    def mostrar_todos(self):
        actual = self.cabeza
        if not actual:
            print("No hay libros registrados.")
        while actual:
            actual.libro.MostrarInformacion()
            actual = actual.siguiente
