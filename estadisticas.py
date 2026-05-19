"""
Archivo llamado: estadisticas.py
Se encuentran las funciones para generar el reporte estadístico de la contraseña.

"""

from validaciones import contar_tipos


# =========================
# REPETIDOS CONSECUTIVOS
# =========================

def mostrar_repetidos(password: str) -> None:
    """
    Funcion detecta e imprime cada grupo de caracteres consecutivos repetidos.
    
    """
    longitud = len(password)
    i = 0
    hay_repetidos = False

    while i < longitud:
        c = password[i]
        cuenta = 1
        while i + cuenta < longitud and password[i + cuenta] == c:
            cuenta += 1
        if cuenta > 1:
            print(f"  '{c}' -> {cuenta - 1} repeticion/es")
            hay_repetidos = True
        i += cuenta

    if hay_repetidos == False:
        print("  No hay caracteres repetidos consecutivos.")


# =========================
# REPORTE
# =========================

def reporte(password: str) -> None:
    """
    Funcion que genera e imprime el reporte estadístico completo de la contraseña.
    
    """
    letras, numeros, simbolos, espacios = contar_tipos(password)
    longitud = len(password)

    porcentaje_letras   = (letras   * 100) / longitud
    porcentaje_numeros  = (numeros  * 100) / longitud
    porcentaje_simbolos = (simbolos * 100) / longitud

    print("\n--- REPORTE ESTADÍSTICO ---")
    print(f"  Longitud total:         {longitud}")
    print(f"  Porcentaje letras:      {porcentaje_letras:.2f}%")
    print(f"  Porcentaje números:     {porcentaje_numeros:.2f}%")
    print(f"  Porcentaje símbolos:    {porcentaje_simbolos:.2f}%")
    print("\n  Caracteres repetidos consecutivos:")
    mostrar_repetidos(password)