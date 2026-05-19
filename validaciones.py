"""
Archivo llamado: validaciones.py
Aqui se encuentran las funciones para validar la contraseña y determinar su nivel de seguridad.

"""


# =========================
# FUNCIONES AUXILIARES
# =========================

def es_letra(caracter: str) -> bool:
    """
    Funcion es_letra determina si un carácter es una letra (mayúscula o minúscula).

    """
    codigo = ord(caracter)
    return (codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122)


def es_numero(caracter: str) -> bool:
    """
    Funcion es_numero determina si un carácter es un numero.

    """
    codigo = ord(caracter)
    return codigo >= 48 and codigo <= 57


def es_simbolo(caracter: str) -> bool:
    """
    Funcion es_simbolo determina si un carácter es un símbolo permitido.

    """
    simbolos = "!\"#$%&'()*+,-./"
    i = 0
    while i < len(simbolos):
        if caracter == simbolos[i]:
            return True
        i += 1
    return False


# =========================
# VALIDAR CONTRASEÑA
# =========================

def validar_password(password: str) -> bool:
    """
    Funcion valida que la contraseña cumpla todos los requisitos obligatorios.

    """
    if len(password) == 0:
        print("ERROR. La contraseña no puede estar vacía.")
        return False

    if len(password) < 8:
        print("ERROR. La contraseña debe tener al menos 8 caracteres.")
        return False

    if password[0] == " ":
        print("ERROR. La contraseña no puede comenzar con espacios.")
        return False

    tiene_letra = False
    i = 0
    while i < len(password):
        if es_letra(password[i]):
            tiene_letra = True
        i += 1

    if tiene_letra == False:
        print("La contraseña debe contener al menos una letra.")
        return False

    return True


def hay_password(password: str) -> bool:
    """
    Funcion que verifica que haya una contraseña cargada.

    """
    if len(password) == 0:
        print("Primero debe ingresar una contraseña (opción 1).")
        return False
    return True


# =========================
# NIVEL DE SEGURIDAD
# =========================

def contar_tipos(password: str) -> tuple:
    """
    Funcion que cuenta letras, números, símbolos y espacios en la contraseña.
    """
    letras = 0
    numeros = 0
    simbolos = 0
    espacios = 0

    i = 0
    while i < len(password):
        caracter = password[i]
        if es_letra(caracter):
            letras += 1
        elif es_numero(caracter):
            numeros += 1
        elif caracter == " ":
            espacios += 1
        else:
            simbolos += 1
        i += 1

    return letras, numeros, simbolos, espacios


def nivel_seguridad(password: str) -> str:
    """
    Funcion que determina el nivel de seguridad de la contraseña.

    Los criterios a tener en cuenta: Fuerte / Media / Débil / No definida.

    """
    letras, numeros, simbolos, espacios = contar_tipos(password)

    if len(password) >= 12 and letras > 0 and numeros > 0 and simbolos > 0:
        return "FUERTE"

    if letras > 0 and numeros > 0:
        return "MEDIA"

    if len(password) >= 8 and len(password) <= 9 and letras > 0 and numeros == 0 and simbolos == 0:
        return "DEBIL"

    return "NO DEFINIDA"