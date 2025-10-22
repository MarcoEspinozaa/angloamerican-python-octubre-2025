''' Promedio hasta cero El usuario ingresa números uno a uno. Cuando introduce 0, el programa muestra el promedio de todos los números positivos ingresados. '''

acumulador = 0
cantidad = 0

while True:
    numero = int(input("Ingrese un número: "))
    
    if numero == 0:
        print(f"Promedio: {acumulador/cantidad}")
        break

    if numero > 0:
        acumulador = acumulador + numero
        # acumulador += numero
        cantidad = cantidad + 1
        # cantidad += 1