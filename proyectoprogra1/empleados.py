from valids import validar_dni, validar_telefono, validar_email, formatear_nombre
from persistencia import cargar_datos, guardar_datos
from colores import aviso, correcto, error, titulo

# Cargamos la lista desde json y si no hay datos arranca vacia
empleados = cargar_datos("empleados.json", [])


def guardar_empleados():
    # Guardamos cada vez que cambia la lista para no perder los datos
    guardar_datos("empleados.json", empleados)


def crear_empleado():
    print(titulo("\n--- ALTA DE EMPLEADO ---"))
    
    empleado = {}
    empleado["id"] = len(empleados) + 1
    
    nombre = input("Nombre: ")
    empleado["nombre"] = formatear_nombre(nombre)
    
    apellido = input("Apellido: ")
    empleado["apellido"] = formatear_nombre(apellido)
    
    dni = input("DNI (8 digitos): ")
    # Validamos con while para que no avance hasta que este bien escrito
    while not validar_dni(dni):
        print(error("DNI invalido. Debe tener 8 digitos."))
        dni = input("DNI (8 digitos): ")
    #Conjuntos, verifica que el DNI no este ya registrado
    dnis_registrados = {e["dni"] for e in empleados}  # ← SET
    while dni in dnis_registrados:
        print(error("Ya existe un empleado con ese DNI."))
        dni = input("DNI (8 digitos): ")
        while not validar_dni(dni):
            print(error("DNI invalido. Debe tener 8 digitos."))
            dni = input("DNI (8 digitos): ")
    empleado["dni"] = dni


    email = input("Email: ")
    while not validar_email(email):
        print(error("Email invalido."))
        email = input("Email: ")
    empleado["email"] = email.lower()
    
    telefono = input("Telefono (ej: 11 1234 5678): ")
    while not validar_telefono(telefono):
        print(error("Telefono invalido."))
        telefono = input("Telefono (ej: 11 1234 5678): ")
    empleado["telefono"] = telefono
    
    cargo = input("Cargo: ")
    empleado["cargo"] = formatear_nombre(cargo)
    
    empleado["activo"] = True
    
    empleados.append(empleado)
    guardar_empleados()
    print(correcto(f"\n Empleado {empleado['nombre']} {empleado['apellido']} registrado. ID: {empleado['id']}"))


def buscar_empleado_id(lista, id_empleado, inicio, fin):
    # Búsqueda binaria recursiva por ID
    if inicio > fin:
        return False
    medio = (inicio + fin) // 2
    if lista[medio]["id"] == id_empleado:
        return lista[medio]
    elif id_empleado < lista[medio]["id"]:
        return buscar_empleado_id(lista, id_empleado, inicio, medio - 1)
    else:
        return buscar_empleado_id(lista, id_empleado, medio + 1, fin)


def listar_empleados():
    # Filtramos solo los empleados que siguen activos
    activos = list(filter(lambda e: e["activo"], empleados))
    
    if len(activos) == 0:
        print(aviso("\nNo hay empleados activos."))
        return
    
    print(titulo("\n--- EMPLEADOS ACTIVOS ---"))
    for empleado in activos:
        print(f"ID: {empleado['id']} | {empleado['nombre']} {empleado['apellido']} | Cargo: {empleado['cargo']} | Tel: {empleado['telefono']}")
    print(f"Total activos: {len(activos)}")

def modificar_empleado():
    if len(empleados) == 0:
        print(aviso("\nNo hay empleados registrados."))
        return
    
    try:
        id_empleado = int(input("\nID del empleado a modificar: "))
    except ValueError:
        print(error("ID invalido. Debe ingresar un numero."))
        return

    empleado = buscar_empleado_id(empleados, id_empleado, 0, len(empleados) - 1)
    
    if not empleado:
        print(error("Empleado no encontrado."))
        return
    
    # Si esta inactivo preguntamos si lo quiere reactivar
    if not empleado["activo"]:
        print(aviso(f"\nEl empleado {empleado['nombre']} {empleado['apellido']} esta INACTIVO."))
        respuesta = input("Desea reactivarlo para modificarlo? (s/n): ").lower()
        if respuesta == "s":
            empleado["activo"] = True
            print(correcto("Empleado reactivado."))
        else:
            print(aviso("No se puede modificar un empleado inactivo."))
            return
        
    while True:
        print(titulo(f"\n--- MODIFICANDO: {empleado['nombre']} {empleado['apellido']} ---"))
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
                print(correcto("Nombre actualizado."))
                
        elif opcion == "2":
            nuevo = input(f"Nuevo apellido [{empleado['apellido']}]: ")
            if nuevo != "":
                empleado["apellido"] = formatear_nombre(nuevo)
                print(correcto("Apellido actualizado."))
                
        elif opcion == "3":
            nuevo = input(f"Nuevo email [{empleado['email']}]: ")
            if nuevo != "":
                while not validar_email(nuevo):
                    print(error("Email invalido."))
                    nuevo = input(f"Nuevo email [{empleado['email']}]: ")
                empleado["email"] = nuevo.lower()
                print(correcto("Email actualizado."))
                
        elif opcion == "4":
            nuevo = input(f"Nuevo telefono [{empleado['telefono']}]: ")
            if nuevo != "":
                while not validar_telefono(nuevo):
                    print(error("Telefono invalido."))
                    nuevo = input(f"Nuevo telefono [{empleado['telefono']}]: ")
                empleado["telefono"] = nuevo
                print(correcto("Telefono actualizado."))
                
        elif opcion == "5":
            nuevo = input(f"Nuevo cargo [{empleado['cargo']}]: ")
            if nuevo != "":
                empleado["cargo"] = formatear_nombre(nuevo)
                print(correcto("Cargo actualizado."))
                
        elif opcion == "0":
            guardar_empleados()
            print(correcto("Cambios guardados."))
            return
            
        else:
            print(error("Opcion invalida."))


def baja_empleado():
    # No borramos el registro solo lo marcamos como inactivo
    if len(empleados) == 0:
        print(aviso("\nNo hay empleados registrados."))
        return
    
    try:
        id_empleado = int(input("\nID del empleado a dar de baja: "))
    except ValueError:
        print(error("ID invalido. Debe ingresar un numero."))
        return

    empleado = buscar_empleado_id(empleados, id_empleado, 0, len(empleados) - 1)
    
    if not empleado:
        print(error("Empleado no encontrado."))
    else:
        empleado["activo"] = False
        guardar_empleados()
        print(correcto(f"Empleado {empleado['nombre']} {empleado['apellido']} dado de baja."))


def buscar_empleados():
    # Busca empleados por nombre, apellido o DNI 
    if len(empleados) == 0:
        print(aviso("\nNo hay empleados registrados."))
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
        print(aviso("No se encontraron empleados."))
    else:
        print(titulo(f"\n--- RESULTADOS ({len(resultados)}) ---"))
        for e in resultados:
            estado = "Activo" if e["activo"] else "Inactivo"
            print(f"ID: {e['id']} | {e['nombre']} {e['apellido']} | Cargo: {e['cargo']} | DNI: {e['dni']} | {estado}")
