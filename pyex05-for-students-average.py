numero_estudiantes = int(input("Ingrese número de estudiantes: "))
numero_materias = int(input("Ingrese número de materias: "))
total_beca = 0
for e in range(numero_estudiantes):
    promedio = 0
    for i in range(numero_materias):
        cal_materia = int(input(f"Ingrese la calificación del material {i} para el estudiante {e} (sobre 10): "))
        promedio += cal_materia
    promedio /= numero_materias
    if promedio >= 8 :
        total_beca += 1
print(f"Hay {total_beca} estudiantes con derecho a beca")
    