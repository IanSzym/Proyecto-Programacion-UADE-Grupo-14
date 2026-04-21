
CREDENCIALES = {
    "admin": "admin123",
    "ignacio": "pita123",
    "ian": "ian123",
    "matias": "rosental123",
    "lucas": "garcia123"
}

def login(usuario, password):
    #Valida usuario y contraseña.
    #Retorna True si son correctos, False si no.
    if usuario in CREDENCIALES:
        if CREDENCIALES[usuario] == password:
            return True
    return False


def iniciar_sesion():
    print("=" * 40)
    print("INICIO DE SESION")
    print("=" * 40)
    print("(Ingrese -1 como usuario para salir)")
    print()
    
    usuario = input("Usuario: ")
    
    while usuario != "-1":
        password = input("Contraseña: ")
        
        if login(usuario, password):
            print(f"\nBienvenido {usuario}")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            print()
            print("(Ingrese -1 como usuario para salir)")
            usuario = input("Usuario: ")
    
    print("\nSaliendo del sistema...")
    return False