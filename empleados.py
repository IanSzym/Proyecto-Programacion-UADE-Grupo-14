# empleados.py

from valids import validar_dni, validar_telefono, validar_email, formatear_nombre

# Lista de diccionarios para guardar empleados
empleados = []


def crear_empleado():
    # Alta de empleado

    print("\n--- ALTA DE EMPLEADO ---")
    
    empleado = {}
    empleado["id"] = len(empleados) + 1
    
    nombre = input("Nombre: ")
    empleado["nombre"] = formatear_nombre(nombre)
    
    apellido = input("Apellido: ")
    empleado["apellido"] = formatear_nombre(apellido)
    
    dni = input("DNI (8 digitos): ")
    while not validar_dni(dni):
        print("DNI invalido. Debe tener 8 digitos.")
        dni = input("DNI (8 digitos): ")
    empleado["dni"] = dni
    
    email = input("Email: ")
    while not validar_email(email):
        print("Email invalido.")
        email = input("Email: ")
    empleado["email"] = email.lower()
    
    telefono = input("Telefono (ej: 11 1234 5678): ")
    while not validar_telefono(telefono):
        print("Telefono invalido.")
        telefono = input("Telefono (ej: 11 1234 5678): ")
    empleado["telefono"] = telefono
    
    cargo = input("Cargo: ")
    empleado["cargo"] = formatear_nombre(cargo)
    
    empleado["activo"] = True
    
    empleados.append(empleado)
    print(f"\n Empleado {empleado['nombre']} {empleado['apellido']} registrado. ID: {empleado['id']}")


def buscar_empleado_id(id_empleado):
    # Busca un empleado por su ID usando un bucle for
    for empleado in empleados:
        if empleado["id"] == id_empleado:
            return empleado
    return False


def listar_empleados():
    # Lista todos los empleados activos
    # Filter con lambda para obtener solo activos
    activos = list(filter(lambda e: e["activo"], empleados))
    
    if len(activos) == 0:
        print("\nNo hay empleados activos.")
        return
    
    print("\n--- EMPLEADOS ACTIVOS ---")
    for empleado in activos:
        print(f"ID: {empleado['id']} | {empleado['nombre']} {empleado['apellido']} | Cargo: {empleado['cargo']} | Tel: {empleado['telefono']}")


def modificar_empleado():
    if len(empleados) == 0:
        print("\nNo hay empleados registrados.")
        return
    
    try:
        id_empleado = int(input("\nID del empleado a modificar: "))
    except ValueError:
        print("ID invalido. Debe ingresar un numero.")
        return

    empleado = buscar_empleado_id(id_empleado)
    
    if not empleado:
        print("Empleado no encontrado.")
        return
    
    # Verificar si está inactivo y preguntar si quiere reactivar
    if not empleado["activo"]:
        print(f"\nEl empleado {empleado['nombre']} {empleado['apellido']} esta INACTIVO.")
        respuesta = input("Desea reactivarlo para modificarlo? (s/n): ").lower()
        if respuesta == "s":
            empleado["activo"] = True
            print("Empleado reactivado.")
        else:
            print("No se puede modificar un empleado inactivo.")
            return
        
    while True:
        print(f"\n--- MODIFICANDO: {empleado['nombre']} {empleado['apellido']} ---")
        print("1. Modificar nombre")
        print("2. Modificar apellido")
        print("3. Modificar email")
        print("4. Modificar telefono")
        print("5. Modificar cargo")
        print("0. Guardar y salir")
        
        opcion = input("\nOpcion: ")
        
        if opcion == "1":
            nuevo = input(f"Nuevo nombre [{empleado['nombre']}]: ")
            if nuevo != "":
                empleado["nombre"] = formatear_nombre(nuevo)
                print("Nombre actualizado.")
                
        elif opcion == "2":
            nuevo = input(f"Nuevo apellido [{empleado['apellido']}]: ")
            if nuevo != "":
                empleado["apellido"] = formatear_nombre(nuevo)
                print("Apellido actualizado.")
                
        elif opcion == "3":
            nuevo = input(f"Nuevo email [{empleado['email']}]: ")
            if nuevo != "":
                while not validar_email(nuevo):
                    print("Email invalido.")
                    nuevo = input(f"Nuevo email [{empleado['email']}]: ")
                empleado["email"] = nuevo.lower()
                print("Email actualizado.")
                
        elif opcion == "4":
            nuevo = input(f"Nuevo telefono [{empleado['telefono']}]: ")
            if nuevo != "":
                while not validar_telefono(nuevo):
                    print("Telefono invalido.")
                    nuevo = input(f"Nuevo telefono [{empleado['telefono']}]: ")
                empleado["telefono"] = nuevo
                print("Telefono actualizado.")
                
        elif opcion == "5":
            nuevo = input(f"Nuevo cargo [{empleado['cargo']}]: ")
            if nuevo != "":
                empleado["cargo"] = formatear_nombre(nuevo)
                print("Cargo actualizado.")
                
        elif opcion == "0":
            print("Cambios guardados.")
            return
            
        else:
            print("Opcion invalida.")


def baja_empleado():
    # Baja de empleado (no se elimina, se marca como inactivo)
    if len(empleados) == 0:
        print("\nNo hay empleados registrados.")
        return
    
    try:
        id_empleado = int(input("\nID del empleado a dar de baja: "))
    except ValueError:
        print("ID invalido. Debe ingresar un numero.")
        return

    empleado = buscar_empleado_id(id_empleado)
    
    if not empleado:
        print("Empleado no encontrado.")
    else:
        empleado["activo"] = False
        print(f"Empleado {empleado['nombre']} {empleado['apellido']} dado de baja.")


def buscar_empleados():
    # Busca empleados por nombre, apellido o DNI 
    if len(empleados) == 0:
        print("\nNo hay empleados registrados.")
        return
    
    termino = input("\nIngrese nombre, apellido o DNI a buscar: ").lower()
    
    resultados = []
    for e in empleados:
        if termino in e["nombre"].lower():
            resultados.append(e)
        elif termino in e["apellido"].lower():
            resultados.append(e)
        elif termino in e["dni"]:
            resultados.append(e)
    
    if len(resultados) == 0:
        print("No se encontraron empleados.")
    else:
        print(f"\n--- RESULTADOS ({len(resultados)}) ---")
        for e in resultados:
            estado = "Activo" if e["activo"] else "Inactivo"
            print(f"ID: {e['id']} | {e['nombre']} {e['apellido']} | Cargo: {e['cargo']} | DNI: {e['dni']} | {estado}")
