# Actividad 2: Analisis de temperaturas Semanales

temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18,
20, 22, 19]

print(f"Temperatura del primer día: {temperaturas[0]}°C")
print(f"Temperatura del último día: {temperaturas[-1]}°C")
print(f"Temperatura del día 7 (mitad): {temperaturas[6]}°C")
print(f"Temperatura del penúltimo día: {temperaturas[-2]}°C")

# Extraer semanas
primera_semana = temperaturas[0:7]
segunda_semana = temperaturas[7:14]

print(f"Primera semana: {primera_semana}")
print(f"Segunda semana: {segunda_semana}")

# Días pares
dias_pares = temperaturas[1:14:2]
print(f"Días pares: {dias_pares}")

# Lista en orden invertido
temperaturas_invertidas = temperaturas[::-1]
print(f"Temperaturas en orden invertido: {temperaturas_invertidas}")

# Calcular promedios
promedio_primera_semana = sum(primera_semana) / len(primera_semana)
promedio_segunda_semana = sum(segunda_semana) / len(segunda_semana)

print(f"Promedio primera semana: {promedio_primera_semana:.2f}°C")
print(f"Promedio segunda semana: {promedio_segunda_semana:.2f}°C")

# Bonus
if promedio_primera_semana > promedio_segunda_semana:
    print("La primera semana tuvo mayor temperatura promedio.")
elif promedio_segunda_semana > promedio_primera_semana:
    print("La segunda semana tuvo mayor temperatura promedio.")
else:
    print("Ambas semanas tuvieron la misma temperatura promedio.")  

