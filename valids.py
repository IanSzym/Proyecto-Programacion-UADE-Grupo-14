import re

def validar_dni(dni):
    patron = '^[0-9]{8}$'
    return re.match(patron, dni)

def validar_telefono(telefono):
    patron = '^[0-9]{2,4}[- ]?[0-9]{3,4}[- ]?[0-9]{4}$'
    return re.match(patron, telefono)

def validar_email(email):
    patron = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[.][a-zA-Z]{2,}$'
    return re.match(patron, email)

def formatear_nombre(nombre):
    return nombre.title()