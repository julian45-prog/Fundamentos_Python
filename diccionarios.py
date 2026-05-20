# Diccionarios (Caracteristicas a u elemento)

# Cracion de un Diccionario

#Estructura de un Diccionario
diccionario = {
    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3"
}

# Diccionario Vacio
diccionario_vacio = {}

# Diccionario con elementos
diccionario_aprendiz = {
    "nombre": "Felipe",
    "apellido": "Gomez",
    "programa":"ADSO",
    "ficha": "3321349",
    "edad": 25
}
print(type(diccionario_aprendiz)) 

# Obtener el valor del diccionario
print(diccionario_aprendiz["nombre"])
print(diccionario_aprendiz.get("apellido"))

# Obtner solo las claves del diccionario
print(diccionario_aprendiz.keys())

# Obtener solo los valores del diccionario
print(diccionario_aprendiz.values())

# Obtener las claves y los valores del diccionario
print(diccionario_aprendiz.items())

# Agregar un nuevo elemento al diccionario
diccionario_aprendiz["correo"] = "felipe.gomez@correo.com"

# Modificar un valor del diccionario
diccionario_aprendiz["edad"] = 26
print(diccionario_aprendiz)

# metodo UPDATE ()
diccionario_aprendiz.update({"telefono": "123456789"})
print(diccionario_aprendiz)

# Comprobar pertenencia (in)
if "ficha" in diccionario_aprendiz:
    print("La ficha existe en el diccionario")

# Recorrer solo las claves deñ Diccionario
for clave in diccionario_aprendiz.keys():
    print(clave)

# Recorrer solo los valores del diccionario
for valor in diccionario_aprendiz.values():
    print(valor)

# Recorrer las claves y los valores del diccionario
for clave, valor in diccionario_aprendiz.items():
    print(f"{clave}: {valor}")

# Eliminar Elementos en un Diccionario con POP(clave)
diccionario_aprendiz.popitem() # Elimina el ultimo elemento agregado al diccionario
print(diccionario_aprendiz)     



diccionario_aprendiz.clear() # Elimina todos los elementos del diccionario
print(diccionario_aprendiz)

# Diccionarios Anidados

aprendices = {
    "aprendiz1": {
        "nombre": "Felipe",
        "apellido": "Gomez",
        "programa":"ADSO",
        "ficha": "3321349",
        "edad": 25,
        "telefono": "123456789"
    },
    "aprendiz2": {
        "nombre": "Santiago",
        "apellido": "Perez",
        "programa":"SST",
        "ficha": "3321350",
        "edad": 24,
        "telefono": "987654321"
    },
    "aprendiz3": {
        "nombre": "Maria",
        "apellido": "Lopez",
        "programa":"Topografia",
        "ficha": "3321351",
        "edad": 26,
        "telefono": "555555555"
    }
}
# Acceder a un valor en un diccionario anidado
print(aprendices["aprendiz1"]["nombre"])

# Recorrer un Diccionario Anidado con un ciclo for
for aprendiz, datos in aprendices.items():
    print(f"Datos del {aprendiz}:")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")
    
