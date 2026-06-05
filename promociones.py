# promociones.py

from valids import formatear_nombre

promociones = []


def crear_promocion():
    print("\n--- ALTA DE PROMOCION ---")

    promocion = {}
    promocion["id"] = len(promociones) + 1
    nombre = input("Nombre promocion: ")
    promocion["nombre"] = formatear_nombre(nombre)
    try:
        descuento = float(input("Descuento (%): "))
    except ValueError:
        print("Descuento invalido.")
        return

    promocion["descuento"] = descuento
    promocion["activa"] = True

    promociones.append(promocion)
    print("Promocion registrada.")


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
    try:
        promocion["descuento"] = float(
            input("Nuevo descuento: ")
        )
    except ValueError:
        print("Descuento invalido.")
    print("Promocion actualizada.")


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