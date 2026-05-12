# LISTAS

# Estructura de una Lista

#Indice: 0                     1             2
from sre_constants import CATEGORY_UNI_NOT_SPACE


listas = ["objeto_1", "objeto_2", "objeto_3"]
print(type(listas))

listas_mixtas = ["Hola", 42, 3.14, True, [1,2,3]]
print(listas_mixtas)

# Crear una lista vacía

aprendices = []

print(aprendices)


# Lista de Aprendices Sena Adso
# Indice:                   0        1         2        3       4
# Indice negativo:           -5       -4        -3       -2      -1

aprendices_sena_adso = ["Andres", "Camilo", "Diana", "Jorge", "Sofia"]
print(aprendices_sena_adso)

#Acceder a un elemento de la lista
print(aprendices_sena_adso[1]) # Camilo
print(aprendices_sena_adso[-1]) # Sofia

# Modificar un elemento de la lista
aprendices_sena_adso[2] = "Maria"
print(aprendices_sena_adso)

# Consultar rangos de elementos en la lista}

print(aprendices_sena_adso[1:4]) # Camilo, Maria,
print(aprendices_sena_adso[:3]) # Andres, Camilo, Maria
print(aprendices_sena_adso[2:]) # Maria, Jorge, Sofia
print(aprendices_sena_adso[:]) # Andres, Camilo, Maria, Jorge, Sofia
print(aprendices_sena_adso[-3:]) # Maria, Jorge, Sofia
print(aprendices_sena_adso[:2:4])

aprendices_ficha_3321349 = ["Andres", "Camilo", "Diana", "Jorge", "Sofia"]
aprendices_ficha_3321350 = ["Ana", "Luis", "Carlos", "Maria", "Sofia"]

# Concatenar listas + 
aprendices_adso = aprendices_ficha_3321349 + aprendices_ficha_3321350
print(aprendices_adso)

# Unir listas con extend

aprendices_ficha_3321349.extend(aprendices_ficha_3321350)
print(aprendices_ficha_3321349)

# Medir el largo con len()
print(len(aprendices_adso))

# Contar elementos repetidos con count

print(aprendices_adso.count("Sofia"))

count_sofia = aprendices_adso.count("Sofia")
print(f"El nombre Sofia se repite {count_sofia} veces en la lista aprendices_adso")

# Obtenr el indice de un elemento con index
indice_carlos = aprendices_adso.index("Carlos")
print(f"El nombre Carlos se encuentra en el indice {indice_carlos} de la lista aprendices_adso")

# Copiar una lista con copy
aprendices_adso_copia = aprendices_adso.copy()
print(aprendices_adso_copia)

# Agregar  elementos a la lista con append e insert
aprendices_adso.append("Valentina") # Agrega al final de la lista
print(aprendices_adso)

aprendices_adso.insert(2, "Valery")# Agrega en el indice 2 de la lista
print(aprendices_adso)

# Eliminar elementos de la lista con (remove y pop)
aprendices_adso.remove("Valentina") # Elimina el primer elemento que coincida con el valor
aprendices_adso.pop(5) # Elimina el elemento en el indice 5

# Comprobar pertenencia (in)
if "Sara" in aprendices_adso:
    print("Sara se encuentra en la lista aprendices_adso")
else:
    print("Sara no se encuentra en la lista aprendices_adso")    

# Ordenar (sort y reverse)    

aprendices_adso.sort() # Ordena la lista de forma ascendente
print(aprendices_adso)

aprendices_adso.reverse() # Ordena la lista de forma descendente
print(aprendices_adso)

aprendices_adso.clear() # Elimina todos los elementos de la lista
print(aprendices_adso)