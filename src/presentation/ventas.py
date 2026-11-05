from src.business.venta_service import procesar_venta


def registrar_venta_pantalla():

    print("\n======================================")
    print("          MI CUENTIKA")
    print("          REGISTRAR VENTA")
    print("======================================")

    detalles = []

    while True:
        try:
            prod_id = int(input("\nCódigo del producto: "))
            cantidad = float(input("Cantidad: "))

            if prod_id <= 0 or cantidad <= 0:
                print("El código y la cantidad deben ser mayores que cero.")
                continue

            detalles.append({
                "prod_id": prod_id,
                "cantidad": cantidad
            })

            continuar = input("\n¿Agregar otro producto? (s/n): ").lower()

            if continuar != "s":
                break

        except ValueError:
            print("Error: ingrese valores numéricos válidos.")

    venta_id = procesar_venta(detalles)

    if venta_id:
        print("\n======================================")
        print("VENTA COMPLETADA")
        print("Código de venta:", venta_id)
        print("======================================")
    else:
        print("\nNo se pudo completar la venta.")


if __name__ == "__main__":
    registrar_venta_pantalla()