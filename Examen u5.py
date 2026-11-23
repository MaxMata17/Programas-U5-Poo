
estudiantes = int(input("Cuantos estudiantes hay en el grupo: "))
materias = int(input("Cuantas materias tiene el grupo: "))

# Crear matriz
calificaciones = []


for i in range(estudiantes):
    fila = []
    print("\nEstudiante", i + 1)

    for j in range(materias):
        nota = float(input("Calificacion de la materia " + str(j + 1) + ": "))

        while nota < 0 or nota > 100:
            print("La calificacion debe estar entre 0 y 100")
            nota = float(input("Ingresa nuevamente la calificacion: "))

        fila.append(nota)

    calificaciones.append(fila)


print("\n Calificaciones")

for i in range(estudiantes):
    print("Estudiante", i + 1, ":", calificaciones[i])


print("\n Promedio por estudiante")

for i in range(estudiantes):
    promedio = sum(calificaciones[i]) / materias
    print("Estudiante", i + 1, ":", round(promedio, 2))

print("\n Promedio por materia")

for j in range(materias):
    suma = 0

    for i in range(estudiantes):
        suma = suma + calificaciones[i][j]

    promedio = suma / estudiantes
    print("Materia", j + 1, ":", round(promedio, 2))


mayor = max(max(fila) for fila in calificaciones)
menor = min(min(fila) for fila in calificaciones)

print("\n Resultados generales")
print("Calificacion mas alta:", mayor)
print("Calificacion mas baja:", menor)

