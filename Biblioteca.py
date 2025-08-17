from ListaMaterial import listaMaterial
from LibroFisico import LibroFisico
from LibroDigital import LibroDigital

class Biblioteca:
    def __init__(self):
        self.lista = listaMaterial()

    def mostrar_menu(self):
        print("\n-------------------Biblioteca IPC2 -------------------")
        print("1. Registrar nuevo material")
        print("2. Gestionar materiales")
        print("3. Listar todos los materiales")
        print("4. Salir")

    def registrar_material(self):
        print("\nRegistrar material")
        print("a) Libro Físico")
        print("b) Libro Digital")
        tipo = input("Seleccione tipo (a/b): ").strip().lower()
        titulo = input("Título: ")
        autor = input("Autor: ")
        if tipo == 'a':
            NoEjemplar = input("Número de ejemplar: ")
            libro = LibroFisico(titulo, autor, NoEjemplar)
            self.lista.agregarMaterial(libro)
            print(f"Libro Físico registrado con código: {libro.getId()}")
        elif tipo == 'b':
            size = input("Tamaño de archivo (MB): ")
            try:
                size = float(size)
            except ValueError:
                print("Tamaño inválido.")
                return
            libro = LibroDigital(titulo, autor, size)
            self.lista.agregarMaterial(libro)
            print(f"Libro Digital registrado con código: {libro.getId()}")
        else:
            print("Opción inválida.")

    def gestionar_material(self):
        total = self.lista.contar()
        if total == 0:
            print("No hay materiales registrados.")
            return
        print("\n-------------------Lista de Materiales-------------------")
        def mostrar(material, idx):
            print(f"{idx}. {material.getTitulo()} ({material.getAutor()}) - {material.getEstado()}")
        self.lista.recorrer(mostrar)
        try:
            seleccion = int(input("Seleccione el número del material a gestionar: "))
        except ValueError:
            print("Selección inválida.")
            return
        material = self.lista.obtenerPorPosicion(seleccion)
        if material is None:
            print("No existe material en esa posición.")
            return
        print("\n--- Gestión de Material ---")
        print("1. Prestar material")
        print("2. Devolver material")
        print("3. Mostrar información")
        opcion = input("Seleccione opción: ").strip()
        if opcion == '1':
            try:
                dias = int(input("Ingrese número de días de préstamo: "))
            except ValueError:
                print("Días inválidos.")
                return
            material.prestarMaterial(dias)
        elif opcion == '2':
            material.devolverMaterial()
        elif opcion == '3':
            material.MostrarInformacion()
        else:
            print("Opción inválida.")

    def listar_materiales(self):
        print("\n--- Materiales registrados ---")
        if self.lista.contar() == 0:
            print("No hay materiales registrados.")
            return
        def mostrar(material, idx):
            print(f"{idx}. {material.getTitulo()} ({material.getAutor()}) - {material.getEstado()}")
            material.MostrarInformacion()
            print("-----------------")
        self.lista.recorrer(mostrar)

def main():
    biblioteca = Biblioteca()
    while True:
        biblioteca.mostrar_menu()
        opcion = input("Seleccione opción: ").strip()
        if opcion == '1':
            biblioteca.registrar_material()
        elif opcion == '2':
            biblioteca.gestionar_material()
        elif opcion == '3':
            biblioteca.listar_materiales()
        elif opcion == '4':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()