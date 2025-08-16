from abc import ABC, abstractmethod

class MaterialBiblioteca(ABC):
    def __init__(self, id, titulo, autor, estado):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__estado = estado
    
    def setId(self, id):
        self.__id = id    
    
    def setTitulo(self, titulo):
        self.__titulo = titulo
        
    def setAutor(self, autor):
        self.__autor = autor
    
    def setEstado(self, estado):
        self.__estado = estado
    
    def getId(self):
        return self.__id
    
    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getEstado(self):
        return self.__estado
    
    @abstractmethod
    def PrestarMaterial():
        pass  
    
    @abstractmethod
    def DevolverMaterial():
        pass
    
    @abstractmethod
    def MostrarInformacion():
        pass