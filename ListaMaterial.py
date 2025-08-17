from Nodo import * 

class listaMaterial:
    def __init__(self):
        self.inicio = None

    def agregarMaterial(self, material):
        nuevo_nodo = Nodo(material)
        if not self.inicio:
            self.inicio = nuevo_nodo
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def obtenerPorPosicion(self, posicion):
        actual = self.inicio
        index = 1
        while actual:
            if index == posicion:
                return actual.libro
            actual = actual.siguiente
            index += 1
        return None

    def contar(self):
        actual = self.inicio
        total = 0
        while actual:
            total += 1
            actual = actual.siguiente
        return total

    def recorrer(self, funcion):
        actual = self.inicio
        index = 1
        while actual:
            funcion(actual.libro, index)
            actual = actual.siguiente
            index += 1