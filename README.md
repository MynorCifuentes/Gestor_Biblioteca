# Gestor_Biblioteca

El gestor de una biblioteca gestiona el prestamos de sus materiales bibliográficos de manera sencilla. 

El sistema debe de diferenciar entre materiales físicos y digitales.

## Especificaciones

El sistema cuenta con una clase padre 
## **MaterialBiblioteca**
### Atributos:
* Título
* Autor
* Código Único (Alfanumérico 8 caracteres)
* Estado del préstamo
### Métodos
* Prestar el material
* Devolverlo
* Mostrar su información general

## Clases Hijas
### Libro Físico
Atributos:
* Número de Ejemplar\
Este tipo de libro puede ser prestado por un máximo de 7 días

### Libro Digital
Atributos:
* Tamaño Archivo (MB) \
Este tipo de libro puede ser prestado por un máximo de 3 días


Para hacer funcional el sistema, debe implementarse un menú interactivo en consola que permita:

* Registrar nuevos materiales (fisicos o digitales)
* Gestionar materiales ya registrados
    * Prestar
    * Devolver
    * Consultar información de cada uno

El sistema debe estar diseñado de  anera que se mantenga en ejecución hasta que el usuario decida salir. 





