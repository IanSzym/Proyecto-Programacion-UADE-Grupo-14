try:
    from colorama import Fore, Style, init
    init(strip=False, convert=True)
except ImportError:
    class Fore:
        GREEN = "\033[32m"
        RED = "\033[31m"
        YELLOW = "\033[33m"
        CYAN = "\033[36m"

    class Style:
        BRIGHT = "\033[1m"
        RESET_ALL = "\033[0m"


def titulo(texto):
    return Style.BRIGHT + Fore.CYAN + texto + Style.RESET_ALL


def correcto(texto):
    return Fore.GREEN + texto + Style.RESET_ALL


def error(texto):
    return Fore.RED + texto + Style.RESET_ALL


def aviso(texto):
    return Fore.YELLOW + texto + Style.RESET_ALL
