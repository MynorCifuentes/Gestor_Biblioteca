from MaterialBiblioteca import *

class LibroFisico(MaterialBiblioteca):
    def __init__(self, titulo, autor, NoEjemplar):
        super().__init__(titulo, autor)
        self.__noEjemplar = NoEjemplar

    def get_NoEjemplar(self):
        return self.__noEjemplar

    def set_NoEjemplar(self, numero):
        self.__noEjemplar = numero

    def dias_max(self):
        return 7
        
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
            print("El material ya está disponible.")
            return False
        self.setEstado("Disponible")
        self.setDiasPrestamo(0)
        print("Material devuelto correctamente.")
        return True


    def MostrarInformacion(self):
        print(f"---------------------Información del Libro Físico---------------------")
        print(f"id: {self.getId()} \n Título: {self.getTitulo()} \n Autor: {self.getAutor()} \n Número de Ejemplar :{self.get_NoEjemplar()} \n Estado: {self.getEstado()} \n Días Máximos: {self.dias_max()}")

