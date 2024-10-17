# Calcula el número de estudiantes que pueden optar a una beca en función de su promedio
numero_estudiantes = int(input("Introduce numero de estudiantes : "))
numero_materias = int(input("Introduce numero de materias : "))
total_beca = 0
for e in range(numero_estudiantes):
    promedio = 0
    for i in range(numero_materias):
        cal_materia = int(input(f"Introduce la clasificación del material {i} para el estudiante {e} (/10): "))
        promedio += cal_materia
    promedio /= numero_materias
    if promedio >= 8 :
        total_beca += 1
print(f"Hay {total_beca} estudiantes con derecho a beca")
    

