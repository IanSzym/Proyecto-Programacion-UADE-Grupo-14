# clientes.py

from valids import validar_dni, validar_telefono, validar_email, formatear_nombre

# Lista de diccionarios para guardar clientes 
clientes = []


def crear_cliente():
    #Alta de cliente

    print("\n--- ALTA DE CLIENTE ---")
    cliente = {}
    cliente["id"] = len(clientes) + 1
    
    nombre = input("Nombre: ")
    cliente["nombre"] = formatear_nombre(nombre)
    
    apellido = input("Apellido: ")
    cliente["apellido"] = formatear_nombre(apellido)
    
    dni = input("DNI (8 digitos): ")
    while not validar_dni(dni):
        print("DNI invalido. Debe tener 8 digitos.")
        dni = input("DNI (8 digitos): ")
    cliente["dni"] = dni
    
    email = input("Email: ")
    while not validar_email(email):
        print("Email invalido.")
        email = input("Email: ")
    cliente["email"] = email.lower()
    
    telefono = input("Telefono (ej: 11 1234 5678): ")
    while not validar_telefono(telefono):
        print("Telefono invalido.")
        telefono = input("Telefono (ej: 11 1234 5678): ")
    cliente["telefono"] = telefono
    
    cliente["activo"] = True
    
    clientes.append(cliente)
    print(f"\n Cliente {cliente['nombre']} {cliente['apellido']} registrado. ID: {cliente['id']}")


def buscar_cliente_id(id_cliente):
    #Busca un cliente por su ID usando un bucle for 
    for cliente in clientes:
        if cliente["id"] == id_cliente:
            return cliente
    return False


def listar_clientes():
    #Lista todos los clientes activos
    # Filter con lambda para obtener solo activos
    activos = list(filter(lambda c: c["activo"], clientes))
    
    if len(activos) == 0:
        print("\nNo hay clientes activos.")
        return
    
    print("\n--- CLIENTES ACTIVOS ---")
    for cliente in activos:
        print(f"ID: {cliente['id']} | {cliente['nombre']} {cliente['apellido']} | DNI: {cliente['dni']} | Tel: {cliente['telefono']}")


def modificar_cliente():
    if len(clientes) == 0:
        print("\nNo hay clientes registrados.")
        return
    
    try:
        id_cliente = int(input("\nID del cliente a modificar: "))
    except ValueError:
        print("ID invalido. Debe ingresar un numero.")
        return

    cliente = buscar_cliente_id(id_cliente)
    
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    # Verificar si este inactivo y preguntar si quiere reactivar
    if not cliente["activo"]:
        print(f"\nEl cliente {cliente['nombre']} {cliente['apellido']} esta INACTIVO.")
        respuesta = input("Desea reactivarlo para modificarlo? (s/n): ").lower()
        if respuesta == "s":
            cliente["activo"] = True
            print("Cliente reactivado.")
        else:
            print("No se puede modificar un cliente inactivo.")
            return
        
    while True:
        print(f"\n--- MODIFICANDO: {cliente['nombre']} {cliente['apellido']} ---")
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
                print("Nombre actualizado.")
                
        elif opcion == "2":
            nuevo = input(f"Nuevo apellido [{cliente['apellido']}]: ")
            if nuevo != "":
                cliente["apellido"] = formatear_nombre(nuevo)
                print("Apellido actualizado.")
                
        elif opcion == "3":
            nuevo = input(f"Nuevo email [{cliente['email']}]: ")
            if nuevo != "":
                while not validar_email(nuevo):
                    print("Email invalido.")
                    nuevo = input(f"Nuevo email [{cliente['email']}]: ")
                cliente["email"] = nuevo.lower()
                print("Email actualizado.")
                
        elif opcion == "4":
            nuevo = input(f"Nuevo telefono [{cliente['telefono']}]: ")
            if nuevo != "":
                while not validar_telefono(nuevo):
                    print("Telefono invalido.")
                    nuevo = input(f"Nuevo telefono [{cliente['telefono']}]: ")
                cliente["telefono"] = nuevo
                print("Telefono actualizado.")
                
        elif opcion == "0":
            print("Cambios guardados.")
            return
            
        else:
            print("Opcion invalida.")


def baja_cliente():
    #Baja de cliente (no se elimina, se marca como inactivo)
    if len(clientes) == 0:
        print("\nNo hay clientes registrados.")
        return
    
    try:
        id_cliente = int(input("\nID del cliente a dar de baja: "))
    except ValueError:
        print("ID invalido. Debe ingresar un numero.")
        return

    cliente = buscar_cliente_id(id_cliente)
    
    if not cliente:
        print("Cliente no encontrado.")
    else:
        cliente["activo"] = False
        print(f"Cliente {cliente['nombre']} {cliente['apellido']} dado de baja.")



def buscar_clientes():
    if len(clientes) == 0:
        print("\nNo hay clientes registrados.")
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
        print("No se encontraron clientes.")
    else:
        print(f"\n--- RESULTADOS ({len(resultados)}) ---")
        for c in resultados:
            estado = "Activo" if c["activo"] else "Inactivo"
            print(f"ID: {c['id']} | {c['nombre']} {c['apellido']} | DNI: {c['dni']} | {estado}")
