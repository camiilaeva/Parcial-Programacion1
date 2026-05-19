"""
Archivo llamado: utilidades.py
Aqui se encuentran las funciones para ordenar los caracteres de la contraseña
usando Bubble Sort sin listas.

"""


# =========================
# INTERCAMBIO EN CADENA
# =========================

def intercambiar_caracteres(cadena: str, i: int, j: int) -> str:
    """
    Funcion que devuelve una nueva cadena con los caracteres en las posiciones
    i y j intercambiados, reconstruyendo la cadena posición por posición.

    """
    resultado = ""
    k = 0
    while k < len(cadena):
        if k == i:
            resultado += cadena[j]
        elif k == j:
            resultado += cadena[i]
        else:
            resultado += cadena[k]
        k += 1
    return resultado


# =========================
# ORDENAMIENTO
# =========================

def ordenar_caracteres(password: str, ascendente: bool) -> str:
    """
    Funcion que ordena los caracteres de la contraseña usando Bubble Sort.
    Compara por código ASCII. No usa listas ni sorted().

    Args:
        password:   Contraseña a ordenar.
        ascendente: True para orden ascendente, False para descendente.
    """
    resultado = password
    n = len(resultado)

    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if ascendente == True:
                intercambiar = ord(resultado[j]) > ord(resultado[j + 1])
            else:
                intercambiar = ord(resultado[j]) < ord(resultado[j + 1])
            if intercambiar == True:
                resultado = intercambiar_caracteres(resultado, j, j + 1)
            j += 1
        i += 1

    return resultado