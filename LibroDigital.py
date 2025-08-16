from MaterialBiblioteca import *
class LibroDigital(MaterialBiblioteca):
    def __init__(self, id, titulo, autor, estado, size):
        super.__init__(id, titulo, autor, estado)
        self.__size = size
    
    def PrestarMaterial():
        pass
    
    def DevolverMaterial():
        pass
    
    def MostrarInformacion(self):
        super().MostrarInformacion()
        print(f'Tamaño: {self.__size} MB')
