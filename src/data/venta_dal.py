from src.data.conexion import obtener_conexion
from decimal import Decimal


def registrar_venta(detalles):
    conexion = obtener_conexion()

    if conexion is None:
        return None

    cursor = None

    try:
        cursor = conexion.cursor()

        total = Decimal("0.00")
        productos = []
        cantidades_acumuladas = {}

        # Verificar existencias y obtener precios
        for detalle in detalles:

            prod_id = detalle["prod_id"]
            cantidad = Decimal(str(detalle["cantidad"]))

            consulta = """
                SELECT prod_stock, prod_precio_venta
                FROM TBL_PRODUCTO
                WHERE prod_id = %s
                FOR UPDATE
            """

            cursor.execute(consulta, (prod_id,))
            producto = cursor.fetchone()

            if producto is None:
                raise Exception("El producto no existe.")

            stock = Decimal(str(producto[0]))
            precio = Decimal(str(producto[1]))

            if cantidad <= 0:
                raise Exception("La cantidad debe ser mayor que cero.")

            cantidad_acumulada = (
                 cantidades_acumuladas.get(prod_id, Decimal("0.00")) + cantidad
            )

            if stock < cantidad_acumulada:
                raise Exception(
                    f"Existencias insuficientes para el producto {prod_id}."
                )

            cantidades_acumuladas[prod_id] = cantidad_acumulada
            subtotal = cantidad * precio
            total += subtotal

            productos.append({
                "prod_id": prod_id,
                "cantidad": cantidad,
                "precio": precio,
                "subtotal": subtotal
            })

        # Registrar la venta principal
        consulta_venta = """
            INSERT INTO TBL_VENTA (venta_total)
            VALUES (%s)
        """

        cursor.execute(consulta_venta, (total,))
        venta_id = cursor.lastrowid

        # Registrar detalles y actualizar inventario
        for producto in productos:

            consulta_detalle = """
                INSERT INTO TBL_DETALLE_VENTA (
                    venta_id,
                    prod_id,
                    detalle_cantidad,
                    detalle_precio,
                    detalle_subtotal
                )
                VALUES (%s, %s, %s, %s, %s)
            """

            valores = (
                venta_id,
                producto["prod_id"],
                producto["cantidad"],
                producto["precio"],
                producto["subtotal"]
            )

            cursor.execute(consulta_detalle, valores)

            consulta_stock = """
                UPDATE TBL_PRODUCTO
                SET prod_stock = prod_stock - %s
                WHERE prod_id = %s
            """

            cursor.execute(
                consulta_stock,
                (producto["cantidad"], producto["prod_id"])
            )

        conexion.commit()

        print("Venta registrada correctamente.")
        return venta_id

    except Exception as error:
        conexion.rollback()
        print("Error al registrar la venta:", error)
        return None

    finally:
        if cursor:
            cursor.close()

        conexion.close()
