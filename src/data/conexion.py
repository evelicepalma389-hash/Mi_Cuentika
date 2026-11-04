import os
from pathlib import Path
import mysql.connector
from dotenv import load_dotenv

# Buscar el archivo .env en la carpeta principal
RUTA_PROYECTO = Path(__file__).resolve().parents[2]
load_dotenv(RUTA_PROYECTO / ".env")


def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", 3306)),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS") or "",
            charset=os.getenv("DB_CHARSET", "utf8mb4")
        )

        return conexion

    except mysql.connector.Error as error:
        print("Error al conectar con MySQL:", error)
        return None