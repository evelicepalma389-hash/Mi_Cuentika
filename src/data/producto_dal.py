from src.data.conexion import obtener_conexion


def listar_productos():
    conexion = obtener_conexion()

    if conexion is None:
        return []

    cursor = None

    try:
        cursor = conexion.cursor(dictionary=True)

        consulta = """
            SELECT
                p.prod_id,
                p.prod_nombre,
                p.prod_unidad,
                p.prod_precio_compra,
                p.prod_precio_venta,
                p.prod_stock,
                p.prod_stock_minimo,
                c.cat_nombre
            FROM TBL_PRODUCTO p
            INNER JOIN TBL_CATEGORIA c
                ON p.cat_id = c.cat_id
            ORDER BY p.prod_id ASC
        """

        cursor.execute(consulta)

        productos = cursor.fetchall()

        return productos

    except Exception as error:
        print("Error al consultar productos:", error)
        return []

    finally:
        if cursor:
            cursor.close()

        conexion.close()

def insertar_producto(nombre, unidad, precio_compra, precio_venta, stock, stock_minimo, cat_id):
    conexion = obtener_conexion()

    if conexion is None:
        return None

    cursor = None

    try:
        cursor = conexion.cursor()

        consulta = """
            INSERT INTO TBL_PRODUCTO (
                prod_nombre,
                prod_unidad,
                prod_precio_compra,
                prod_precio_venta,
                prod_stock,
                prod_stock_minimo,
                prod_activo,
                cat_id
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            nombre,
            unidad,
            precio_compra,
            precio_venta,
            stock,
            stock_minimo,
            True,
            cat_id
        )

        cursor.execute(consulta, valores)
        conexion.commit()

        return cursor.lastrowid

    except Exception as error:
        conexion.rollback()
        print("Error al registrar producto:", error)
        return None

    finally:
        if cursor:
            cursor.close()

        conexion.close()
def listar_categorias():
    conexion = obtener_conexion()

    if conexion is None:
        return []

    cursor = None

    try:
        cursor = conexion.cursor(dictionary=True)

        consulta = """
            SELECT cat_id, cat_nombre
            FROM TBL_CATEGORIA
            ORDER BY cat_id ASC
        """

        cursor.execute(consulta)

        categorias = cursor.fetchall()

        return categorias

    except Exception as error:
        print("Error al consultar categorías:", error)
        return []

    finally:
        if cursor:
            cursor.close()

        conexion.close()