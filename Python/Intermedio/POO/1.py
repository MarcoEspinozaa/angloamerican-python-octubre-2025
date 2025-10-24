estudiantes = [
    {"nombre": "juan", "edad": 17, "calificaciones": [85, 90, 88]}
    ,
    {"nombre": "Maria", "edad": 19, "calificaciones": [92, 89, 90]}
    ,
    {"nombre": "Pedro", "edad": 21, "calificaciones": [85, 95, 80]}
    ,
    {"nombre": "Ana", "edad": 18, "calificaciones": [90, 90, 87]}
    ,
    {"nombre": "Luis", "edad": 20, "calificaciones": [88, 85, 50]}
    ,
]

juanito = {
    "nombre": "juan", 
    "edad": 17, 
    "calificaciones": [85, 90, 88]
    }

juanito["nombre"] # => "juan"
juanito["edad"] # 17
juanito["calificaciones"] # [85, 90, 88]

for indice, i in enumerate(estudiantes, start=1):
    print(f"en el ciclo {indice} la variable i representa: {i}")

    notas = i["calificaciones"]
    print(f"y sus notas son {notas}")