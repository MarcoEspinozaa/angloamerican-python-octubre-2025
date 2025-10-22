'''Crea un programa que: - Pida por teclado el nombre y las notas de 3 estudiantes. - Guarde cada
estudiante en un diccionario con estructura: {"nombre": "Juan", "notas": [5.5, 6.0, 6.5]}. -
Almacene los diccionarios en una lista. - Luego, calcule el promedio de cada alumno y muestre
cuál tiene la nota más alta.'''

estudiantes = []

for i in range(3):
    nombre = input("Ingrese nombre: ")

    notas = []
    for j in range(3):
        nota = float(input("Ingrese nota " + str(j+1) + " : "))
        notas.append(nota)
    
    estudiante = {
        "nombre":nombre, 
        "notas": notas 
        }
    
    estudiantes.append(estudiante)

mejor_promedio = 0
mejor_nombre = ""

for alumno in estudiantes:
    suma = 0
    notas = alumno["notas"]

    # for nota in alumno["notas"]
    for nota in notas:
        suma = suma + nota
        #suma += nota

    promedio = suma/len(notas)

    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_nombre = alumno["nombre"]

print(f"El promedio más alto es del estudiante {mejor_nombre} con un promedio de {mejor_promedio}")
    
    
