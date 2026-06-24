import json
import os


def obtener_ruta(nombre_archivo):
    carpeta_actual = os.path.dirname(__file__)
    carpeta_datos = os.path.join(carpeta_actual, "data")

    if not os.path.exists(carpeta_datos):
        os.makedirs(carpeta_datos)

    return os.path.join(carpeta_datos, nombre_archivo)


def cargar_datos(nombre_archivo, datos_iniciales):
    ruta = obtener_ruta(nombre_archivo)

    if not os.path.exists(ruta):
        guardar_datos(nombre_archivo, datos_iniciales)
        return datos_iniciales

    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_datos(nombre_archivo, datos):
    ruta = obtener_ruta(nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
