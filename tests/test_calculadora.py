from calculadora import calcular_imc, clasificar_imc, calcular_proteinas


def test_calcular_imc():
    resultado = calcular_imc(70, 1.75)
    assert round(resultado, 2) == 22.86


def test_clasificar_imc_bajo_peso():
    categoria, descripcion = clasificar_imc(18)
    assert categoria == "Bajo peso"
    assert descripcion == "Estas por debajo del peso saludable."


def test_clasificar_imc_peso_normal():
    categoria, descripcion = clasificar_imc(22)
    assert categoria == "Peso normal"
    assert descripcion == "Estas en un rango de peso saludable."


def test_clasificar_imc_sobrepeso():
    categoria, descripcion = clasificar_imc(27)
    assert categoria == "Sobrepeso"
    assert descripcion == "Estas por encima del peso saludable."


def test_clasificar_imc_obesidad():
    categoria, descripcion = clasificar_imc(31)
    assert categoria == "Obesidad"
    assert descripcion == "Se recomienda consultar con un profesional de salud."


def test_calcular_proteinas():
    objetivo, factor, gramos = calcular_proteinas(70, 2)
    assert objetivo == "Ganar musculo (volumen)"
    assert factor == 2.0
    assert gramos == 140.0
