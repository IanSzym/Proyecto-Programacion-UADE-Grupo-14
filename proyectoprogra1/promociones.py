from valids import formatear_nombre
from persistencia import cargar_datos, guardar_datos
from colores import aviso, correcto, error, titulo

# Cargamos la lista desde json y si no hay datos arranca vacia
promociones = cargar_datos("promociones.json", [])


def guardar_promociones():
    # Guardamos cada vez que cambia la lista para no perder los datos
    guardar_datos("promociones.json", promociones)


def crear_promocion():
    print(titulo("\n--- ALTA DE PROMOCION ---"))

    promocion = {}
    promocion["id"] = len(promociones) + 1
    nombre = input("Nombre promocion: ")
    promocion["nombre"] = formatear_nombre(nombre)
    # Usamos try porque el descuento tiene que ser un numero
    while True:
        try:
            descuento = float(input("Descuento (%): "))
            if descuento < 0 or descuento > 100:
                print(error("El descuento debe estar entre 0 y 100."))
            else:
                promocion["descuento"] = descuento
                promocion["activa"] = True
                break 
        except ValueError:
            print(error("Descuento invalido."))

    promociones.append(promocion)
    guardar_promociones()
    print(correcto("Promocion registrada."))


def buscar_promocion_id(id_promocion):

    # Recorremos la lista y devolvemos la promocion que tenga ese id
    for promocion in promociones:
        if promocion["id"] == id_promocion:
            return promocion
    return False


def listar_promociones():

    # Filtramos solo las promociones que siguen activas
    activas = list(filter(lambda p: p["activa"], promociones))

    if len(activas) == 0:
        print(aviso("\nNo hay promociones activas."))
        return
    print(titulo("\n--- PROMOCIONES ACTIVAS ---"))
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
        print(error("ID invalido."))
        return
    promocion = buscar_promocion_id(id_promocion)
    if not promocion:
        print(error("Promocion no encontrada."))
        return
    
    # Esta variable sirve para saber si hay algo para guardar o no
    hubo_cambios = False

    nuevo_nombre = input("Nuevo nombre: ")
    if nuevo_nombre != "":
        promocion["nombre"] = formatear_nombre(nuevo_nombre)
        hubo_cambios = True

    nuevo_descuento = input("Nuevo descuento: ")
    if nuevo_descuento != "":
        try:
            nuevo = float(nuevo_descuento)
            if nuevo < 0 or nuevo > 100:
                print(error("El descuento debe estar entre 0 y 100."))
            else:
                promocion["descuento"] = nuevo
                hubo_cambios = True
        except ValueError:
            print(error("Descuento invalido."))


    if hubo_cambios:
        guardar_promociones()
        print(correcto("Promocion actualizada."))
    else:
        print(aviso("No se realizaron cambios."))


def baja_promocion():

    try:
        id_promocion = int(input("ID promocion: "))
    except ValueError:
        print(error("ID invalido."))
        return
    promocion = buscar_promocion_id(id_promocion)
    if not promocion:
        print(error("Promocion no encontrada."))
        return
    # No borramos el registro solo lo marcamos como inactivo
    promocion["activa"] = False
    guardar_promociones()
    print(correcto("Promocion dada de baja."))


def buscar_promociones():

    termino = input("Buscar promocion: ").lower()
    resultados = []
    for promocion in promociones:
        if termino in promocion["nombre"].lower():
            resultados.append(promocion)
    if len(resultados) == 0:
        print(aviso("No se encontraron promociones."))
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
