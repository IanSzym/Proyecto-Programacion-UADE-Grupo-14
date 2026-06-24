import json
import os


# Armamos siempre la ruta dentro de la carpeta data
def obtener_ruta(nombre_archivo):
    carpeta_actual = os.path.dirname(__file__)
    carpeta_datos = os.path.join(carpeta_actual, "data")

    if not os.path.exists(carpeta_datos):
        os.makedirs(carpeta_datos)

    return os.path.join(carpeta_datos, nombre_archivo)


def cargar_datos(nombre_archivo, datos_iniciales):
    ruta = obtener_ruta(nombre_archivo)

    # Si el archivo no existe todavia lo creamos con datos iniciales
    if not os.path.exists(ruta):
        guardar_datos(nombre_archivo, datos_iniciales)
        return datos_iniciales

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        # Si el json esta roto lo reiniciamos para que no se caiga todo el programa
        print(f"El archivo {nombre_archivo} tenia un error y fue reiniciado.")
        guardar_datos(nombre_archivo, datos_iniciales)
        return datos_iniciales


def guardar_datos(nombre_archivo, datos):
    ruta = obtener_ruta(nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as archivo:
        # Guardamos con indent para que el archivo quede facil de leer
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
