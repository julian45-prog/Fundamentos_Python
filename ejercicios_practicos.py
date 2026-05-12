# Ejercicio 1

nombre = "Felipe"
producto = 20000
promedio_asignatura = 4.5
print(f"Hola {nombre}, el valor del producto es {producto} y tu promedio en la asignatura es {promedio_asignatura}")

# Ejercicio 2

variable_1_entera = int(input("Ingrese el primer número entero: "))
variable_2_entera = int(input("Ingrese el segundo número entero: "))
variable_float = float(input("Ingrese un número decimal: "))
variable_1_string = input("Ingrese la primera cadena de texto: ")
variable_2_string = input("Ingrese la segunda cadena de texto: ")

suma_numeros= variable_1_entera + variable_2_entera + variable_float
print(f"La suma de los números es: {suma_numeros}")

# Ejercicio 3

base = 5
exponente = 3
resultado = base ** exponente

print(f"El resultado de {base} elevado a {exponente} es: {resultado}")


# Ejercicio 4

numeros = [2, 8, 9, 27, 28, 55, 121]
for numero in numeros:
    raiz_cuadrada = numero ** 0.5
    print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")

# Ejercicio 5    

nombre_estudiante = input("Ingrese el nombre del estudiante: ")
nota_1 = float(input("Ingrese la primera nota decimal: "))
nota_2 = float(input("Ingrese la segunda nota decimal: "))
nota_3 = float(input("Ingrese la tercera nota decimal: "))
nota_4 = float(input("Ingrese la cuarta nota decimal: "))
nota_5 = float(input("Ingrese la quinta nota decimal: "))
promedio_final = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5
print(f"El promedio final de {nombre_estudiante} es: {promedio_final}")


# Ejercicio 6

numeroUno = 8
numeroDos = 2
auxiliar = numeroUno
numeroUno = numeroDos
numeroDos = auxiliar
print(f"numeroUno: {numeroUno}, numeroDos: {numeroDos}")

# Ejercicio 7

estado = (5 == 2) or (2 > 1)
print(f"El estado es: {estado}")

# Ejercicio 8

resultado = (9/2) + 8*2/1-(2+2) /4+3
print(resultado)

# Ejercicio 9

ladoCuadrado = 8
area_cuadrado = ladoCuadrado ** 2
perimetro_cuadrado = 4 * ladoCuadrado
print(f"Cuadrado: lado={ladoCuadrado}, área={area_cuadrado}, perímetro={perimetro_cuadrado}")

baseTriangulo = 9
alturaTriangulo = 8
ladoUnoTriangulo = 8
ladoDosTriangulo = 8
area_triangulo = (baseTriangulo * alturaTriangulo) / 2
perimetro_triangulo = baseTriangulo + ladoUnoTriangulo + ladoDosTriangulo
print(f"Triángulo: base={baseTriangulo}, altura={alturaTriangulo}, área={area_triangulo}, perímetro={perimetro_triangulo}")

baseRectangulo = 8
alturaRectangulo = 6
area_rectangulo = baseRectangulo * alturaRectangulo
perimetro_rectangulo = 2 * (baseRectangulo + alturaRectangulo)
print(f"Rectángulo: base={baseRectangulo}, altura={alturaRectangulo}, área={area_rectangulo}, perímetro={perimetro_rectangulo}")

# Ejercicio 10

edad = int(input("Ingrese la edad de la persona: "))

if edad < 0:
    categoria = "Edad no válida"
elif edad <= 5:
    categoria = "Infante"
elif edad <= 10:
    categoria = "Niño"
elif edad <= 15:
    categoria = "Pre adolescente"
elif edad <= 18:
    categoria = "Adolescente"
elif edad <= 25:
    categoria = "Pre adulto"
elif edad <= 40:
    categoria = "Adulto"
elif edad <= 55:
    categoria = "Pre anciano"
else:
    categoria = "Anciano"

print(f"Edad: {edad}, categoría: {categoria}")












