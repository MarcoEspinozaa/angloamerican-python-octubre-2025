# =========================
# DICCIONARIOS EN PYTHON
# =========================

# --- Crear diccionarios ---
# Un diccionario es una colección NO ORDENADA, MUTABLE e INDEXADA de pares clave-valor.
# Las claves deben ser únicas e inmutables (strings, números o tuplas).
# Sintaxis: {clave1: valor1, clave2: valor2, ...}
# se puede declarar así:

alumno = {
    "nombre": "Ana", 
    "edad": 16, 
    "curso": "Python Básico", 
    "notas":[6, 5.5, 4.6]
    }

# o así que es lo normal ya que almarcenen muchos pares clave valor:
diccionario = {
    "nombre": "Ana",
    "edad": 16,
    "curso": "Python Básico"
}
print(diccionario)

# --- Acceder a valores por clave ---
print(diccionario["nombre"])  # Ana
print(diccionario.get("edad")) # 16 -> get() evita error si la clave no existe, pero es poco común ocuparlo

# --- Modificar valores ---
diccionario["edad"] = 17
print(diccionario["edad"])  # 17

# --- Agregar nuevas claves ---
diccionario["ciudad"] = "Santiago"
print(diccionario)

# --- Eliminar elementos ---
del diccionario["curso"]
print(diccionario)

valor_eliminado = diccionario.pop("ciudad")  # elimina y devuelve el valor
print(valor_eliminado)  # Santiago
print(diccionario)

# --- Verificar si una clave existe ---
print("nombre" in diccionario)  # True
print("curso" in diccionario)   # False

# --- Iterar sobre diccionarios --- 
# como ayuda memoria, lo veremos más adelante
# a) Claves
for clave in diccionario:
    print(clave)

# b) Valores
for valor in diccionario.values():
    print(valor)

# c) Claves y valores
for clave, valor in diccionario.items():
    print(f"{clave} → {valor}")

# --- Métodos útiles de diccionarios ---
# Devuelven vistas (views) que reflejan los cambios en el diccionario
print(diccionario.keys())    # dict_keys(['nombre', 'edad'])
print(diccionario.values())  # dict_values(['Ana', 17])
print(diccionario.items())   # dict_items([('nombre', 'Ana'), ('edad', 17)])

# ---  Diccionarios anidados (diccionario dentro de diccionario) --- 
estudiante = {
    "nombre": "Ana",
    "edad": 16,
    "notas": {"matematicas": 5, "python": 6}
}

print(estudiante["notas"]) # {'matematicas': 5, 'python': 6}
print(estudiante["notas"]["python"]) # 6

# --- Copiar diccionarios ---
# Usar copy() para evitar referencias al mismo objeto
copia = diccionario.copy()
print(copia)

# --- Vaciar diccionario --- 
diccionario.clear()
print(diccionario)  # {}
