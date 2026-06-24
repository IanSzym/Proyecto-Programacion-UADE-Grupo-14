from login import login


def test_login_correcto():
    assert login("admin", "admin123")


def test_login_password_incorrecto():
    assert not login("admin", "otra")


def test_login_usuario_inexistente():
    assert not login("usuario", "admin123")
