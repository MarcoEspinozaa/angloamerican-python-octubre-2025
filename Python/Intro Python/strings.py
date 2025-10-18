# =========================
# STRINGS EN PYTHON
# =========================

# Un string es una cadena de texto
# Se pueden usar comillas simples, dobles o triples

# --- Declaración básica ---
texto1 = 'Hola'
texto2 = "Mundo"
print(texto1)  # Imprime: Hola
print(texto2)  # Imprime: Mundo
print(type(texto1))  # <class 'str'>
print(type(texto2))  # <class 'str'>

# --- Se puede imprimir ambos string en un print ---
print(texto1, texto2)  # Hola Mundo

# --- Triple comillas (multilínea) ---
texto3 = '''Este es un texto
que puede ocupar
varias líneas'''
print(texto3)

# =========================
# CONCATENACIÓN
# =========================

# Unir dos o más strings con +
saludo = texto1 + " " + texto2
print(saludo)  # Hola Mundo

# =========================
# REPETICIÓN
# =========================

# Se puede repetir un string con el operador *
eco = "repito! " * 3
print(eco)  # repito! repito! repito!

# =========================
# ACCEDER A CARACTERES
# =========================

# Los strings son secuencias, es decir listas de caracteres (char), cada letra tiene una posición (índice)
palabra = "Python"
print(palabra[0])   # P (primer carácter, índice 0)
print(palabra[-1])  # n (último carácter) -> lo veremos más adelante en las listas

# =========================
# FORMATO DE STRINGS
# =========================

nombre = "Ana"
edad = 16

# f-strings 
print(f"Hola {nombre}, el próximo año tendrás {edad + 1} años")


# =========================
# FUNCIONES/MÉTODOS ÚTILES DE STRING, SE DEJA COMO AYUDA MEMORIA, LO VEREMOS MÁS ADELANTE
# =========================

print(len(palabra))       # longitud: 6
print(palabra.upper())    # PYTHON (mayúsculas)
print(palabra.lower())    # python (minúsculas)
print(palabra.capitalize()) # Python Es El Mejor Lenguaje (cada nueva palabra empieza con mayúscula)
print(palabra.title())    # Python (cada palabra capitalizada)
print(palabra.replace("Py", "My"))  # Mython
print("   hola   ".strip())  # quita espacios al inicio y al final

# Muchos métodos de los strings en Python devuelven un valor booleano
# (True o False) dependiendo de si se cumple cierta condición.

# --- isdigit() --- ¿Este texto es solo números?
# Revisa si TODOS los caracteres del string son dígitos (números del 0 al 9).
print("123".isdigit())     # True → porque todos los caracteres son números.
print("123a".isdigit())    # False → porque contiene la letra "a".

# --- isalpha() --- ¿Este texto es solo letras?
# Revisa si TODOS los caracteres son letras (a-z o A-Z, sin espacios ni números).
print("abc".isalpha())     # True → solo letras.
print("abc123".isalpha())  # False → porque hay números.
print("hola mundo".isalpha()) # False → porque contiene un espacio.

# --- isalnum() --- ¿Este texto es solo letras o números (sin símbolos)?
# Revisa si TODOS los caracteres son alfanuméricos (letras o números, sin símbolos).
print("abc123".isalnum())  # True → contiene letras y números, permitido.
print("abc!".isalnum())    # False → porque tiene un símbolo (!).
print("12345".isalnum())   # True → solo números también es válido.

# --- startswith() --- ¿El texto empieza con esto?
# Revisa si el string EMPIEZA con cierta subcadena.
print("hola".startswith("ho"))   # True → comienza con "ho".
print("hola".startswith("la"))   # False → no comienza con "la".

# --- endswith() --- ¿El texto termina con esto?
# Revisa si el string TERMINA con cierta subcadena.
print("hola".endswith("la"))     # True → termina con "la".
print("hola".endswith("ho"))     # False → no termina con "ho".