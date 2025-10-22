suma = 0

for i in range(1, 501):
    if i % 2 != 0:
    # if i % 2 == 1:
        suma = suma + i
        # suma += i

#print(suma)

'''edad = int(input("Ingresa tu edad: "))
if edad > 18:
    if edad % 2 == 0:
        print("es mayor de edad y su edad es par")
    else:
        print("es mayor de edad y su edad es impar")

if (edad > 18) and (edad % 2 == 0):
    print("es mayor de edad y su edad es par")
elif (edad > 18) and (edad % 2 != 0):
     print("es mayor de edad y su edad es impar")'''


numero = int(input("Ingrese un numero: ")) # con input capturamos lo que el usuario ingresa por teclado, se captura como string, para poder operar lo transformamos a entero

# la idea es mostrar el numero con su tabla de multiplicar
# 1 x 1 = 1
# 1 x 2 = 2 
# 1 x 3 = 3 
# .....
# 1 x 10 = 10

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")