# productos.py

from valids import formatear_nombre
from archivosJson import guardar, cargar

productos = cargar("productos")
print(f"{len(productos)} productos cargados.")


def crear_producto():
    print("\n--- ALTA DE PRODUCTO ---")

    producto = {}

    producto["id"] = len(productos) + 1

    nombre = input("Nombre del producto: ")
    producto["nombre"] = formatear_nombre(nombre)

    while True:
        try:
            precio = float(input("Precio: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                producto["precio"] = precio
                break
        except ValueError:
            print("Precio invalido. Ingrese un numero.")

    while True:
        try:
            stock = int(input("Stock: "))
            if stock < 0:
                print("El stock no puede ser negativo.")
            else:
                producto["stock"] = stock
                producto["activo"] = True
                break
        except ValueError:
            print("Stock invalido.")

    productos.append(producto)
    print(f"\nProducto {producto['nombre']} registrado.")
    guardar("productos", productos)
    

def buscar_producto_id(id_producto):
    for producto in productos:
        if producto["id"] == id_producto:
            return producto
    return False


def listar_productos():

    activos = list(filter(lambda p: p["activo"], productos))

    if len(activos) == 0:
        print("\nNo hay productos activos.")
        return

    print("\n--- PRODUCTOS ACTIVOS ---")

    for producto in activos:
        print(
            f"ID: {producto['id']} | "
            f"{producto['nombre']} | "
            f"${producto['precio']} | "
            f"Stock: {producto['stock']}"
        )


def modificar_producto():

    if len(productos) == 0:
        print("\nNo hay productos registrados.")
        return

    try:
        id_producto = int(input("ID del producto: "))
    except ValueError:
        print("ID invalido.")
        return

    producto = buscar_producto_id(id_producto)

    if not producto:
        print("Producto no encontrado.")
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
            while True:
                try:
                    nuevo = float(input("Nuevo precio: "))
                    if nuevo < 0:
                        print("El precio no puede ser negativo.")
                    else:
                        producto["precio"] = nuevo
                        print("Precio actualizado.")
                        break
                except ValueError:
                    print("Precio invalido.")

        elif opcion == "3":
            while True:
                try:
                    nuevo = int(input("Nuevo stock: "))
                    if nuevo < 0:
                        print("El stock no puede ser negativo.")
                    else:
                        producto["stock"] = nuevo
                        print("Stock actualizado.")
                        break
                except ValueError:
                    print("Stock invalido.")

        elif opcion == "0":
            print("Cambios guardados.")
            guardar("productos", productos)
            return

        else:
            print("Opcion invalida.")


def baja_producto():

    if len(productos) == 0:
        print("\nNo hay productos.")
        return

    try:
        id_producto = int(input("ID del producto: "))
    except ValueError:
        print("ID invalido.")
        return

    producto = buscar_producto_id(id_producto)

    if not producto:
        print("Producto no encontrado.")
        return

    producto["activo"] = False
    print(f"Producto {producto['nombre']} dado de baja.")
    guardar("productos", productos)


def buscar_productos():

    if len(productos) == 0:
        print("\nNo hay productos.")
        return

    termino = input("Nombre del producto: ").lower()

    resultados = []

    for producto in productos:
        if termino in producto["nombre"].lower():
            resultados.append(producto)

    if len(resultados) == 0:
        print("No se encontraron productos.")
    else:
        for producto in resultados:
            estado = "Activo" if producto["activo"] else "Inactivo"

            print(
                f"ID: {producto['id']} | "
                f"{producto['nombre']} | "
                f"${producto['precio']} | "
                f"Stock: {producto['stock']} | "
                f"{estado}"
            )