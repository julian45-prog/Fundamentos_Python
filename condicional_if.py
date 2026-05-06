#Condicional IF/ELIF/ELSE
if True : 

    print("La condicion es Verdadera")

elif False:
    print("La segunda condicion es verdadera en elif")

elif False:
    print("la segunda condicion es verdadera en elif")    

else:
    print("la condicion es falsa")    
       

# Ejercicio: Clasificacion de Edad

edad = 70

if edad < 18:
    print("Eres un menor de edad")

elif edad >=18 and edad < 65:
    print("Eres un adulto")    

else:
     print("Eres un adulto mayor")    

# Ejercicio: Clasificacion de Edad IF anidado

edad= int(input("Ingrese su Edad para ser Clasificada: "))

if edad < 18:
    if edad > 12 and edad < 18:
        print("adolescente")
    else:


        print("Niño")    
else: 
     if edad >=18 and edad < 60:
      print("Eres un adulto")    
     else:
         print("Eres un adulto mayor")   

# Operador ternerario

numero = 4

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")    

#Montamos todo en una sola linea para tener menos lineas de codigo

print("El numero es par" if numero & 2 == 0 else "El numero es impar")             


 

         





