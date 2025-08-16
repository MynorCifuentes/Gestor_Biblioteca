from MaterialBiblioteca import *
from LibroFisico import * 
from LibroDigital import * 
from ListaMaterial import *

class Biblioteca:
    pass

ListaLibroFisico = listaMaterial()
ListaLibroDigital = listaMaterial()

def menu_principal():
    print("\n---------------------Bienvenido a la Biblioteca IPC2---------------------")
    print("1] Registrar material bibliotecario")
    print("2] Gestionar material bibliotecario")
    print("3] Salir")

def menu_registro_material():
    print("\n---------------------¿Qué tipo de libro desea registrar?---------------------")
    print("1] Libros Fisicos")
    print("2] Libros Digitales")
    print("3] Regresar al menu principal")

def menu_gestion_material():
    print("\n---------------------Gestión de Material Bibliotecario---------------------")
    print("1] Prestar material")
    print("2] Devolver material")
    print("3] Consultar información de cada material")
    print("4] Volver al menú principal")

def menu_prestamo_material():
    print("\n---------------------Préstamo Material---------------------")
    print("1] Libro Físico")
    print("2] Libro Digital")
    print("3] Volver al menú Gestión de Material")

def menu_devolver_material():
    print("\n---------------------Devolución Material---------------------")
    print("1] Libro Físico")
    print("2] Libro Digital")
    print("3] Volver al menú Gestión de Material")

def menu_informacion_material():
    print("\n---------------------Información Material---------------------")
    print("1] Catálogo Libros Físicos")
    print("2] Catálogo Libros Digitales")
    print("3] Catálogo Completo")
    print("4] Volver al menú Gestión de Material")

def registroLibroFisico():
    pass

def registroLibroDigital():
    pass    

def prestarLibroFisico():
    pass

def prestarLibroDigital():
    pass

def devolverLibroFisico():
    pass

def devolverLibroDigital():
    pass

def informacionLibroFisico():
    pass

def informacionLibroDigital():
    pass

def informacionTodo():
    pass

def main():
    while True:  
        menu_principal()
        opcion = input("Seleccione una opción: ")
        if opcion == "1": #Menu de registro de Material
            while True:
                menu_registro_material()
                OpcionRegistro = input("¿Qué tipo de libro desea registrar?")
                if OpcionRegistro == "1":
                    registroLibroFisico()
                elif OpcionRegistro == "2":
                    registroLibroDigital()
                elif OpcionRegistro == "3":
                    break
                else:
                    print("\nOpción no válida.")

        elif opcion == "2": #Menu de Gestion de Material
            while True:
                menu_gestion_material()
                opcionGestion = input("Seleccione una opción: ")
                if opcionGestion == "1": #Menu prestar Material
                    while True:
                        menu_prestamo_material()
                        OpcionPrestamo = input("¿Qué tipo de libro desea Prestar?")
                        if OpcionPrestamo == "1": #Prestamo libro fisico
                            prestarLibroFisico()
                        elif OpcionPrestamo == "2": #Prestamo libro digital
                            prestarLibroDigital()
                        elif OpcionPrestamo == "3":
                            break
                        else:
                            print("\nOpción no válida.")
                elif opcionGestion == "2": #Menu devolver Material 
                    while True:
                        menu_devolver_material()
                        OpcionDevolver = input("¿Qué tipo de libro desea devolver?")
                        if OpcionDevolver == "1": #Devolver libro fisico
                            devolverLibroFisico()
                        elif OpcionDevolver == "2": #Devolver libro digital
                            devolverLibroDigital()
                        elif OpcionDevolver == "3":
                            break
                        else:
                            print("\nOpción no válida.")
                elif opcionGestion == "3": #Menu consultar Informacion
                    while True:
                        menu_informacion_material()
                        OpcionInformacion = input("¿Qué tipo de libro desea devolver?")
                        if OpcionInformacion == "1": #Informacion libro fisico
                            informacionLibroFisico()
                        elif OpcionInformacion == "2": #Informacion libro digital
                            informacionLibroDigital()
                        elif OpcionInformacion == "3": #Informacion Catálogo Completo
                            informacionTodo()
                        elif OpcionInformacion == "4":
                            break
                        else:
                            print("\nOpción no válida.")
                elif opcionGestion == "4":
                    break
                else:
                    print("Opción no válida.")
        elif opcion == "3":
            print("¡Gracias por visitar la Biblioteca IPC2!")
            break
        else:
            print("\nOpción no válida.")

if __name__ == "__main__":
    main()