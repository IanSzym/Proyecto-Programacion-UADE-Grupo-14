
from persistencia import cargar_datos
from colores import aviso, correcto, error, titulo


# Estos usuarios se usan si el archivo usuarios json todavia no existe
usuarios_iniciales = {
    "admin": "admin123",
    "ignacio": "pita123",
    "ian": "ian123",
    "matias": "rosental123",
    "lucas": "garcia123"
}

# Cargamos las credenciales desde json para que no queden solo en memoria
CREDENCIALES = cargar_datos("usuarios.json", usuarios_iniciales)


def login(usuario, password):
    # Primero revisamos que exista el usuario y despues que la clave coincida
    if usuario in CREDENCIALES:
        if CREDENCIALES[usuario] == password:
            return True
    return False


def iniciar_sesion():
    print("=" * 40)
    print(titulo("INICIO DE SESION"))
    print("=" * 40)
    print(aviso("(Ingrese -1 como usuario para salir)"))
    print()
    
    usuario = input("Usuario: ")
    
    while usuario != "-1":
        password = input("Contraseña: ")
        
        if login(usuario, password):
            print(correcto(f"\nBienvenido {usuario}"))
            return True
        else:
            print(error("Usuario o contraseña incorrectos."))
            print()
            print(aviso("(Ingrese -1 como usuario para salir)"))
            usuario = input("Usuario: ")
    
    print(aviso("\nSaliendo del sistema..."))
    return False
