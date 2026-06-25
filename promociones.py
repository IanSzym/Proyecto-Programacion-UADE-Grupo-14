# promociones.py

from valids import formatear_nombre
from archivosJson import guardar, cargar

promociones = cargar("promociones")
print(f"{len(promociones)} promociones cargadas.")


def crear_promocion():
    print("\n--- ALTA DE PROMOCION ---")

    promocion = {}
    promocion["id"] = len(promociones) + 1
    nombre = input("Nombre promocion: ")
    promocion["nombre"] = formatear_nombre(nombre)
    # En crear_promocion()
    while True:
        try:
            descuento = float(input("Descuento (%): "))
            if descuento < 0 or descuento > 100:
                print("El descuento debe estar entre 0 y 100.")
            else:
                promocion["descuento"] = descuento
                promocion["activa"] = True
                break
        except ValueError:
            print("Descuento invalido.")


    promociones.append(promocion)
    print("Promocion registrada.")
    guardar("promociones", promociones)


def buscar_promocion_id(id_promocion):

    for promocion in promociones:
        if promocion["id"] == id_promocion:
            return promocion
    return False


def listar_promociones():

    activas = list(filter(lambda p: p["activa"], promociones))

    if len(activas) == 0:
        print("\nNo hay promociones activas.")
        return
    print("\n--- PROMOCIONES ACTIVAS ---")
    for promocion in activas:
        print(
            f"ID: {promocion['id']} | "
            f"{promocion['nombre']} | "
            f"{promocion['descuento']}%"
        )


def modificar_promocion():
  
    try:
        id_promocion = int(input("ID promocion: "))
    except ValueError:
        print("ID invalido.")
        return
    promocion = buscar_promocion_id(id_promocion)
    if not promocion:
        print("Promocion no encontrada.")
        return
    nuevo_nombre = input("Nuevo nombre: ")
    if nuevo_nombre != "":
        promocion["nombre"] = formatear_nombre(nuevo_nombre)
    while True:
        try:
            nuevo_descuento = float(input("Nuevo descuento: "))
            if nuevo_descuento < 0 or nuevo_descuento > 100:
                print("El descuento debe estar entre 0 y 100.")
            else:
                promocion["descuento"] = nuevo_descuento
                print("Descuento actualizado.")
                break
        except ValueError:
            print("Descuento invalido.")
    print("Promocion actualizada.")
    guardar("promociones", promociones)


def baja_promocion():

    try:
        id_promocion = int(input("ID promocion: "))
    except ValueError:
        print("ID invalido.")
        return
    promocion = buscar_promocion_id(id_promocion)
    if not promocion:
        print("Promocion no encontrada.")
        return
    promocion["activa"] = False
    print("Promocion dada de baja.")
    guardar("promociones", promociones)


def buscar_promociones():

    termino = input("Buscar promocion: ").lower()
    resultados = []
    for promocion in promociones:
        if termino in promocion["nombre"].lower():
            resultados.append(promocion)
    if len(resultados) == 0:
        print("No se encontraron promociones.")
    else:
        for promocion in resultados:
            estado = (
                "Activa"
                if promocion["activa"]
                else "Inactiva"
            )
            print(
                f"ID: {promocion['id']} | "
                f"{promocion['nombre']} | "
                f"{promocion['descuento']}% | "
                f"{estado}"
            )