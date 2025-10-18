# =========================
# SETS EN PYTHON
# =========================

# --- Crear sets ---
# Un set es una colección NO ORDENADA y NO INDEXADA de elementos únicos (sin duplicados).
# Se definen con llaves {} o con la función set()
conjunto1 = {1, 2, 3, 4, 5}       # set de números
conjunto2 = {"a", "b", "c", "a"}  # los elementos repetidos se eliminan automáticamente

print(conjunto1)  # {1, 2, 3, 4, 5}
print(conjunto2)  # {'a', 'b', 'c'} -> 'a' no se repite

# --- Crear un set vacío ---
vacio = set()    # NOTA: {} crea un diccionario vacío, no un set
print(vacio)     # set()

# --- Acceder a elementos ---
# Los sets NO tienen índice, por lo que NO se puede hacer conjunto1[0]
# Podemos recorrerlos con un bucle, entender que no se puede acceder por le índice, el ciclo lo vemos más adelante
for elem in conjunto1:
    print(elem)
 
# --- Agregar y eliminar elementos ---
conjunto1.add(6)     # agregar un elemento
print(conjunto1)     # {1, 2, 3, 4, 5, 6}

conjunto1.remove(3)  # eliminar un elemento (error si no existe)
print(conjunto1)

conjunto1.discard(10) # eliminar si existe, no da error si no existe
print(conjunto1)

# --- Operaciones entre sets (similares a teoría de conjuntos) ---
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

print(setA.union(setB))        # {1, 2, 3, 4, 5, 6} -> unión
print(setA.intersection(setB)) # {3, 4} -> intersección
print(setA.difference(setB))   # {1, 2} -> elementos en A pero no en B
print(setB.difference(setA))   # {5, 6} -> elementos en B pero no en A

# --- Comprobación de pertenencia ---
print(2 in setA)   # True -> 2 está en A
print(5 in setA)   # False -> 5 no está en A

# --- Operaciones con operadores simbólicos ---
print(setA | setB)   # unión -> {1,2,3,4,5,6}
print(setA & setB)   # intersección -> {3,4}
print(setA - setB)   # diferencia -> {1,2}
print(setA ^ setB)   # diferencia simétrica -> {1,2,5,6}

# --- Conversión entre tipos ---
# Convertir lista a set (elimina duplicados)    
lista = [1, 2, 2, 3, 4, 4, 5]
conjunto_desde_lista = set(lista)  # elimina duplicados
print(conjunto_desde_lista)  # {1, 2, 3, 4, 5}

# --- Vaciar un set ---
conjunto1.clear()
print(conjunto1)  # set()