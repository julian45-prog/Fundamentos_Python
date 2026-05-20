# Tuplas

# Estructura de una tupla
tupla1 = (1, 2, 3, 4, 5)
print(type(tupla1))

tupla2 = "a", "b", "c"
print(type(tupla2))

tupla3 = ("hola",)
print(type(tupla3))

tupla4 = tuple("hola")
print(type(tupla4))

tuplas_mixta = ("hola", 123, 3.14, True, [1, 2, 3])
print(tuplas_mixta)

# TUPLA DE APRENDICES SENA ADSO

# Indice:        0        1         2       3      4
aprendices = ("simon","carlos","alberto","Sara","Sofia")
print(aprendices)

# Acceder a un elemento de la tupla
print(aprendices[2]) # Santiago

# Consultar rangos de elementos de la lista
print(aprendices[0:2])
print(aprendices[1:4])
print(aprendices[1:])

# Sumar 2 tuplas
tupla_1 = (1,2,3)
tupla_2 = (4,5,6)
tupla_suma = tupla_1 + tupla_2
print(tupla_suma)

# Multiplicar una tupla
tupla_multiplicada = tupla_1 * 3
print(tupla_multiplicada)

# Medigar el largo con len()
print(len(aprendices))

# Contar elementos repetidos en una tupla con count
tupla_4 = (1,2,2,3,3,3)
print(tupla_4.count(2))
print(tupla_4.count(3))

# Obtener el indice de un elemento en una tupla
print(tupla_4.index(2))
print(tupla_4.index(3))

# Modificar una tupla en una lista
print(type(aprendices))
aprendices_lista = list(aprendices)
print(type(aprendices_lista))
aprendices_lista.append("Felipe")
print(aprendices_lista)

# comprovar si un elemento existe en una tupla
print("simon" in aprendices)
print("Felipe" in aprendices)

# Empaquetar tuplas

programa_1 = "ADSO" 
programa_2 = "SST"
programa_3 = "Topografia"

tupla_programas = (programa_1, programa_2, programa_3)
print(tupla_programas)

# Desempaquetar tuplas
tupla_desempaquetada = ("ADSO", "SST", "Topografia")
programa_1, programa_2, programa_3 = tupla_desempaquetada
print(programa_1)
print(programa_2)
print(programa_3)

# Ejercicio 2 deesempaquetar tuplas
tupla_ciudades_2 = ("Sogamoso", "Medellin", "Tunja")
ciudad_1, *ciudad_2, ciudad_3 = tupla_ciudades_2
print(ciudad_1)
print(ciudad_2)
print(ciudad_3)

# Iterar sobre una tupla con un ciclo for
for ciudad in tupla_ciudades_2:

    print(ciudad)

# Ejercicio Tuplas
#1
tupla_positivos = (1, 2, 3,)
tupla_negativos = (-1, 0,-2)
tupla_suma = tupla_positivos + tupla_negativos
print(tupla_suma)

#2
 
precios = (50,75,46,22,80,65,8)

precios_ordenados = sorted(precios)
print(precios_ordenados)