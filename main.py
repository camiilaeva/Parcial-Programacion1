"""
Archivo llamado: main.py
Sistema de Procesamiento de Contraseñas
Programación 1 - Parcial APD

Aqui comienza el programa y se controla el menú principal
e invoca las funciones de cada módulo.

"""

from validaciones import validar_password, hay_password, nivel_seguridad
from analisis import buscar_caracter, invertir_password, es_palindromo, mostrar_tipos
from estadisticas import reporte
from utilidades import ordenar_caracteres


# =========================
#  BIENVENIDOS AL MENÚ 
# =========================

def mostrar_menu() -> None:
    """
    Funcion que muestra el menú principal del sistema.
    """
    print("\n===== MENÚ =====")
    print("1 - Ingresar contraseña")
    print("2 - Validar nivel de seguridad")
    print("3 - Contar tipos de caracteres")
    print("4 - Buscar carácter")
    print("5 - Mostrar contraseña invertida")
    print("6 - Generar reporte estadístico")
    print("7 - Verificar palíndromo")
    print("8 - Ordenar caracteres de la contraseña")
    print("9 - Salir")


# =========================
# PROGRAMA PRINCIPAL
# =========================

def main() -> None:
    """
    Función principal. Controla el flujo del programa.

    """
    password = ""
    opcion = -1

    while opcion != 9:

        mostrar_menu()
        opcion = int(input("Ingrese una opción por favor: "))

        if opcion == 1:
            nueva = input("Ingrese contraseña: ")
            if validar_password(nueva):
                password = nueva
                print("Perfecto. Contraseña guardada correctamente.")

        elif opcion == 2:
            if hay_password(password):
                print(f"Nivel: {nivel_seguridad(password)}")

        elif opcion == 3:
            if hay_password(password):
                mostrar_tipos(password)

        elif opcion == 4:
            if hay_password(password):
                caracter = input("Ingrese carácter a buscar: ")
                buscar_caracter(password, caracter)

        elif opcion == 5:
            if hay_password(password):
                print(invertir_password(password))

        elif opcion == 6:
            if hay_password(password):
                reporte(password)

        elif opcion == 7:
            if hay_password(password):
                if es_palindromo(password):
                    print("Es palíndromo.")
                else:
                    print("No es palíndromo.")

        elif opcion == 8:
            if hay_password(password):
                print("  1 - Ascendente")
                print("  2 - Descendente")
                criterio = input("  Ingrese criterio: ")
                if criterio == "1":
                    print(ordenar_caracteres(password, True))
                elif criterio == "2":
                    print(ordenar_caracteres(password, False))
                else:
                    print("Opción inválida.")

        elif opcion == 9:
            print("Salir. Fin del programa")


        else:
            print("Opción inválida.")


# =========================
# INICIO
# =========================

main()