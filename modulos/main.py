# main.py

import productos

def mostrar_menu():
    print("\n=== MENÚ DE INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto por nombre")
    print("4. Actualizar stock")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        stock = int(input("Cantidad en stock: "))
        productos.agregar_producto(nombre, precio, stock)

    elif opcion == "2":
        productos.listar_productos()

    elif opcion == "3":
        nombre = input("Nombre del producto a buscar: ")
        productos.buscar_producto(nombre)

    elif opcion == "4":
        nombre = input("Nombre del producto a actualizar: ")
        nuevo_stock = int(input("Nuevo stock: "))
        productos.actualizar_stock(nombre, nuevo_stock)

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
