from src.data.producto_dal import listar_productos, insertar_producto, listar_categorias
from decimal import Decimal, InvalidOperation

def obtener_productos():
    try:
        productos = listar_productos()

        if not productos:
            print("No hay productos registrados.")
            return []

        return productos

    except Exception as error:
        print("Error en la lógica de negocio:", error)
        return []


def registrar_producto(nombre, unidad, precio_compra, precio_venta, stock, stock_minimo, cat_id):
    try:
        nombre = nombre.strip()
        unidad = unidad.strip()

        if not nombre or not unidad:
            print("El nombre y la unidad son obligatorios.")
            return None

        precio_compra = Decimal(str(precio_compra))
        precio_venta = Decimal(str(precio_venta))
        stock = Decimal(str(stock))
        stock_minimo = Decimal(str(stock_minimo))
        cat_id = int(cat_id)

        if precio_compra < 0 or precio_venta < 0:
            print("Los precios no pueden ser negativos.")
            return None

        if stock < 0 or stock_minimo < 0:
            print("Las existencias no pueden ser negativas.")
            return None

        if cat_id <= 0:
            print("La categoría no es válida.")
            return None

        nuevo_id = insertar_producto(
            nombre,
            unidad,
            precio_compra,
            precio_venta,
            stock,
            stock_minimo,
            cat_id
        )

        if nuevo_id:
            print("Producto registrado correctamente.")
            return nuevo_id

        return None

    except (ValueError, InvalidOperation):
        print("Error: verifica que los precios y existencias sean números válidos.")
        return None

    except Exception as error:
        print("Error en la lógica de negocio:", error)
        return None      
def obtener_categorias():
    try:
        categorias = listar_categorias()

        if not categorias:
            print("No hay categorías registradas.")
            return []

        return categorias

    except Exception as error:
        print("Error al consultar categorías:", error)
        return []