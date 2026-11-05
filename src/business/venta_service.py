from src.data.venta_dal import registrar_venta


def procesar_venta(detalles):
    try:
        if not detalles:
            print("La venta debe contener al menos un producto.")
            return None

        for detalle in detalles:

            if "prod_id" not in detalle or "cantidad" not in detalle:
                print("Faltan datos del producto.")
                return None

            prod_id = int(detalle["prod_id"])
            cantidad = float(detalle["cantidad"])

            if prod_id <= 0:
                print("El código del producto no es válido.")
                return None

            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                return None

        venta_id = registrar_venta(detalles)

        if venta_id:
            print("Proceso de venta finalizado correctamente.")
            return venta_id

        return None

    except (ValueError, TypeError):
        print("Error: verifica los códigos y las cantidades.")

        return None

    except Exception as error:
        print("Error en la lógica de negocio:", error)
        return None