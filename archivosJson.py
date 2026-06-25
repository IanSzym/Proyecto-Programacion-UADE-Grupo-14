# Guarda y carga los datos en archivos JSON para que no se pierdan al cerrar.

import json
import os

ARCHIVOS = {
    "clientes":    "clientes.json",
    "empleados":   "empleados.json",
    "productos":   "productos.json",
    "promociones": "promociones.json",
}

def guardar(nombre, datos):
    """Escribe una lista en su archivo JSON correspondiente."""
    try:
        with open(ARCHIVOS[nombre], "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=2)
    except Exception as e:
        print(f"Error al guardar {nombre}: {e}")


def cargar(nombre):
    """Lee el archivo JSON y retorna la lista. Si no existe, retorna []."""
    archivo = ARCHIVOS[nombre]
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error al cargar {nombre}: {e}")
        return []

    