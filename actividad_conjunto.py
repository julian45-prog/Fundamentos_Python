# actividad4_sets.py

# 1. Conjuntos de aprendices por programa
python_curso = {'Ana', 'Luis', 'Marta', 'Carlos', 'Sofia', 'Pedro'}
java_curso = {'Luis', 'Carlos', 'Pedro', 'Laura', 'Diego'}
bd_curso = {'Marta', 'Sofia', 'Laura', 'Ana', 'Miguel'}

# 2. Operaciones con conjuntos

# Unión triple: todos los aprendices únicos
todos = python_curso | java_curso | bd_curso
print("Total de aprendices únicos:", len(todos))
print("Aprendices únicos:", todos)
print()

# Aprendices que cursan Python y Java
python_y_java = python_curso & java_curso
print("Aprendices en Python y Java:", python_y_java)
print()

# Aprendices que solo están en Python
solo_python = python_curso - java_curso - bd_curso
print("Aprendices solo en Python:", solo_python)
print()

# Aprendices en exactamente dos programas
exactamente_dos = (
    (python_curso & java_curso) |
    (python_curso & bd_curso) |
    (java_curso & bd_curso)
) - (python_curso & java_curso & bd_curso)

print("Aprendices en exactamente dos programas:", exactamente_dos)
print()

# 3. Lista con duplicados
inscripciones = [
    'Ana', 'Luis', 'Ana', 'Marta',
    'Carlos', 'Luis', 'Sofia', 'Pedro', 'Ana'
]

inscritos_unicos = set(inscripciones)

print("Cantidad de inscritos únicos:", len(inscritos_unicos))
print("Inscritos únicos:", inscritos_unicos)
print()

# 4. Diccionario con número de programas por aprendiz
conteo_programas = {
    aprendiz:
        (aprendiz in python_curso) +
        (aprendiz in java_curso) +
        (aprendiz in bd_curso)
    for aprendiz in todos
}

print("Conteo de programas por aprendiz:")
for aprendiz, cantidad in conteo_programas.items():
    print(f"{aprendiz}: {cantidad}")
print()

# 5. Bonus: Aprendices en los tres programas
en_los_tres = python_curso & java_curso & bd_curso

print("Aprendices matriculados en los tres programas:", en_los_tres)