# Operadores aritméticos en Python

a = 3
b = 2

# Suma
suma = a + b
print(f"La Suma de {a} y {b} es: {suma}")

# Resta
resta = a - b
print(f"La Resta de {a} y {b} es: {resta}")

# Multiplicación
multiplicacion = a * b      
print(f"La Multiplicación de {a} y {b} es: {multiplicacion}")

# División
division = a / b
print(f"La División de {a} y {b} es: {division}")

# Módulo
modulo = a % b

print(f"El Módulo de {a} y {b} es: {modulo}")

# División entera
division_entera = a // b
print(f"La División Entera de {a} y {b} es: {division_entera}")

# Potencia
potencia = a ** b
print(f"{a} elevado a la {b} es: {potencia}")

#Potencia de Operadores
resultado = a + b * 2
print(f"El resultado de la operación {a} + {b} * 2 es: {resultado}")

resultado_parentesis = (a + b) * 2
print(f"El resultado de la operación ({a} + {b}) * 2 es: {resultado_parentesis}")

resultado_3 = a * b // 3
print(f"El resultado de la operación {a} * {b} // 3 es: {resultado_3}")

resultado_4 = (a * b) // 3
print(f"El resultado de la operación ({a} * {b}) // 3 es: {resultado_4}")

resultado_5 = a * (b // 3)
print(f"El resultado de la operación {a} * ({b} // 3) es: {resultado_5}")

ejercicio = ((a - b) * (a-b) / (a * b)) - ((a ** b) % 3)
# Ejercicio = ((3 - 2) * (3-2) / (3 * 2)) - ((3 ** 2) % 3)
# Ejercicio = ((1) * (1) / (6)) - ((9) % 3)
# Ejercicio = (1 / 6) - (0)
# Ejercicio = 0.16666666666666666

print(f"El resultado del ejercicio (({a} - {b}) * ({a}-{b}) / ({a} * {b})) - (({a} ** {b}) % 3) es: {ejercicio}")

# Librerias de Matematicas
import math

print(math.pi)
print(math.e)

print(math.sqrt(16))

import random

random.random()  # Genera un número aleatorio entre 0 y 1
numero_aleatorio = random.randint(1, 10)  # número aleatorio entre 1 y 10
print(numero_aleatorio)









