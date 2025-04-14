# productos.py

inventario = []

def agregar_producto(nombre, precio, stock):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado con éxito.")

def listar_productos():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\nInventario:")
        for i, prod in enumerate(inventario, start=1):
            print(f"{i}. Nombre: {prod['nombre']}, Precio: ${prod['precio']}, Stock: {prod['stock']}")

def buscar_producto(nombre):
    encontrados = [prod for prod in inventario if prod['nombre'].lower() == nombre.lower()]
    if encontrados:
        print("\nProducto encontrado:")
        for prod in encontrados:
            print(f"Nombre: {prod['nombre']}, Precio: ${prod['precio']}, Stock: {prod['stock']}")
    else:
        print(f"No se encontró el producto con nombre '{nombre}'.")

def actualizar_stock(nombre, nuevo_stock):
    for prod in inventario:
        if prod['nombre'].lower() == nombre.lower():
            prod['stock'] = nuevo_stock
            print(f"Stock actualizado para '{nombre}': {nuevo_stock} unidades.")
            return
    print(f"No se encontró el producto con nombre '{nombre}'.")
