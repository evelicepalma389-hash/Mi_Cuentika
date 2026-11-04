from src.business.producto_service import obtener_productos, obtener_categorias, registrar_producto


def mostrar_productos():
    print("\n======================================")
    print("          MI CUENTIKA")
    print("          INVENTARIO")
    print("======================================")

    productos = obtener_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        print("--------------------------------------")
        print("Código:", producto["prod_id"])
        print("Producto:", producto["prod_nombre"])
        print("Unidad:", producto["prod_unidad"])
        print("Precio de compra: C$", producto["prod_precio_compra"])
        print("Precio de venta: C$", producto["prod_precio_venta"])
        print("Existencias:", producto["prod_stock"])
        print("Categoría:", producto["cat_nombre"])

    print("--------------------------------------")
    print("Total de productos:", len(productos))


def registrar_producto_pantalla():
    print("\n======================================")
    print("       REGISTRAR PRODUCTO")
    print("======================================")

    categorias = obtener_categorias()

    if not categorias:
        print("No se puede registrar sin categorías.")
        return

    print("\nCATEGORÍAS DISPONIBLES:")

    for categoria in categorias:
        print(categoria["cat_id"], "-", categoria["cat_nombre"])

    print("\nIngrese los datos del producto:")

    nombre = input("Nombre: ")
    unidad = input("Unidad (Unidad, Libra, Litro, etc.): ")
    precio_compra = input("Precio de compra: ")
    precio_venta = input("Precio de venta: ")
    stock = input("Existencias: ")
    stock_minimo = input("Stock mínimo: ")
    cat_id = input("Código de categoría: ")

    nuevo_id = registrar_producto(
        nombre,
        unidad,
        precio_compra,
        precio_venta,
        stock,
        stock_minimo,
        cat_id
    )

    if nuevo_id:
        print("Código del producto registrado:", nuevo_id)


if __name__ == "__main__":
    while True:
        print("\n========== MI CUENTIKA ==========")
        print("1. Mostrar inventario")
        print("2. Registrar producto")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_productos()

        elif opcion == "2":
            registrar_producto_pantalla()

        elif opcion == "3":
            print("Gracias por utilizar Mi Cuentika.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")