from src.data.conexion import obtener_conexion

conexion = obtener_conexion()

if conexion and conexion.is_connected():
    print("¡Conexión exitosa con MySQL!")
    print("Base de datos: bd_mi_cuentika")
    print("Servidor:", conexion.server_info)

    conexion.close()
else:
    print("No se pudo establecer la conexión.")