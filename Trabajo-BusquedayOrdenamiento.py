import random
random.seed(42)
alumnos = generar_lista_alumnos(100)
alumnos = ordenar_lista(alumnos)
notas = {}

nombre = input("Ingrese el nombre del alumno (ej. alumno001): ")
valido = False
while not valido:
    entrada = input("Ingrese la nota del alumno (entre 0 y 10): ")
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            valido = True
        else:
            print("La nota debe estar entre 0 y 10.")
    except ValueError:
        print("La nota debe ser un número decimal válido.")

import time

inicio_binaria = time.perf_counter()
indice_binaria = busqueda_binaria(alumnos, nombre)
tiempo_binaria = time.perf_counter() - inicio_binaria

inicio_lineal = time.perf_counter()
indice_lineal = busqueda_lineal(alumnos, nombre)
tiempo_lineal = time.perf_counter() - inicio_lineal

indice = indice_binaria
if indice != -1:
    notas[nombre] = nota
    print(f"Nota registrada para {nombre}: {nota}")
else:
    print("El alumno no se encuentra en la lista.")

print(f"Tiempo de búsqueda binaria: {tiempo_binaria:.8f} segundos")
print(f"Tiempo de búsqueda lineal: {tiempo_lineal:.8f} segundos")