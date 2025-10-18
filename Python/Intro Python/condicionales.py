# ===============================
#  CONDICIONALES EN PYTHON
# ===============================

# En Python las decisiones se toman con:
#   if  (si)
#   elif (si no, entonces si...)
#   else (en cualquier otro caso)


# Operadores de comparación: ==  !=  <  <=  >  >=
# Operadores lógicos:        and   or   not
#   - En otros lenguajes (C/JS):  &&  ||  !
#   - En Python se escribe:       and or not


# Nota sobre "valores considerados FALSOS" en condiciones:
#   0, 0.0, "", [], {}, set(), None y False.
# #   Todo lo demás se considera VERDADERO.
#   (No hace falta memorizar la lista: es para entender por qué a veces
#    una cadena vacía "" se toma como Falso, por ejemplo.)


# --- if simple ---
# Si la condición es Verdadera, ejecuta el bloque.
numero = 10
if numero > 0:
    print("El número es positivo")  # -> El número es positivo

# --- if - else ---
# Si la condición NO se cumple, ejecuta el bloque de else.
x = 7
if (x % 2 == 0):
    print("x es par")
else:
    print("x es impar")  # -> x es impar


# --- if - elif - else (varios casos) ---
edad = 30
if edad < 0:
    print("Edad inválida")
elif edad < 18:
    print("Menor de edad")
elif edad < 65:
    print("Adulto")  # -> Adulto
else:
    print("Adulto mayor")

# --- Comparaciones encadenadas ---
# Se puede escribir 0 < n < 10 (equivale a (0 < n) and (n < 10))
n = 5
print(0 < n < 10)  # -> True

# --- Operadores lógicos: and / or / not ---
# Ejemplo típico en otros lenguajes:
#   (a > 0 && b < 10) || !bloqueado
# En Python se escribe:
a = 5
b = 7
bloqueado = False # por tanto lo no bloqueado es True (!bloqueado => no bloqueado)
resultado = (a > 0 and b < 10) or not bloqueado
print(resultado)  # -> True

# evaluar si un numero es menor que 15, par y divisble por 3
numero = int(input("ingrese un numero: "))

if (numero > 15) and (numero%2 == 0) and (numero%3 == 0):
    print("el numero es mayor que 15, par y divisble por 3")
elif numero > 15 and numero%2 == 0 and numero%3 != 0:
    print("el numero es mayor que 15, par y no divisble por 3")

if numero > 15:
    if numero%2 == 0:
        if numero%3 == 0:
            print("el numero es mayor que 15, par y divisble por 3")
        else:
            print("el numero es mayor que 15, par y no divisble por 3")
    
    else: # el numero es impar
        if numero%3 == 0:
            print("el numero es mayor que 15, impar y divisble por 3")
        else:
            print("el numero es mayor que 15, impar y no divisble por 3")


else: # el numero es menor a 15
    if numero%2 == 0:
        if numero%3 == 0:
            print("el numero es menor que 15, par y divisble por 3")
        else:
            print("el numero es menor que 15, par y no divisble por 3")
    
    else: # el numero es impar
        if numero%3 == 0:
            print("el numero es menor que 15, impar y divisble por 3")
        else:
            print("el numero es menor que 15, impar y no divisble por 3")
            

# --- Prioridad de evaluación (importante) ---
# not tiene mayor prioridad que and, y and mayor que or.
# Es decir: not > and > or
print(True or False and False)    # -> True  (se evalúa primero False and False)
print((True or False) and False)  # -> False (por los paréntesis)

# --- "Se detiene" cuando ya sabe el resultado (and / or) ---
# and: si la primera parte es FALSA, NO evalúa la segunda.
num = 0
condicion_inicial = (num != 0)      # -> False
# En la línea siguiente NO se hace 10/num porque 'and' se detiene al ver False
if condicion_inicial and (10 / num > 1):
    print("Esto no se ejecuta")
else:
    print("Con and, si la primera parte es Falsa, se detiene")  # -> esta línea

# or: si la primera parte es VERDADERA, NO evalúa la segunda.
tiene_nombre = "Ana"  # cadena no vacía se considera Verdadera
if tiene_nombre or (3 > 10):
    print("Con or, si la primera parte es Verdadera, se detiene y no evalua, no lo necesita")  # -> esta línea

# --- Textos en condiciones (cadenas vacías) ---
nombre = ""
if nombre == "":
    print("Nombre vacío (comparación directa)")  # -> esta línea
# Otra forma muy usada en Python (leer: “si nombre NO está vacío”):
if nombre:  # cadena vacía se considera Falsa
    # es lo mismo que if True:
    print("Hay nombre")
else:
    print("No hay nombre (cadena vacía)")  # -> esta línea

# --- None en Python (no existe null ni undefined) ---
# None representa “no hay valor”. Se compara con 'is' / 'is not'.
nada = None
print(nada is None)      # -> True  (forma recomendada)
print(nada == None)      # -> True  (posible, pero NO recomendado)

# --- Pertenencia: in / not in ---
texto = "python"
print("py" in texto)       # -> True
print("z" not in texto)    # -> True

# --- Expresión condicional (forma corta) ---
# Se lee: "aprobado" si nota >= 60, en caso contrario "reprobado".
nota = 59
estado = "aprobado" if nota >= 60 else "reprobado"
print(estado)  # -> reprobado
