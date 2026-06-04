import re

def validar_dni(dni):
    try:
        patron = '^[0-9]{8}$'
        return re.match(patron, str(dni))
    except TypeError:
        return False

def validar_telefono(telefono):
    try:
        patron = '^[0-9]{2,4}[- ]?[0-9]{3,4}[- ]?[0-9]{4}$'
        return re.match(patron, str(telefono))
    except TypeError:
        return False

def validar_email(email):
    try:
        patron = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[.][a-zA-Z]{2,}$'
        return re.match(patron, str(email))
    except TypeError:
        return False

def formatear_nombre(nombre):
    try:
        return str(nombre).title()
    except TypeError:
        return ""
