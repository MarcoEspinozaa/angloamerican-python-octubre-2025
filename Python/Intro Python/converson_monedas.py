#Dólar a Euro, Euro a Dólar, Dólar a Peso Chileno
valor_euro = 1050
valor_dolar = 950

def dolar_euro(cantidad_dolares, dolar = 950, euro = 1050):
    #valor_en_pesos = cantidad_dolares*dolar
    #return (valor_en_pesos/euro)
    return ((cantidad_dolares*dolar)/euro)

def euro_dolar(cantidad_euros, dolar = valor_dolar, euro = valor_euro):
    #valor_en_pesos = cantidad_euros*euro
    #return (valor_en_pesos/dolar)
    return ((cantidad_euros*euro)/dolar)

def dolar_peso(cantidad_dolares, dolar = valor_dolar):
    return cantidad_dolares*dolar

def euro_peso(cantidad_euros, euro = valor_euro):
    return cantidad_euros*euro

def peso_dolar(pesos, dolar = valor_dolar):
    return pesos/dolar

def peso_euro(pesos, euro = valor_euro):
    return pesos/euro

'''while True:

    print("===== MENU ======")
    print(" 1. Transformar peso a dolar")
    print(" 2. Transformar peso a euro")
    print(" 3. Transformar euro a dolar")
    print(" 4. Transformar euro a peso")
    print(" 5. Transformar dolar a peso")
    print(" 6. Transformar dolar a euro")
    print(" 0. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 0:
        print("Hasta pronto")
        break'''

