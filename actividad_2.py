# Calculadora de Notas en Python
nota_1 = float(input("Ingrese su primera nota: "))
nota_2 = float(input("Ingrese su segunda nota: "))
nota_3 = float(input("Ingrese su tercera nota: "))

# Calcular promedio
promedio = round((nota_1 + nota_2 + nota_3) / 3, 2)

# Calcular puntos faltantes para 5.0
puntos_faltantes = max(0, round(5.0 - promedio, 2))

# Mostrar resultados
print("\n--- RESULTADOS ---")
print(f"Promedio: {promedio}")

# Evaluar si aprueba
if promedio >= 3.0:
    print("Estado: APROBÓ")
else:
    print("Estado: NO APROBÓ")

print(f"Puntos para llegar a 5.0: {puntos_faltantes}")