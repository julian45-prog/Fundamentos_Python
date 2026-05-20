# actividad2_diccionarios.py

# Función para calcular el promedio de una lista de notas
def calcular_promedio(notas):
    return sum(notas) / len(notas)


# Diccionario principal: clave = número de ficha
aprendices = {
    "aprendiz1": {
        "nombre": "Julian",
        "edad": 17,
        "notas": [4.5, 3.8, 4.2, 4.0],
        "ciudad": "Sogamoso"
    },
    "aprendiz2": {
        "nombre": "Camila",
        "edad": 18,
        "notas": [2.8, 3.0, 2.9, 3.1],
        "ciudad": "Medellín"
    },
    "aprendiz3": {
        "nombre": "Andrés",
        "edad": 19,
        "notas": [4.8, 4.6, 4.9, 5.0],
        "ciudad": "Cali"
    },
    "aprendiz4": {
        "nombre": "Laura",
        "edad": 20,
        "notas": [2.5, 2.7, 3.0, 2.8],
        "ciudad": "Barranquilla"
    }
}

# 4. Agregar un nuevo aprendiz
aprendices["aprendiz5"] = {
    "nombre": "Sofía",
    "edad": 21,
    "notas": [3.5, 4.0, 3.8, 4.2],
    "ciudad": "Cartagena"
}

# Actualizar la ciudad de un aprendiz existente
aprendices["aprendiz2"]["ciudad"] = "Manizales"

# 3. Reporte general
print("=== REPORTE DE APRENDICES ===\n")

for ficha, datos in aprendices.items():
    promedio = calcular_promedio(datos["notas"])
    estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"

    print(f"Ficha: {ficha}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print(f"Ciudad: {datos['ciudad']}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {estado}")
    print("-" * 30)

# 5. Bonus: Ordenar de mayor a menor promedio
print("\n=== APRENDICES ORDENADOS POR PROMEDIO ===\n")

ordenados = sorted(
    aprendices.items(),
    key=lambda item: calcular_promedio(item[1]["notas"]),
    reverse=True
)

for ficha, datos in ordenados:
    promedio = calcular_promedio(datos["notas"])
    print(f"{datos['nombre']} (Ficha {ficha}) - Promedio: {promedio:.2f}")