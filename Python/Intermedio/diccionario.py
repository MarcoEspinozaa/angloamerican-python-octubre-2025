'''Crea un diccionario de palabras y sus sinónimos. Permite agregar nuevas o buscar existentes.
Ayuda: Si la palabra ya existe, agrega con append(). Si no, crea nueva lista.'''

diccionario = {}

while True:
    print(" 1. Agregar")
    print(" 2. Buscar")
    print(" 0. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        palabra = input("Ingrese la palabra: ") # la palabra es alegre
        sinonimo = input("Ingrese sinónimo: ")

        if palabra in diccionario:
            # {"alegre: ['contento']"} => la palabra existe, el sinónimo agregarlo a la lista de sinonimos
            lista_de_sinonimos = diccionario[palabra] # diccionario["alegre"]
            lista_de_sinonimos.append(sinonimo) # le vamor agregando sinonimos a la lista
        else:
            # creo el diccionario con la clave y el valor
            diccionario[palabra] = [sinonimo]

    elif opcion == 2:
        palabra = input("Ingrese la palabra: ") 
        if palabra in diccionario:
            print(diccionario[palabra])
        else: 
            print("No existe la palabra en el diccionario")

    elif opcion == 0:
        break



