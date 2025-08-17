from abc import ABC, abstractmethod
import random
import string


class MaterialBiblioteca(ABC):
    def __init__(self, titulo, autor):
        self.__id = self.setId()
        self.__titulo = titulo
        self.__autor = autor
        self.__estado = "Disponible"
        self.__diasPrestado = 0
    
    def setId(self):
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choices(caracteres, k=8))

    def getId(self):
        return self._id

    
    def setTitulo(self, titulo):
        self.__titulo = titulo
        
    def setAutor(self, autor):
        self.__autor = autor
    
    def setEstado(self, estado):
        self.__estado = estado
    

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getEstado(self):
        return self.__estado
    
    @abstractmethod
    def PrestarMaterial(self, dias):
        pass
    
    @abstractmethod
    def dias_max(self): #Dias maximos, polimorfimo 
        pass
  
    
    @abstractmethod
    def DevolverMaterial(self):
        pass
    
    @abstractmethod
    def MostrarInformacion(self):
        pass

    