# 🔐 Sistema de Procesamiento de Contraseñas

> **Programación 1 — Examen Parcial APD**
> Universidad Tecnológica Nacional — Avellaneda

---

## 📋 Descripción

Sistema desarrollado en Python que permite analizar y validar contraseñas ingresadas por usuarios, implementando distintas funcionalidades como validación, análisis estadístico y ordenamiento de caracteres.

---

## 🗂️ Estructura del proyecto

```
Parcial-Programacion1/
│
├── main.py            → Menú principal y flujo del programa
├── validaciones.py    → Validación de contraseña y nivel de seguridad
├── analisis.py        → Búsqueda, inversión y palíndromo
├── estadisticas.py    → Reporte estadístico
└── utilidades.py      → Ordenamiento Bubble Sort
```

---

## ⚙️ Funcionalidades

| # | Opción | Descripción |
|---|--------|-------------|
| 1 | Ingresar contraseña | Valida y guarda la contraseña |
| 2 | Validar nivel de seguridad | Indica si es Débil, Media o Fuerte |
| 3 | Contar tipos de caracteres | Letras, números, símbolos y espacios |
| 4 | Buscar carácter específico | Posiciones y cantidad de apariciones |
| 5 | Mostrar contraseña invertida | Sin slicing ni funciones avanzadas |
| 6 | Generar reporte estadístico | Longitud, porcentajes y repetidos |
| 7 | Verificar si es palíndromo | Ej: radar, ana |
| 8 | Ordenar caracteres | Ascendente o descendente por ASCII |
| 9 | Salir | Finaliza el programa |

---

## ✅ Validaciones de la contraseña

- ❌ No puede estar vacía
- ❌ No puede comenzar con espacios
- ❌ No puede tener menos de 8 caracteres
- ✅ Debe contener al menos una letra

---

## 🔒 Niveles de seguridad

| Nivel | Criterio |
|-------|----------|
| 🔴 Débil | 8 a 9 caracteres, solo letras |
| 🟡 Media | Tiene letras y números |
| 🟢 Fuerte | Letras + números + símbolos + 12 caracteres mínimo |

---

## 🚫 Restricciones aplicadas

- ✅ Sin métodos de cadenas (`.upper()`, `.isalpha()`, etc.)
- ✅ Sin métodos de listas (`.append()`, `.sort()`, etc.)
- ✅ Sin `sorted()` ni slicing
- ✅ Sin listas por comprensión
- ✅ Sin operador `in`
- ✅ Solo se usaron: `len()`, `int()`, `float()`, `str()`, `range()`, `ord()`

---


> Todos los archivos deben estar en la misma carpeta.

---

## 🛠️ Tecnologías

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![VSCode](https://img.shields.io/badge/Editor-VSCode-blue?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![GitHub](https://img.shields.io/badge/Repositorio-GitHub-black?style=for-the-badge&logo=github&logoColor=white)
