# =========================
# LISTAS EN PYTHON
# =========================

# Una lista es una colección ORDENADA y MUTABLE de elementos.
# Puede contener cualquier tipo de dato (incluso mezclados).

# --- Crear listas ---
vacia = []                 # lista vacía
numeros = [1, 2, 3, 4, 5]  # lista de enteros
mixta = [1, "hola", 3.14]  # lista con distintos tipos

print(numeros)
print(mixta)

# --- Acceso a elementos (índices) ---
print(numeros[0])   # 1 -> primer elemento
print(numeros[-1])  # 5 -> último elemento

# --- Modificar elementos (son mutables) ---
numeros[0] = 10
print(numeros)  # [10, 2, 3, 4, 5]

# --- Agregar elementos ---
numeros.append(6)      # agrega al final
print(numeros)         # [10, 2, 3, 4, 5, 6]

numeros.insert(1, 20)  # inserta en posición 1
print(numeros)         # [10, 20, 2, 3, 4, 5, 6]

# --- Eliminar elementos ---
numeros.remove(20)     # elimina primera coincidencia, el primer 20
print(numeros)

ultimo = numeros.pop() # elimina el último y lo devuelve el indice
print("Se eliminó:", ultimo)
print(numeros)

del numeros[0]         # elimina por índice
print(numeros)

# --- Otras operaciones útiles ---
print(len(numeros))         # longitud de la lista
print(3 in numeros)         # True si 3 está en la lista
print(numeros.count(3))     # cuántas veces aparece el 3
print(numeros.index(3))     # posición del primer 3

# --- Ordenar listas ---
numeros.sort()              # ordena la lista (menor a mayor)
print(numeros)

numeros.sort(reverse=True)  # ordena de mayor a menor
print(numeros)

# --- Copiar listas ---
copia = numeros.copy()
print("Copia:", copia)

# --- Listas dentro de listas (anidadas) ---
matriz = [[1, 2], [3, 4], [5, 6]]
print(matriz[0])       # [1, 2]
print(matriz[0][1])    # 2 -> fila 0, columna 1