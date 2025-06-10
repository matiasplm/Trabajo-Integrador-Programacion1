# Algoritmos de Búsqueda y Ordenamiento en Python

**Trabajo Integrador – Programación I**

**Autores:** Matias Perez, Marcos Pousada
**Profesor:** Nicolás Quirós
**Tutor:** Carla Bustos
**Comisión:** 19
**Fecha de Entrega:** 09/06/2025

---

## Descripción

Este proyecto implementa y compara algoritmos de ordenamiento y búsqueda en Python mediante un caso práctico: registrar la nota de un alumno tras buscar su nombre en una lista de 500 estudiantes.

Los objetivos principales son:

* Comprender la lógica y características de distintos algoritmos de ordenamiento (Bubble Sort, y perspectivas de Quick Sort, Insertion Sort, Selection Sort).
* Implementar búsqueda binaria y validar su eficiencia frente a búsqueda lineal.
* Integrar estructuras de datos (listas y diccionarios) para gestionar datos de forma eficiente.
* Desarrollar un programa modular, robusto y fácil de usar.

## Tabla de Contenidos

1. [Estructura del Proyecto](#estructura-del-proyecto)
2. [Algoritmos Implementados](#algoritmos-implementados)
3. [Instalación y Requisitos](#instalación-y-requisitos)
4. [Uso](#uso)
5. [Resultados y Rendimiento](#resultados-y-rendimiento)
6. [Metodología](#metodología)
7. [Mejoras y Extensiones Futuras](#mejoras-y-extensiones-futuras)
8. [Autores](#autores)
9. [Licencia](#licencia)

## Estructura del Proyecto

```
├── Trabajo-BusquedayOrdenamiento.py  # Script principal con algoritmos de búsqueda y ordenamiento
└── README.md                       # Este archivo
```

## Algoritmos Implementados

* **Bubble Sort:** Ordenamiento por comparación de pares adyacentes.
* **Bubble Sort (estudio):** Análisis de complejidad y comportamiento práctico en 500 elementos.
* **Búsqueda Binaria:** División y conquista para listas ordenadas (O(log n)).
* **Búsqueda Lineal (comparativa):** Caso base para contrastar tiempos.

## Instalación y Requisitos

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/matiasplm/Trabajo-Integrador-Programacion1.git
   ```
2. Navegar al directorio:

   ```bash
   cd Trabajo-Integrador-Programacion1
   ```
3. Crear y activar un entorno virtual (opcional, pero recomendado):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
4. Instalar dependencias (ninguna más allá de la biblioteca estándar de Python).

## Uso

Ejecutar el programa principal y seguir las instrucciones:

```bash
python Trabajo-BusquedayOrdenamiento.py
```

1. Ingresar el nombre del alumno (ej. `Alumno012`).
2. Ingresar la nota (valor decimal entre 0 y 10).
3. El programa verificará existencia, registrará la nota y mostrará el resultado.

## Resultados y Rendimiento

* La lista de 500 alumnos se ordena correctamente con Bubble Sort.
* La búsqueda binaria se mostró significativamente más rápida que la lineal en todos los casos de prueba (inicio, medio y fin).
* Validación robusta de entradas, manejo de errores y acumulación de notas en un diccionario.

## Metodología

1. **Investigación:** Lectura de documentación oficial de Python y materiales de la cátedra.
2. **Diseño:** Definición de funciones modulares de ordenamiento y búsqueda.
3. **Implementación:** Desarrollo en Python, pruebas iterativas y control de versiones con Git.
4. **Pruebas:** Casos de prueba para rangos de notas, búsquedas en distintos puntos de la lista y mediciones de tiempo.

## Mejoras y Extensiones Futuras

* Implementar algoritmos más eficientes: Merge Sort, Quick Sort.
* Cargar datos desde archivos o bases de datos.
* Crear interface gráfica con Tkinter o web (Flask/Django).
* Añadir persistencia de notas en un archivo CSV o JSON.

## Autores

* **Matias Perez** – Desarrollo de ordenamiento y presentación de resultados.
* **Marcos Pousada** – Implementación de búsqueda, validación de datos y redacción del informe.

## Licencia

Este proyecto está bajo la licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

---



