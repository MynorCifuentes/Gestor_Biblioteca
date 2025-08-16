from MaterialBiblioteca import *
class LibroFisico(MaterialBiblioteca):
    def __init__(self, id, titulo, autor, estado, NoEjemplar):
        super().__init__(id, titulo, autor, estado)
        self.__noEjemplar = NoEjemplar
        
    def PrestarMaterial(self):
        if self.getEstado() == "Disponible":
            self.setEstado("Prestado")
            print(f"Ejemplar {self.__noEjemplar} ha sido prestado.")
            return True
        print(f"Ejemplar {self.__noEjemplar} no está disponible para prestar.")
        return False

    def DevolverMaterial(self):
        if self.getEstado() == "Prestado":
            self.setEstado("Disponible")
            print(f"El ejemplar {self.__noEjemplar} ha sido devuelto.")
            return True
        print(f"El ejemplar {self.__noEjemplar} no está prestado.")
        return False

    def MostrarInformacion(self):
        print(f"---------------------Información del Libro Físico---------------------")
        print(f"Título: {self.getTitulo()} \n Autor: {self.getAutor()} \n Estado: {self.getEstado()} \n Número de Ejemplar: {self.__noEjemplar}")

