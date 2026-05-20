# CONNJUNTOS (SETS) EN PYTHON

# Estructura de conjunto
conjunto = set()
print(type(conjunto))

# --- Creación ---
lenguajes = {"Python", "Java", "C++", "JavaScript"}
print(lenguajes)


# --- Metodos de modificación ---
frutas = {"manzana", "banana", "naranja","mora"}
frutas.add("pera") # Agregar un elemento al conjunto
frutas.update({"manzana"}) # Agregar un elemento que ya existe (no se agrega)
frutas.remove("mora") # Eliminar un elemento del conjunto (si no existe, lanza error)
frutas.discard("papaya") # Eliminar un elemento del conjunto (si no existe
elem = frutas.pop() # Eliminar un elemento aleatorio del conjunto y devolverlo
print(frutas)

python_devs = {"Alice", "Bob", "Charlie"}
java_devs = {"Bob", "David", "Eve"}

todos_los_devs = python_devs | java_devs # Unión de conjuntos
union = python_devs.union(java_devs) # Unión de conjuntos
print(todos_los_devs)

devs_en_ambos = python_devs & java_devs # Intersección de conjuntos
interseccion = python_devs.intersection(java_devs) # Intersección de conjuntos
print(devs_en_ambos)

# Intersección 
devs_unicos = python_devs - java_devs # Diferencia de conjuntos
diferencia = python_devs.difference(java_devs) # Diferencia de conjuntos
print(devs_unicos)

devs_uni = java_devs - python_devs
print(devs_uni)

# Diferencia Simetrica 

exclusivos = python_devs ^ java_devs
print(exclusivos)
