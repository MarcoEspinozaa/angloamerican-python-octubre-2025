# ===============================
#  CICLOS EN PYTHON
# ===============================

# Dos tipos principales:
#   for -> recorre elementos de una secuencia (lista, tupla, cadena, etc.)
#   while -> repite mientras una condición sea Verdadera

# Palabras clave que controlan el ciclo:
#   break -> detiene el ciclo por completo
#   continue -> salta a la siguiente iteración
#   pass -> no hace nada (marcador de posición)

# 'else' en ciclos:
#  El bloque 'else' de un for/while se ejecuta SOLO si el ciclo terminó sin usar 'break'.


# --- for sobre lista ---
numeros = [10, 20, 30]
for n in numeros:
    print(n)
# Salida:
# 10
# 20
# 30

# --- for sobre tupla (desempaquetado) ---
pares = [(1, 2), (3, 4)]
for a, b in pares:
    print(a, b)
# Salida:
# 1 2
# 3 4

# --- for sobre cadena (caracter por caracter) ---
for ch in "PY":
    print(ch)
# Salida:
# P
# Y

# --- for sobre set ---
# Atención: los conjuntos (set) no garantizan orden.
colores = {"rojo", "verde", "azul", "rojo"}
for c in colores:
    print(c)
# Salida (puede variar el orden):
# rojo
# verde
# azul
# (solo una vez cada color)

# --- for sobre diccionario: keys / values / items ---
persona = {"nombre": "Ana", "edad": 29}

print(list(persona.keys()))    # -> ['nombre', 'edad']
print(list(persona.values()))  # -> ['Ana', 29]
print(list(persona.items()))   # -> [('nombre','Ana'), ('edad',29)]

for clave, valor in persona.items():
    print(clave, "->", valor)
# Salida:
# nombre -> Ana
# edad -> 29

# --- range(inicio, fin, paso) ---
# 'fin' es EXCLUSIVO (llega hasta fin-1)
for i in range(5):  # 0,1,2,3,4
    print(i, end=" ")
print()  # -> 0 1 2 3 4

for i in range(1, 6):  # 1,2,3,4,5
    print(i, end=" ")
print()  # -> 1 2 3 4 5

for i in range(10, 0, -2):  # 10,8,6,4,2
    print(i, end=" ")
print()  # -> 10 8 6 4 2

# --- enumerate(iterable, start=1) ---
frutas = ["manzana", "pera", "uva"]
for indice, fruta in enumerate(frutas):
    print(indice, fruta)
# Salida:
# 1 manzana
# 2 pera
# 3 uva

# --- zip(lista1, lista2, ...) ---
# Recorre en paralelo varios iterables (se detiene en el más corto)
precios = [1000, 1200, 900]
for fruta, precio in zip(frutas, precios):
    print(fruta, "->", precio)
# Salida:
# manzana -> 1000
# pera -> 1200
# uva -> 900

# --- while (repite mientras la condición sea Verdadera) ---
contador = 1
while contador <= 3:
    print("contador:", contador)
    contador += 1
# Salida:
# contador: 1
# contador: 2
# contador: 3

# --- break / continue / pass ---
# break: detiene el ciclo
for i in range(1, 6):
    if i == 3:
        break
    print("i:", i)
# Salida:
# i: 1
# i: 2

# continue: salta el resto de la vuelta y sigue con la siguiente
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print("impar:", i)
# Salida:
# impar: 1
# impar: 3
# impar: 5

# pass: no hace nada (sirve como “bloque vacío”)
for i in range(3):
    pass  # no imprime nada

# --- for ... else (se ejecuta SOLO si NO hubo break) ---
valores = [2, 4, 6, 8]
objetivo = 5
for v in valores:
    if v == objetivo:
        print("Encontré", objetivo)
        break
else:
    print("No lo encontré (no hubo break)")  # -> esta línea

# --- Patrones útiles sin usar funciones ---
# 1) Suma de 1..N
N = 5
suma = 0
for i in range(1, N + 1):
    suma += i
print("Suma 1..N =", suma)  # -> 15

# 2) Filtrar pares de una lista
lista = [1, 2, 3, 4, 5, 6]
pares = []
for num in lista:
    if num % 2 == 0:
        pares.append(num)
print("Pares ->", pares)  # -> [2, 4, 6]

# 3) Bucle con “palabra de corte”
entradas = ["10", "20", "fin", "100"]  # '100' ya no se procesa
total = 0
for dato in entradas:
    if dato.lower() == "fin":
        break
    total += int(dato)
print("Total acumulado ->", total)  # -> 30
