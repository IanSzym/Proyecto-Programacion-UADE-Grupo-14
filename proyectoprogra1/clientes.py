from valids import validar_dni, validar_telefono, validar_email, formatear_nombre
from persistencia import cargar_datos, guardar_datos
from colores import aviso, correcto, error, titulo

# Cargamos la lista desde json y si no hay datos arranca vacia
clientes = cargar_datos("clientes.json", [])


def guardar_clientes():
    # Guardamos cada vez que cambia la lista para no perder los datos
    guardar_datos("clientes.json", clientes)


def crear_cliente():
    print(titulo("\n--- ALTA DE CLIENTE ---"))
    
    cliente = {}
    cliente["id"] = len(clientes) + 1
    
    nombre = input("Nombre: ")
    cliente["nombre"] = formatear_nombre(nombre)
    
    apellido = input("Apellido: ")
    cliente["apellido"] = formatear_nombre(apellido)
    
    dni = input("DNI (8 digitos): ")
    # Validamos con while para que no avance hasta que este bien escrito
    while not validar_dni(dni):
        print(error("DNI invalido. Debe tener 8 digitos."))
        dni = input("DNI (8 digitos): ")
    cliente["dni"] = dni
    
    email = input("Email: ")
    while not validar_email(email):
        print(error("Email invalido."))
        email = input("Email: ")
    cliente["email"] = email.lower()
    
    telefono = input("Telefono (ej: 11 1234 5678): ")
    while not validar_telefono(telefono):
        print(error("Telefono invalido."))
        telefono = input("Telefono (ej: 11 1234 5678): ")
    cliente["telefono"] = telefono
    
    cliente["activo"] = True
    
    clientes.append(cliente)
    guardar_clientes()
    print(correcto(f"\n Cliente {cliente['nombre']} {cliente['apellido']} registrado. ID: {cliente['id']}"))


def buscar_cliente_id(id_cliente):
    # Recorremos la lista y devolvemos el cliente que tenga ese id
    for cliente in clientes:
        if cliente["id"] == id_cliente:
            return cliente
    return False


def listar_clientes():
    # Filtramos solo los clientes que siguen activos
    activos = list(filter(lambda c: c["activo"], clientes))
    
    if len(activos) == 0:
        print(aviso("\nNo hay clientes activos."))
        return
    
    print(titulo("\n--- CLIENTES ACTIVOS ---"))
    for cliente in activos:
        print(f"ID: {cliente['id']} | {cliente['nombre']} {cliente['apellido']} | DNI: {cliente['dni']} | Tel: {cliente['telefono']}")


def modificar_cliente():
    if len(clientes) == 0:
        print(aviso("\nNo hay clientes registrados."))
        return
    
    try:
        id_cliente = int(input("\nID del cliente a modificar: "))
    except ValueError:
        print(error("ID invalido. Debe ingresar un numero."))
        return

    cliente = buscar_cliente_id(id_cliente)
    
    if not cliente:
        print(error("Cliente no encontrado."))
        return
    
    # Si esta inactivo preguntamos si lo quiere reactivar
    if not cliente["activo"]:
        print(aviso(f"\nEl cliente {cliente['nombre']} {cliente['apellido']} esta INACTIVO."))
        respuesta = input("Desea reactivarlo para modificarlo? (s/n): ").lower()
        if respuesta == "s":
            cliente["activo"] = True
            print(correcto("Cliente reactivado."))
        else:
            print(aviso("No se puede modificar un cliente inactivo."))
            return
        
    while True:
        print(titulo(f"\n--- MODIFICANDO: {cliente['nombre']} {cliente['apellido']} ---"))
        print("1. Modificar nombre")
        print("2. Modificar apellido")
        print("3. Modificar email")
        print("4. Modificar teléfono")
        print("0. Guardar y salir")
        
        opcion = input("\nOpción: ")
        
        if opcion == "1":
            nuevo = input(f"Nuevo nombre [{cliente['nombre']}]: ")
            if nuevo != "":
                cliente["nombre"] = formatear_nombre(nuevo)
                print(correcto("Nombre actualizado."))
                
        elif opcion == "2":
            nuevo = input(f"Nuevo apellido [{cliente['apellido']}]: ")
            if nuevo != "":
                cliente["apellido"] = formatear_nombre(nuevo)
                print(correcto("Apellido actualizado."))
                
        elif opcion == "3":
            nuevo = input(f"Nuevo email [{cliente['email']}]: ")
            if nuevo != "":
                while not validar_email(nuevo):
                    print(error("Email invalido."))
                    nuevo = input(f"Nuevo email [{cliente['email']}]: ")
                cliente["email"] = nuevo.lower()
                print(correcto("Email actualizado."))
                
        elif opcion == "4":
            nuevo = input(f"Nuevo telefono [{cliente['telefono']}]: ")
            if nuevo != "":
                while not validar_telefono(nuevo):
                    print(error("Telefono invalido."))
                    nuevo = input(f"Nuevo telefono [{cliente['telefono']}]: ")
                cliente["telefono"] = nuevo
                print(correcto("Telefono actualizado."))
                
        elif opcion == "0":
            guardar_clientes()
            print(correcto("Cambios guardados."))
            return
            
        else:
            print(error("Opcion invalida."))


def baja_cliente():
    # No borramos el registro solo lo marcamos como inactivo
    if len(clientes) == 0:
        print(aviso("\nNo hay clientes registrados."))
        return
    
    try:
        id_cliente = int(input("\nID del cliente a dar de baja: "))
    except ValueError:
        print(error("ID invalido. Debe ingresar un numero."))
        return

    cliente = buscar_cliente_id(id_cliente)
    
    if not cliente:
        print(error("Cliente no encontrado."))
    else:
        cliente["activo"] = False
        guardar_clientes()
        print(correcto(f"Cliente {cliente['nombre']} {cliente['apellido']} dado de baja."))



def buscar_clientes():
    if len(clientes) == 0:
        print(aviso("\nNo hay clientes registrados."))
        return
    
    termino = input("\nIngrese nombre, apellido o DNI a buscar: ").lower()
    
    resultados = []
    for c in clientes:
        if termino in c["nombre"].lower():
            resultados.append(c)
        elif termino in c["apellido"].lower():
            resultados.append(c)
        elif termino in c["dni"]:
            resultados.append(c)
    
    if len(resultados) == 0:
        print(aviso("No se encontraron clientes."))
    else:
        print(titulo(f"\n--- RESULTADOS ({len(resultados)}) ---"))
        for c in resultados:
            estado = "Activo" if c["activo"] else "Inactivo"
            print(f"ID: {c['id']} | {c['nombre']} {c['apellido']} | DNI: {c['dni']} | {estado}")
