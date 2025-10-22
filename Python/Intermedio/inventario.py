inventario = []
# nombre, cantidad, precio unitario
while True:
    nombre = input("Ingrese nombre producto (escribe fin si quieres terminar): ")
    if nombre.lower() == 'fin':
        break
    cantidad = int(input("Ingresar cantidad: "))
    precio = int(input("Ingresa precio: "))

    #fin = input("Si quiere terminar escriba la palabra fin: ")

    #if fin.lower() == 'fin':
        #break

    producto = {"nombre":nombre, "cantidad":cantidad, "precio":precio}
    inventario.append(producto)

#Finalmente, muestra el inventario completo, el valor total y el producto más caro.

suma = 0
producto_mas_caro = ""
precio_mas_alto = 0

for produc in inventario:
    precio_total = produc["cantidad"] * produc["precio"]
    suma = suma + precio_total
    #Opción 1 =>  suma += produc["cantidad"] * produc["precio"]
    #Opción 2 =>  suma += precio_total

    if produc["precio"] > precio_mas_alto:
        precio_mas_alto = produc["precio"]
        producto_mas_caro = produc["nombre"]


print(inventario)
print(f"El valor total del inventario es de: ${suma} pesos")
print(f"El producto más caro es {producto_mas_caro} con un precio de ${precio_mas_alto} pesos")