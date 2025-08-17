from MaterialBiblioteca import *
class LibroDigital(MaterialBiblioteca):
    def __init__(self, titulo, autor, size):
        super().__init__(titulo, autor)
        self.__size = size

    def getSize(self):
        return self.__size

    def setSize(self, size):
        self.__size = size
    
    def dias_max(self):
        return 3


    def prestarMaterial(self, dias):
        if self.getEstado() == "Prestado":
            print("El material ya está prestado.")
            return False
        if dias > self.dias_max():
            print(f"No se puede prestar por más de {self.dias_max()} días.")
            return False
        self.setEstado("Prestado")
        self.setDiasPrestamo(dias)
        print(f"Material prestado por {dias} días.")
        return True

    def devolverMaterial(self):
        if self.getEstado() == "Disponible":
            print("El libro ya está disponible.")
            return False
        self.setEstado("Disponible")
        self.setDiasPrestamo(0)
        print("Gracias por devolver el libro!!!.")
        return True
    
    def MostrarInformacion(self):
        print(f"Tipo: Libro Digital")
        print(f"Código: {self.getId()}")
        print(f"Título: {self.getTitulo()}")
        print(f"Autor: {self.getAutor()}")
        print(f"Tamaño del archivo: {self.getSize()} MB")
        print(f"Estado: {self.getEstado()}")
        print(f"Días máximos de préstamo: {self.dias_max()}")
