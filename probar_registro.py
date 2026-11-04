from src.business.producto_service import registrar_producto

nuevo_id = registrar_producto(
    "Jugo de naranja",
    "Unidad",
    15.00,
    20.00,
    10,
    2,
    1
)

if nuevo_id:
    print("Código del nuevo producto:", nuevo_id)
    print("Prueba de registro completada.")
else:
    print("No se pudo registrar el producto.")