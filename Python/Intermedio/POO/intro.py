# RECORDATORIO:
# camel case => soyUnaFuncion():
# snake case => soy_una_funcion():
# pascal case => SoyUnaFuncion():

class Automovil():
    def __init__(self, marca, modelo, cilindraje, combustible, transmision, consumo):
        self.marca = marca
        self.modelo = modelo
        self.cilindraje = cilindraje
        self.combustible = combustible
        self.transmision = transmision
        self.consumo = consumo
        self.cant_ruedad = 4

    def encender(self):
        print("El automovil se está encendiendo")

    def apagar(self):
        print("El automovil se apagó")

    def consumo_por_litro(self, precio_combustible:int):
        return self.consumo * precio_combustible

auto1 = Automovil("ford", "fiesta", "2.5cc", "gasolina", "manual", 5)
auto2 = Automovil("toyota", "rav4", "2.5cc", "diesel", "automática", 10)
#print(auto2.cant_ruedad)

auto2.cant_ruedad = 2

'''print(f"el auto numero 1 es un {auto1.marca} {auto1.modelo}, con transmisión {auto1.transmision} y {auto1.cant_ruedad} ruedas")
print(f"el auto numero 1 es un {auto2.marca} {auto2.modelo}, con transmisión {auto2.transmision} y {auto2.cant_ruedad} ruedas")'''

auto1.encender()
auto2.apagar()
consumo_auto1 = auto1.consumo_por_litro(1290)

print(f"el consumo del auto 1 es de {consumo_auto1} pesos")