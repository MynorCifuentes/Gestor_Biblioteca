from MaterialBiblioteca import *
from LibroFisico import * 
from LibroDigital import * 

class Biblioteca:
    pass

def menu_principal():
    print("\n---------------------Bienvenido a la Biblioteca IPC2---------------------")
    print("1. Registrar material bibliotecario")
    print("2. Gestionar material bibliotecario")
    print("3. Salir")

def menu_gestion_material():
    print("\nGestión de Material Bibliotecario")
    print("1. Prestar material")
    print("2. Devolver material")
    print("3. Consultar información de cada material")
    print("4. Volver al menú principal")

def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("Función para registrar materiales (no implementada).")
        elif opcion == "2":
            while True:
                menu_gestion_material()
                subopcion = input("Seleccione una opción: ")
                if subopcion == "1":
                    print("Función para prestar material (no implementada).")
                elif subopcion == "2":
                    print("Función para devolver material (no implementada).")
                elif subopcion == "3":
                    print("Función para consultar información (no implementada).")
                elif subopcion == "4":
                    break
                else:
                    print("Opción no válida.")
        elif opcion == "3":
            print("¡Gracias por visitar la Biblioteca IPC2!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()