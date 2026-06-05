# main.py

from login import iniciar_sesion
from clientes import crear_cliente, listar_clientes, modificar_cliente, baja_cliente, buscar_clientes
from empleados import crear_empleado, listar_empleados, modificar_empleado, baja_empleado, buscar_empleados
from calculadora import calculadora_corporal
from productos import crear_producto, listar_productos, modificar_producto, baja_producto, buscar_productos


def menu_clientes():
    opcion = ""
    while opcion != "0":
        print("\n" + "=" * 40)
        print("GESTION DE CLIENTES")
        print("=" * 40)
        print("1. Alta de cliente")
        print("2. Listar clientes activos")
        print("3. Buscar cliente")
        print("4. Modificar cliente")
        print("5. Baja de cliente")
        print("0. Volver al menu principal")
        
        opcion = input("\nOpcion: ")
        
        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_clientes()
        elif opcion == "4":
            modificar_cliente()
        elif opcion == "5":
            baja_cliente()
        elif opcion == "0":
            return  
        else:
            print("Opcion invalida.")


def menu_empleados():
    opcion = ""
    while opcion != "0":
        print("\n" + "=" * 40)
        print("GESTION DE EMPLEADOS")
        print("=" * 40)
        print("1. Alta de empleado")
        print("2. Listar empleados activos")
        print("3. Buscar empleado")
        print("4. Modificar empleado")
        print("5. Baja de empleado")
        print("0. Volver al menu principal")
        
        opcion = input("\nOpcion: ")
        
        if opcion == "1":
            crear_empleado()
        elif opcion == "2":
            listar_empleados()
        elif opcion == "3":
            buscar_empleados()
        elif opcion == "4":
            modificar_empleado()
        elif opcion == "5":
            baja_empleado()
        elif opcion == "0":
            return 
        else:
            print("Opcion invalida.")


def menu_productos():
    opcion = ""
    while opcion != "0":
        print("\n" + "=" * 40)
        print("GESTION DE PRODUCTOS")
        print("=" * 40)
        print("1. Alta de producto")
        print("2. Listar productos activos")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Baja de producto")
        print("0. Volver al menu principal")
        
        opcion = input("\nOpcion: ")
        
        if opcion == "1":
            crear_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            buscar_productos()
        elif opcion == "4":
            modificar_producto()
        elif opcion == "5":
            baja_producto()
        elif opcion == "0":
            return
        else:
            print("Opcion invalida.")


def menu_principal():
    opcion = ""
    while opcion != "0":
        print("\n" + "=" * 40)
        print("SISTEMA DE GESTION - GRUPO 14")
        print("=" * 40)
        print("1. Gestion de Clientes")
        print("2. Gestion de Empleados")
        print("3. Gestion de Productos")
        print("4. Calculadora corporal")
        print("0. Salir")
        
        opcion = input("\nOpcion: ")
        
        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_empleados()
        elif opcion == "3":
            menu_productos()
        elif opcion == "4":
            calculadora_corporal()
        elif opcion == "0":
            print("\nSaliendo del sistema...")
            return  
        else:
            print("Opcion invalida.")


# Programa principal
print("=" * 50)
print("SISTEMA DE GESTION - GRUPO 14")
print("=" * 50)

if iniciar_sesion():
    menu_principal()
    