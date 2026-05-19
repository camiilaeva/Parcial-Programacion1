"""
Archivo llamado: analisis.py
Aqui se encuentran las funciones de análisis sobre la contraseña

"""

from validaciones import contar_tipos


# =========================
# BUSCAR CARÁCTER
# =========================

def buscar_caracter(password: str, buscado: str) -> None:
    """
    Funcion que busca un carácter en la contraseña e imprime sus posiciones y cantidad.

    """
    contador = 0
    i = 0
    while i < len(password):
        if password[i] == buscado:
            print(f"  Aparece en posición {i}")
            contador += 1
        i += 1
    print(f"  Cantidad total: {contador}")


# =========================
# INVERTIR
# =========================

def invertir_password(password: str) -> str:
    """
    Funcion que devuelve la contraseña con sus caracteres en orden inverso.

    """
    invertida = ""
    i = len(password) - 1
    while i >= 0:
        invertida += password[i]
        i -= 1
    return invertida


# =========================
# PALÍNDROMO
# =========================

def es_palindromo(password: str) -> bool:
    """
    Funcion que verifica si la contraseña se lee igual de izquierda a derecha
    que de derecha a izquierda.

    """
    invertida = invertir_password(password)
    i = 0
    while i < len(password):
        if password[i] != invertida[i]:
            return False
        i += 1
    return True


# =========================
# CONTAR TIPOS (reexportado para uso en menú)
# =========================

def mostrar_tipos(password: str) -> None:
    """
    Funcion que muestra la cantidad de letras, números, símbolos y espacios.
    """
    letras, numeros, simbolos, espacios = contar_tipos(password)
    print(f"  Letras:   {letras}")
    print(f"  Números:  {numeros}")
    print(f"  Símbolos: {simbolos}")
    print(f"  Espacios: {espacios}")