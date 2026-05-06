# Clasificador de IMC

# Solicitar datos
peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

# Validación (bonus)
if peso <= 0 or estatura <= 0:
    print("Error: el peso y la estatura deben ser valores positivos.")
else:
    # Calcular IMC
    imc = round(peso / (estatura ** 2), 2)

    # Clasificación
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif imc < 25:
        clasificacion = "Normal"
    elif imc < 30:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"

    # Mostrar resultados
    print("\n--- RESULTADOS ---")
    print(f"IMC: {imc}")
    print(f"Clasificación: {clasificacion}")