from valids import validar_dni, validar_telefono, validar_email, formatear_nombre


def test_validar_dni_correcto():
    assert validar_dni("12345678")


def test_validar_dni_incorrecto():
    assert not validar_dni("1234")
    assert not validar_dni("1234567a")


def test_validar_telefono_correcto():
    assert validar_telefono("11 1234 5678")
    assert validar_telefono("011-1234-5678")


def test_validar_telefono_incorrecto():
    assert not validar_telefono("telefono")


def test_validar_email_correcto():
    assert validar_email("usuario@email.com")


def test_validar_email_incorrecto():
    assert not validar_email("usuarioemail.com")
    assert not validar_email("usuario@")


def test_formatear_nombre():
    assert formatear_nombre("juan perez") == "Juan Perez"
    assert formatear_nombre("MARIA") == "Maria"
