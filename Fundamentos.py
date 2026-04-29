
#Tipos de Variables
nombre = "Julian"
apellido = "Univio"
edad = 19
altura = 1.71
activo = True
correo = "univiojulian255@gmail.com"
telefono = "3208543405"

telefono_int = int(telefono)
cedula = "1234567890"
cedula_str = str(cedula)

#Casting
print(type(nombre),nombre)
print(type(apellido),apellido)
print(type(edad),edad)
print(type(altura),altura)
print(type(activo),activo)
print(type(correo),correo)
print(type(telefono),telefono)
print(type(telefono_int),telefono_int)
print(type(cedula),cedula)

'''Esto es comentario de varias lineas
para explicar el codigo'''

#Indentación en Python 
if 5 > 2:
    print("5 es mayor que 2")
else:
    print("5 no es mayor que 2")

#Inputs

nombre_completo = input("Ingrese su nombre completo: ")  
print("nombre_completo")

     #Imprimir con formato f-string     
print(f"{nombre_completo}")     
print(f"hola {nombre_completo},tienes {edad} años.")     


