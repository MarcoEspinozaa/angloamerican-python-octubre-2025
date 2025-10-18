# ===============================
#  TUPLAS EN PYTHON
# ===============================

# --- Crear una tupla ---
tupla1 = (1, 2, 3, 4, 5)          # Tupla de números enteros
tupla2 = ("hola", "mundo", 2025)  # Tupla con distintos tipos de datos
tupla3 = (True, False, True)      # Tupla de valores booleanos
print(tupla1)
print(tupla2)
print(tupla3)

# --- Tupla con un solo elemento (importante) ---
entero = (5 )  # Esto NO es una tupla, es un int
print(type(entero))  # <class 'int'>
tupla_uno = (5,)   # Para que Python lo reconozca como tupla, lleva coma
print(type(tupla_uno))  # <class 'tuple'>

# --- Acceder a los elementos de una tupla ---
print(tupla1[0])   # Primer elemento (posición 0) -> 1
print(tupla2[1])   # Segundo elemento -> "mundo"
print(tupla2[-1])  # Último elemento -> 2025

# --- Slicing (cortar secciones de la tupla), creo que no lo puse en las listas, funciona igual ---
print(tupla1[1:4])  # Elementos desde posición 1 hasta 3 -> (2, 3, 4) - va desde el indice 1 hasta el n-1
print(tupla1[:3])   # Desde el inicio hasta posición 2 -> (1, 2, 3)
print(tupla1[::2])  # Saltando de 2 en 2 -> (1, 3, 5)

# --- Inmutabilidad de las tuplas ---
# A diferencia de las listas, las tuplas NO se pueden modificar (son inmutables)
# tupla1[0] = 99 -> ERROR: las tuplas no permiten reasignación
# tampoco se pueden agregar o eliminar elementos
# Pero sí se pueden crear nuevas tuplas a partir de otras
nueva_tupla = tupla1 + (6, 7, 8)
print(nueva_tupla)  # (1, 2, 3, 4, 5, 6, 7, 8)

# --- Métodos útiles de las tuplas ---
# Aunque las tuplas son inmutables, tienen algunos métodos útiles
print(tupla1.count(3))  # Cuenta cuántas veces aparece el valor 3 -> 1
print(tupla1.index(4))  # Devuelve la posición donde está el 4 -> 3


# --- Tuplas anidadas (tupla dentro de otra) ---
tupla_anidada = ((1, 2), (3, 4), (5, 6))
print(tupla_anidada[0])     # (1, 2)
print(tupla_anidada[0][1])  # 2

# --- Desempaquetado de tuplas, funciona tambien para lista, creo no lo puse ---
# Asignar los valores de una tupla a varias variables
a, b, c = (10, 20, 30)  
print(a, b, c)  # 10 20 30

# Si se desconoce el número exacto de elementos, usar "*"
x, *y = (1, 2, 3, 4, 5)
print(x)  # 1
print(y)  # [2, 3, 4, 5]

# --- Uso común: retorno múltiple en funciones ---
# DEJARLOS COMO AYUDA MEMORIA, LO ACLARAREMOS MÁS ADELANTE
def coordenadas():
    return (10.5, 20.8)  # Una función puede devolver una tupla

lat, lon = coordenadas()
print(f"Latitud: {lat}, Longitud: {lon}")

# --- Conversión entre lista y tupla
lista = [1, 2, 3]
tupla_convertida = tuple(lista)
print(tupla_convertida)  # (1, 2, 3)

lista_nueva = list(tupla1)
print(lista_nueva)  # [1, 2, 3, 4, 5]