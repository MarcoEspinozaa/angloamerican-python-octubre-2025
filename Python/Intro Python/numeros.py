# =========================
# NÚMEROS EN PYTHON
# =========================

# --- Enteros (int) ---
entero = 10   # número sin decimales
print(entero, type(entero))  # 10 <class 'int'>

# --- Flotantes (float) ---
decimal = 3.14   # número con decimales
print(decimal, type(decimal))  # 3.14 <class 'float'>

# =========================
# OPERACIONES BÁSICAS
# =========================

a = 10
b = 3

# Suma
print(a + b)        # 13 -> int + int = int
print(a + 2.5)      # 12.5 -> int + float = float

# Resta
print(a - b)        # 7 -> int
print(5.5 - 2)      # 3.5 -> float

# Multiplicación
print(a * b)        # 30 -> int
print(a * 2.5)      # 25.0 -> float

# División normal (/)
print(a / b)        # 3.333... -> SIEMPRE devuelve float, aunque ambos sean int
print(10 / 2)       # 5.0 -> noten que devuelve float, no int

# División entera (//)
print(a // b)       # 3 -> devuelve el cociente entero, sin decimales
print(10 // 2)      # 5 -> aquí sí devuelve un int

# Módulo (%)
print(a % b)        # 1 -> el "resto" de la división 10 ÷ 3
print(10 % 2)       # 0 -> porque es divisible exacto

# Potencia (**)
print(a ** b)       # 1000 -> 10^3
print(2 ** 0.5)     # 1.414... -> raíz cuadrada (devuelve float)

# =========================
# DIFERENCIA DE TIPOS
# =========================

# int con int -> devuelve int (excepto división normal, que da float)
print(7 + 2)        # 9 (int)
# int con float -> convierte todo a float
print(7 + 2.0)      # 9.0 (float)

# =========================
# OPERADORES DE COMPARACIÓN
# =========================

x = 5
y = 2

print(x > y)    # True -> 5 es mayor que 2
print(x < y)    # False -> 5 no es menor que 2
print(x == y)   # False -> no son iguales
print(x != y)   # True -> son distintos
print(x >= 5)   # True -> 5 es mayor o igual a 5
print(y <= 2)   # True -> 2 es menor o igual a 2

# =========================
# VALORES GRANDES Y LÍMITES
# =========================

# En Python, los enteros (int) pueden crecer sin límite
# Solo dependen de la memoria del computador.
entero_grande = 10**100   # un 1 seguido de 100 ceros
print(entero_grande)

# Los floats tienen límite, se basan en el estándar IEEE 754 (64 bits).
import sys
print("Máximo float:", sys.float_info.max)   # valor más grande representable
print("Mínimo float positivo:", sys.float_info.min)  # más pequeño positivo
print("Precisión de decimales:", sys.float_info.dig, "dígitos")

# Nota: si un float sobrepasa el máximo permitido → devuelve "inf" (infinito)
print(1e308 * 1000)   # inf