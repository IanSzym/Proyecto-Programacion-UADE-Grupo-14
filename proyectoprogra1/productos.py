from valids import formatear_nombre
from persistencia import cargar_datos, guardar_datos
from colores import aviso, correcto, error, titulo

# Cargamos la lista desde json y si no hay datos arranca vacia
productos = cargar_datos("productos.json", [])


def guardar_productos():
    # Guardamos cada vez que cambia la lista para no perder los datos
    guardar_datos("productos.json", productos)


def crear_producto():
    print(titulo("\n--- ALTA DE PRODUCTO ---"))

    producto = {}

    producto["id"] = len(productos) + 1

    nombre = input("Nombre del producto: ")
    producto["nombre"] = formatear_nombre(nombre)

    # Usamos try porque el precio tiene que ser un numero
    try:
        precio = float(input("Precio: "))
    except ValueError:
        print(error("Precio invalido."))
        return

    producto["precio"] = precio

    # Usamos try porque el stock tiene que ser un numero entero
    try:
        stock = int(input("Stock: "))
    except ValueError:
        print(error("Stock invalido."))
        return

    producto["stock"] = stock
    producto["activo"] = True

    productos.append(producto)
    guardar_productos()

    print(correcto(f"\nProducto {producto['nombre']} registrado."))
    

def buscar_producto_id(id_producto):
    # Recorremos la lista y devolvemos el producto que tenga ese id
    for producto in productos:
        if producto["id"] == id_producto:
            return producto
    return False


def listar_productos():

    # Filtramos solo los productos que siguen activos
    activos = list(filter(lambda p: p["activo"], productos))

    if len(activos) == 0:
        print(aviso("\nNo hay productos activos."))
        return

    print(titulo("\n--- PRODUCTOS ACTIVOS ---"))

    for producto in activos:
        print(
            f"ID: {producto['id']} | "
            f"{producto['nombre']} | "
            f"${producto['precio']} | "
            f"Stock: {producto['stock']}"
        )


def modificar_producto():

    if len(productos) == 0:
        print(aviso("\nNo hay productos registrados."))
        return

    try:
        id_producto = int(input("ID del producto: "))
    except ValueError:
        print(error("ID invalido."))
        return

    producto = buscar_producto_id(id_producto)

    if not producto:
        print(error("Producto no encontrado."))
        return

    while True:

        print("\n1. Nombre")
        print("2. Precio")
        print("3. Stock")
        print("0. Guardar")

        opcion = input("Opcion: ")

        if opcion == "1":

            nuevo = input("Nuevo nombre: ")

            if nuevo != "":
                producto["nombre"] = formatear_nombre(nuevo)

        elif opcion == "2":

            try:
                producto["precio"] = float(input("Nuevo precio: "))
            except ValueError:
                print(error("Precio invalido."))

        elif opcion == "3":

            try:
                producto["stock"] = int(input("Nuevo stock: "))
            except ValueError:
                print(error("Stock invalido."))

        elif opcion == "0":
            guardar_productos()
            print(correcto("Cambios guardados."))
            return

        else:
            print(error("Opcion invalida."))


def baja_producto():

    if len(productos) == 0:
        print(aviso("\nNo hay productos."))
        return

    try:
        id_producto = int(input("ID del producto: "))
    except ValueError:
        print(error("ID invalido."))
        return

    producto = buscar_producto_id(id_producto)

    if not producto:
        print(error("Producto no encontrado."))
        return

    # No borramos el registro solo lo marcamos como inactivo
    producto["activo"] = False
    guardar_productos()

    print(correcto(f"Producto {producto['nombre']} dado de baja."))


def buscar_productos():

    if len(productos) == 0:
        print(aviso("\nNo hay productos."))
        return

    termino = input("Nombre del producto: ").lower()

    resultados = []

    for producto in productos:
        if termino in producto["nombre"].lower():
            resultados.append(producto)

    if len(resultados) == 0:
        print(aviso("No se encontraron productos."))
    else:
        for producto in resultados:
            estado = "Activo" if producto["activo"] else "Inactivo"

            print(
                f"ID: {producto['id']} | "
                f"{producto['nombre']} | "
                f"${producto['precio']} | "
                f"{estado}"
            )
