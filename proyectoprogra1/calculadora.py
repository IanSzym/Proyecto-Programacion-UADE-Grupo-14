from colores import aviso, error, titulo


def obtener_float(mensaje, minimo, maximo):
    """Pide un número flotante al usuario con validación de rango."""
    # Repetimos el pedido hasta que ingrese un numero dentro del rango
    while True:
        try:
            valor = float(input(mensaje))
            if valor < minimo or valor > maximo:
                print(error(f"Valor fuera de rango. Debe estar entre {minimo} y {maximo}."))
            else:
                return valor
        except ValueError:
            print(error("Entrada invalida. Ingrese un numero (ej: 70 o 70.5)."))


def obtener_int(mensaje, opciones_validas):
    """Pide un número entero al usuario validando que esté entre las opciones."""
    # Repetimos el pedido hasta que elija una opcion valida
    while True:
        try:
            valor = int(input(mensaje))
            if valor not in opciones_validas:
                print(error(f"Opcion invalida. Elija entre: {list(opciones_validas)}"))
            else:
                return valor
        except ValueError:
            print(error("Entrada invalida. Ingrese un numero entero."))


def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal."""
    # Formula del imc peso dividido altura al cuadrado
    return peso / (altura ** 2)


def clasificar_imc(imc):
    """Devuelve la categoría del IMC y una descripción."""
    # Segun el valor del imc devolvemos una categoria distinta
    if imc < 18.5:
        return "Bajo peso", "Estas por debajo del peso saludable."
    elif imc < 25:
        return "Peso normal", "Estas en un rango de peso saludable."
    elif imc < 30:
        return "Sobrepeso", "Estas por encima del peso saludable."
    else:
        return "Obesidad", "Se recomienda consultar con un profesional de salud."


def calcular_proteinas(peso, objetivo):
    """
    Calcula gramos de proteína diaria recomendados según el objetivo.
    Factores basados en referencias generales de nutrición deportiva:
     - Mantenimiento: 1.6 g/kg
     - Volumen (ganar músculo): 2.0 g/kg
      - Definición (bajar grasa): 2.2 g/kg
      - Pérdida de peso: 1.2 g/kg
    """
    # Cada objetivo tiene un factor distinto de proteina por kilo
    factores = {
        1: ("Mantenimiento", 1.6),
        2: ("Ganar musculo (volumen)", 2.0),
        3: ("Bajar grasa (definicion)", 2.2),
        4: ("Perder peso", 1.2),
    }
    nombre_obj, factor = factores[objetivo]
    gramos = round(peso * factor, 1)
    return nombre_obj, factor, gramos


def calculadora_corporal():
    """Función principal de la calculadora. Se llama desde el menú."""

    print("\n" + "=" * 40)
    print(titulo("CALCULADORA CORPORAL"))
    print("=" * 40)

    # Datos basicos
    peso = obtener_float("Peso en kg (ej: 70.5): ", minimo=20, maximo=300)
    altura = obtener_float("Altura en metros (ej: 1.75): ", minimo=0.5, maximo=2.5)

    #  IMC 
    imc = calcular_imc(peso, altura)
    categoria, descripcion = clasificar_imc(imc)

    print(titulo("\n--- RESULTADO IMC ---"))
    print(f"IMC: {imc:.2f}")
    print(f"Categoria: {categoria}")
    print(f"{descripcion}")

    # Objetivo del cliente 
    print(titulo("\n--- OBJETIVO ---"))
    print("1. Mantenimiento")
    print("2. Ganar musculo (volumen)")
    print("3. Bajar grasa (definicion)")
    print("4. Perder peso")

    objetivo = obtener_int("Seleccione su objetivo: ", opciones_validas={1, 2, 3, 4})

    # Proteinas
    nombre_obj, factor, gramos = calcular_proteinas(peso, objetivo)

    print(titulo("\n--- RECOMENDACION DE PROTEINAS ---"))
    print(f"Objetivo: {nombre_obj}")
    print(f"Factor aplicado: {factor} g por kg de peso corporal")
    print(f"Proteina diaria recomendada: {gramos} g")
    print(aviso("\nNota: Estos valores son orientativos. Consulta con un nutricionista"))
    print(aviso("para un plan personalizado."))

if __name__ == "__main__":
    calculadora_corporal()
