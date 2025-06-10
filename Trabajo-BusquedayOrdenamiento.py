# Funcion que genera una lista de nombres únicos de alumnos y la desordena aleatoriamente
def generar_lista_alumnos(cantidad):
    import random
    lista = [f"Alumno{i:03}" for i in range(1, cantidad + 1)]
    random.shuffle(lista)
    return lista

# Funcion ordena la lista alfabéticamente usando el algoritmo Bubble Sort
def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Funcion realiza búsqueda binaria en una lista ordenada y retorna la posición del elemento
def busqueda_binaria(lista, objetivo):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

import random
random.seed(42)  # Fijamos la semilla para obtener siempre la misma lista desordenada
alumnos = generar_lista_alumnos(500)  # Crear y desordenar 500 nombres de alumnos
alumnos = ordenar_lista(alumnos)  # Ordenar alfabéticamente la lista de alumnos
notas = {}  # Diccionario para registrar las notas asignadas


# Solicita nombre del alumno
nombre = input("Ingrese el nombre del alumno (ej. Alumno001): ")  
valido = False  # Controla que se ingrese una nota válida
while not valido:
    entrada = input("Ingrese la nota del alumno (entre 0 y 10): ")
    try:
        nota = float(entrada)  # Convierte la entrada a número decimal
        if 0 <= nota <= 10:
            valido = True
        else:
            print("La nota debe estar entre 0 y 10.")
    except ValueError:
        print("La nota debe ser un número decimal válido.")

indice_binaria = busqueda_binaria(alumnos, nombre)

indice = indice_binaria  # Se usa la posición devuelta por la búsqueda binaria
if indice != -1:
    notas[nombre] = nota
    print(f"Nota registrada para {nombre}: {nota}")  # Confirmación de registro
else:
    print("El alumno no se encuentra en la lista.")  # Mensaje si no se encuentra el alumno
